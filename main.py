#!/usr/bin/env python3

import sys
import argparse
from datetime import datetime
import json
import time
from retry import retry

import metric_descriptions
from node_tracker import NodeTracker
import requests
from result_parser import ResultParser

import config as cfg
import graphyte

class MetricGatherer():
    def __init__(self):
        self.node_tracker = NodeTracker()

    def to_url_params(self, metric_description):
        return "metrics={}&dim={}&agg={}&nodes=all".format(
            metric_description.name, ",".join(metric_description.dimensions),metric_description.agg)

    @retry(delay=1)

    def get_metric(self, metric_description):
        BASE_URL = 'http://' + cfg.elastic['es_host'] + ':9600/_opendistro/_performanceanalyzer/metrics?'
        url = "{}{}".format(BASE_URL, self.to_url_params(metric_description))
        return requests.get(url,timeout=2)

    def get_all_metrics(self):
        ''' Loops through all the metric descriptions, sending one at a time,
            parsing the results, and returning a list of dicts '''
        docs = []
        for metric in metric_descriptions.get_working_metric_descriptions():
            result = self.get_metric(metric)
            if result.status_code != 200:
                print("FAIL", metric, '\n', result.text)
            else:
                rp = ResultParser(metric, result.text, self.node_tracker)
                for doc in rp.records():
                    docs.append(doc)
        return docs

class MetricWriter():
  def put_graphite(self, docs):
      for doc in docs:

          keys = list(doc)
          hostname = doc['node_fqdn'].split('.')[0]

          metric_path = hostname + '.openelastic.' + doc['metric'] + '.' + str(doc[keys[1]]) + '_' + doc['agg'] 
          metric_value = (doc[doc['metric']])
#          print(metric_path + " " + str(metric_value))
          graphyte.send(metric_path, float(metric_value))


def init_graphite():
    ''' Init Graphite '''
    graphyte.init(cfg.graphite['g_host'], prefix=cfg.graphite['prefix'], interval=20 )

if __name__ == '__main__':

  init_graphite()

  while 1:

    # limit execution speed
    target=(int(time.time())) + 5

    # print(str(int(time.time())) + ' target: ' + str(target))

    docs = MetricGatherer().get_all_metrics()

    MetricWriter().put_graphite(docs)

    while True:
      if int(time.time()) >= int(target):
        break
      time.sleep(1)

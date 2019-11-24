#!/bin/python3

import sys
import argparse
from datetime import datetime
import json

import metric_descriptions
from node_tracker import NodeTracker
from pytz import timezone
import requests
from result_parser import ResultParser
import config as cfg
import graphyte

class MetricGatherer():
    ''' Use this class to retrieve metrics from Open Distro's Performance
        Analyzer. Call get_all_metrics() to receive a list of ES docs. '''

    def __init__(self):
        self.node_tracker = NodeTracker()

    def to_url_params(self, metric_description):
        '''Converts a metric description into the corresponding URL params'''
        return "metrics={}&dim={}&agg={}&nodes=all".format(
            metric_description.name, ",".join(metric_description.dimensions),
            metric_description.agg)

    def get_metric(self, metric_description):
        BASE_URL = 'http://' + cfg.elastic['es_host'] + ':9600/_opendistro/_performanceanalyzer/metrics?'
        url = "{}{}".format(BASE_URL, self.to_url_params(metric_description))
        return requests.get(url,timeout=2)

    def get_all_metrics(self):
        ''' Loops through all the metric descriptions, sending one at a time,
            parsing the results, and returning a list of dicts, each one 
            representing one future Elasticsearch document. '''
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
    ''' Use this class to send metrics to graphite'''

    def put_doc_batches(self, docs):
        for doc in docs:

	    # new formatting
            keys = list(doc)

            metric1 = doc['node_fqdn'] + '.' + doc['metric'] + '.'
            metric2 = str(doc[keys[1]]) + '_' + doc['agg']
            print(metric1 + metric2 + " " + str(doc[keys[2]]))

def init_graphite():
    ''' Init Graphite '''
    print('connecting to graphite')
    graphyte.init('carbon1.localnetm', prefix='openelastic')
    

if __name__ == '__main__':
    init_graphite()
    while 1:
    #    print('Gathering docs')
        docs = MetricGatherer().get_all_metrics()
    #    print('Sending docs: ', len(docs))
        MetricWriter().put_doc_batches(docs)

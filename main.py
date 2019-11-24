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
    ''' Use this class to send documents in bulk to Elasticsearch'''

    def __init__(self, args):
        ''' Recieves the command-line args, which must include an index root,
            and an ES type. '''
        self.index_name = args.index_name 
        self.index_type = args.index_type
        self.seven = args.seven

    def now_pst(self):
        '''Return the current time in PST timezone'''
        ''' TODO: This should use the timezone of the current host or UTC.'''
        now_utc = datetime.now(timezone('UTC'))
        return now_utc.astimezone(timezone('US/Pacific'))

    def put_doc_batches(self, docs):
        ''' Takes a list of Elasticsearch documents, interleaves the control
            lines and sends them via the _bulk API.'''
        batch = []
        for doc in docs:
            ''' It would be better to take the index name from the doc's
                timestamp. Otherwise weird stuff happens at midnight.'''
            batch.append((doc))

	    # new formatting
            
            print (doc['node_fqdn'] + ',' + doc['metric'] + ',' , end ='')
            statickeys = ['node_fqdn', 'metric', '@timestamp', 'agg']
            for keys in doc.keys():
              if keys in statickeys:
                continue
#              print('key ' + keys +' ')
              print(str(doc[keys]) + ',' , end='')
            print(doc['agg'])
#            print (doc['node_fqdn'] + ',' +  doc['metric'])

#        bulk = '\n'.join(batch) + '\n'
        bulk = (batch)
#        print("Sending batch of {} characters".format(len(bulk)))


#        print(json.dumps(bulk, indent=4))



#        result = requests.post('https://localhost:9200/_bulk', 
#                               data=bulk,
#                               headers={'Content-Type':'application/json'},
#                               ### HACK ALERT !!! TODO TODO TODO ###
#                               auth=('admin', 'admin'),
#                               verify=False)
#        print('Sent batch', result.status_code)

def get_args():
    ''' Parse command line arguments '''
    description = 'Send performance data from Open Distro for Elasticsearch to Elasticsearch'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--index-name', type=str, default='pa',
                        help='root string for the index name for performance indexes', 
                        action='store')
    parser.add_argument('-t', '--index-type', type=str, default='log',
                        help='root string for the index type for performance indexes', 
                        action='store')
    parser.add_argument('--seven', default=False, action='store_true',
                        help='send data to ES 7 (removes type)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    while 1:
    #    print('Gathering docs')
        docs = MetricGatherer().get_all_metrics()
    #    print('Sending docs: ', len(docs))
        MetricWriter(get_args()).put_doc_batches(docs)

import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import config as cfg

class NodeTracker():
    ''' Discovers nodes in the cluster, and holds a map from node name to
        ip address. Construct the object, then use ip() to retrieve the 
        address from the node name.'''

    def __init__(self):
        ''' Constructs a local dict, and fills it.'''
        self._nodes_map = dict()
        self._retrieve_node_ids_and_ips()

    def _retrieve_node_ids_and_ips(self):
#        pass=cfg.elastic['pass']
        response = requests.get('https://' + cfg.elastic['es_host'] + ':9200/_nodes',
            auth=((cfg.elastic['user']), (cfg.elastic['pass'])),
            verify=False,timeout=2)
        if int(response.status_code) >= 300:
            raise Exception('Bad response code trying to get node names and ips') 
        json_response = json.loads(response.text)
        if 'nodes' not in json_response:
            raise Exception('Bad response - no nodes') 
        for node_id, values in json_response['nodes'].items():
            self._nodes_map[node_id] = values['ip']
            self._nodes_map[node_id] = values['name']

    def ip(self, node_name):
        if node_name in self._nodes_map:
            return self._nodes_map[node_name]
        raise ValueError('{} is not a recognized node name'.format(node_name))

    def print_table(self):
        for name, ip in self._nodes_map.items():
            print(' {}    {}'.format(name, ip))

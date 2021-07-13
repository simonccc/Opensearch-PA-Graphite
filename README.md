# AWS "Open" distro Elasticsearch Performance analyzer output to Graphite

Provides a main.py script that collects some of the metrics exported Performance Analyzer.

It pushes those metrics to Graphite for visualiation with eg Grafana.

It is a modificaton of the code posted here https://github.com/opendistro-for-elasticsearch/community/tree/master/pa-to-es

It uses the node hostnames rather that nodeid's and assumes you want to write to graphite in the form of

$prefix/nodename/openelastic/$metric blah

## Usage

Create a config.py based on the example example-config.py

`python3 ./main.py`

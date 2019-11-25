# Opendistro for Elasticsearch Performance analyzer output to Graphite

This library provides a main.py script that collects some of the metrics
surfaced by Performance Analyzer.

It pushes those metrics to Graphite for visualiation with eg Grafana.

It is a very small modificaton of the code posted here https://github.com/opendistro-for-elasticsearch/community/tree/master/pa-to-es

It uses the node hostnames rather that nodeid's and assumes you want to write to graphite in the form of

$prefix/nodename/openleastic/$metric blah

## Requirements

The code requires Python 3

pip3 install -r requirements.txt


## Basic Usage

Create a config.py based on the example example-config.py

python3 main.py

## Code of Conduct

This project has adopted an [Open Source Code of
Conduct](https://opendistro.github.io/for-elasticsearch/codeofconduct.html).

## Licensing

See the [LICENSE](./LICENSE) file for our project's licensing. We will ask you
to confirm the licensing of your contribution.

## Copyright

Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

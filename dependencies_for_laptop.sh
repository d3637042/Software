#!/bin/bash
set -e
set -x

# Important: always use the python-X library if available,
# rather than doing "pip install X".

sudo apt install -y \
	python-frozendict \
	libxslt-dev \
	libxml2-dev \
	python-lxml \
	python-bs4 \
	python-tables


pip install --upgrade --user \
	PyContracts \
	QuickApp \
	conftools \
	comptests \
	procgraph \
	pymongo \
	ruamel.yaml==0.15.34
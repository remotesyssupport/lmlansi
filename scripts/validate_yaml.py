#!/usr/bin/env python
# Script to validate yml and dump as json
# Yaml Syntak:
#     http://docs.ansible.com/YAMLSyntax.html
# Online checkers:
#     http://data-lint.herokuapp.com/
#     http://yamllint.com/
#     http://yaml-online-parser.appspot.com/

import json
import sys
import yaml

fh = open(sys.argv[1])
try:
    data = yaml.load(fh)
except yaml.error.YAMLError, e:
    print e
    sys.exit(1)
print json.dumps(data, indent=4, sort_keys=True)

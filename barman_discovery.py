#!/usr/bin/env python
from __future__ import print_function

import json
import subprocess
import sys

try:
    barman_list = subprocess.Popen(['barman','list-server'],stdout=subprocess.PIPE)
except (OSError) as e:
    print(e)
    print("install barman first",file=sys.stdout)
    sys.exit(1)

value = {'data':[] }

for line in barman_list.stdout:
    server = line.decode().split(' ')[0]
    value['data'].append({'{#SERVER}':server})
print (json.dumps(value))

#!/usr/bin/python

import subprocess
import json

barman_list = subprocess.Popen(['barman','list-server'],stdout=subprocess.PIPE)

value = {'data':[] }

for line in barman_list.stdout:
    server = line.split(' ')[0]
    value['data'].append({'{#SERVER}':server})
print json.dumps(value)

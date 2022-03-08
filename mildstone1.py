# -*- coding: utf-8 -*-
"""mildstone1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FZE-tXqCMmmJH_nipcOhmoPj7uHxcgKa
"""

! pip install pyyaml

import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('/content/Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

print(data['M1A_Workflow']['Activities']['TaskA']['Inputs']['ExecutionTime'])

import time
def TimeFunction(e):
  time.sleep(e)

import logging
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

d=list(data)
print(d[0][0])

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

logging.basicConfig(format='%(asctime)s')
logger = logging.getLogger()
# logger.setLevel(logging.INFO) 
logger.info('Entry')
TimeFunction(int(data['M1A_Workflow']['Activities']['TaskA']['Inputs']['ExecutionTime']))
logger.info('Executing')
#!/usr/bin/env python

import json

import requests

def run ():
  with open('../users.json', 'r') as fh:
    data = json.load(fh)
    
  for d in data:
    print(d)
    
if __name__ == '__main__':
  run()
  
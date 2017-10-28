#!/usr/bin/env python

import json
import subprocess

import requests

def run ():
  with open('../users.json', 'r') as fh:
    data = json.load(fh)
    
  for d in data:
    print('User:', d['fields']['username'])
    url = 'https://www.pytexas.org/api/v1/users/profile/{}?conf=2015&format=json'.format(d['fields']['username'])
    
    response = requests.get(url)
    
    with open('2015/api/v1/users/profile/' + d['fields']['username'], 'wb') as fh:
      fh.write(response.content)
      
    subprocess.call("ln -s ../index.html 2015/user/{}.html".format(d['fields']['username']), shell=True)
    
  with open('../talks.json', 'r') as fh:
    data = json.load(fh)
    
  for d in data:
    print('Talk:', d['fields']['id'])
    url = 'https://www.pytexas.org/api/v1/users/profile/{}?conf=2015&format=json'.format(d['fields']['username'])
    
    response = requests.get(url)
    
    with open('2015/api/v1/users/profile/' + d['fields']['username'], 'wb') as fh:
      fh.write(response.content)
      
    subprocess.call("ln -s ../index.html 2015/user/{}.html".format(d['fields']['username']), shell=True)
    
if __name__ == '__main__':
  run()
  
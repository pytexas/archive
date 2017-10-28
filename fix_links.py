#!/usr/bin/env python

import re
import sys

# find 2014 -name "*.html" -print0 | xargs -0 ./fix_links.py

def replace_external (mobj):
  url = mobj.group(1)
  if 'pytexas.org' in url:
    url = url.replace('http://archive.pytexas.org', '/2014')
    
  else:
    pass
    
  return '="{}"'.format(url)
  
def run (fps):
  for fp in fps:
    with open(fp, 'r') as fh:
      html = fh.read()
      
    # html = re.sub('[\./]+/static/', '/2014/static/', html)
    # html = re.sub('[\./]+/media/', '/2014/media/', html)
    # new_favi = '<link rel="shortcut icon" href="/favicon.ico">'
    # html = re.sub('<.*?shortcut icon.*?>', new_favi, html)
    
    html = re.sub('=".*?external\.html\?link=(.*?)"', replace_external, html)
    
    with open(fp, 'w') as fh:
      fh.write(html)
      
if __name__ == '__main__':
  run(sys.argv[1:])
  
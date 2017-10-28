#!/usr/bin/env python

import re
import sys

# find 2013 -name "*.html" -print0 | xargs -0 ./fix_links.py

def run (fps):
  for fp in fps:
    with open(fp, 'r') as fh:
      html = fh.read()
      
    html = re.sub('[\./]+/static/', '/2013/static/', html)
    html = re.sub('[\./]+/media/', '/2013/media/', html)
    
    with open(fp, 'w') as fh:
      fh.write(html)
      
if __name__ == '__main__':
  run(sys.argv[1:])
  
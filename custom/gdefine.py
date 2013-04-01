#!/usr/bin/env python
import sys
import pprint
from gdefine import gdefine

if len(sys.argv) < 2:
    sys.exit("""You must give a define request in format:\n"""
             """!define "Hello world!\"""")

pp = pprint.PrettyPrinter(indent=4)

meaning = gdefine.get_meaning(sys.argv[1])
output = ''
if not meaning:
    sys.exit("Not found! Try another word.")
if 'primaries' in meaning and meaning['primaries']:
    output = '---\n'
    for wordType,wordMeans in meaning['primaries'].iteritems():
        output += wordType + ": "
        for wordMean in wordMeans[0]:
          if wordMean is not None:
            output += wordMean + "\n"
    output += '---\n'
if 'webDefinitions' in meaning:
    for wordMean in meaning['webDefinitions'][0:5]:
        output += '\n  - ' + wordMean
    output += '---\n'
print output.encode('UTF-8')

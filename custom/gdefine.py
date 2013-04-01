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
    output += '---\n'
    output += 'Primaries: \n'
    ident = 0
    for wordType,wordMeans in meaning['primaries'].iteritems():
        ident = 1
        output += ('%s' % '  ' * ident) + wordType + ": "
        for wordMean_lv1 in wordMeans:
            ident = 2
            if wordMean_lv1[0]:
                output += '\n' + ('%s' % '  ' * ident) + wordMean_lv1[0]
            if wordMean_lv1[1]:
                ident = 3
                for example in wordMean_lv1[1][0:3]:
                    output += '\n . ' + ('%s' % '  ' * ident) + example
    output += '---\n'
if 'webDefinitions' in meaning:
    output += '\nWeb definitions:'
    for wordMean in meaning['webDefinitions'][0:5]:
        output += '\n  - ' + wordMean
    output += '---\n'
print output.encode('UTF-8')

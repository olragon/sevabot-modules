#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from translate import translate

if len(sys.argv) < 3:
    sys.exit("""You must give a translate request in format:\n"""
	     """!translate en_vi "Hello world!\"""")

args = sys.argv

lang_io = args[1]
lang_io = lang_io.split('_')

word = args[2]

result = translate.translate(word, lang_io[0], lang_io[1])
print(result["trans"].encode('UTF-8'))
#print(sys.argv[2])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import imap
import urllib2,urllib
import json

def _get_url(url):
    ua = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/17.0 Firefox/17.0"
    req = urllib2.Request(url)
    req.add_header("User-Agent",ua)

    try:
        r = urllib2.urlopen(req).read()
    except urllib2.URLError as e:
        print "URLError on url : %s => %s" % (e.url,e.reason,)
        sys.exit(0)

    return r

def translate(text,lin="fr",lout="en"):
    url = "http://translate.google.fr/translate_a/t?client=a&text=%s&hl=%s&sl=%s&tl=%s&ie=UTF-8&oe=UTF-8&multires=1&ssel=0&tsel=0&sc=1" % (urllib.quote(text),lin,lin,lout,)

    r = json.loads(_get_url(url))
    out = {"trans": ""}
    for sentence in r["sentences"]:
        out["trans"] += sentence["trans"]
    return out


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Translate text using google services")
    parser.add_argument("text",metavar="TEXT",help="Text to translate",nargs="*")
    parser.add_argument("-i","--input",metavar="LANGUAGE",default="fr",help="Input Language (default fr)")
    parser.add_argument("-o","--output",metavar="LANGUAGE",default="en",help="Output Language (default en)")
    args = parser.parse_args()

    t = translate(" ".join(args.text),args.input,args.output)
    if "trans" in t:
        print t["trans"].encode('UTF-8');
    else:
        print "no translation"
    if "other" in t:
        smax = len(max(imap(lambda x:x[0],t['other']),key=len))
        for o in t["other"]:
            print "%s => %s" % (o[0].ljust(smax," "),",".join(o[1]),)

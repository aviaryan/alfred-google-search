# -*- coding: utf-8 -*-

from __future__ import print_function

from sys import argv, stdout, version
import json
import os

# https://github.com/aviaryan/googlesearch
from gsearch.googlesearch import search


isPython2 = version.startswith('2')
isClipboard = False


def makeItem(query, url, name):
    item = {
        'uid': url,
        'title': name,
        'subtitle': url,
        'arg': url + ('$' if isClipboard else ''),
        'autocomplete': query,
        'icon': {
            'path': 'icon.png'
        }
    }
    return item


def makeReturn(items):
    out = {
        'items': items
    }
    return out


def main():
    global isClipboard
    arg_c = len(argv)
    if arg_c <= 1:
        return makeReturn([])
    query = argv[1]
    if not query:
        return makeReturn([])
    # clipboard queries
    if query.endswith('$'):
        query = query[:-1]
        isClipboard = True
        # load cache
        if os.path.isfile('cache.txt'):
            if isPython2:
                fp = open('cache.txt', 'r')
                data = fp.read().decode('utf-8', errors='ignore')
                query = query.decode('utf-8', errors='ignore')  # startswith wants this in unicode, since data in unicode
            else:
                fp = open('cache.txt', 'r', encoding='utf-8')
                data = fp.read()
            fp.close()
            if data.startswith(query + '\n'):
                obj = json.loads(data[len(query)+1:])
                for r in obj['items']:
                    if not r['arg'].endswith('$'):  # case: prev $ too
                        r['arg'] = r['arg'] + '$'
                out = json.dumps(obj, indent=4, encoding='utf-8')
                # weird bug
                out += '\n'
                return out
    results = search(query, num_results=10)
    items = []
    if len(results) == 0:
        items.append(makeItem(query, 'Please try again after 20 seconds', 'RATE LIMIT EXCEEDED'))
    for r in results:
        items.append(makeItem(query, r[1], r[0]))
    # return back
    out = makeReturn(items)
    out = json.dumps(out, indent=4, encoding='utf-8')
    # caching -- helps when $ inserted at last and you don't want to search again
    if isPython2:
        fp = open('cache.txt', 'w')
    else:
        fp = open('cache.txt', 'w', encoding='utf-8')
    fp.write(query + '\n' + out)
    fp.close()

    return out



if __name__ == '__main__':
    data = main()
    stdout.write(data)

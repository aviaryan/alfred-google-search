# -*- coding: utf-8 -*-

from __future__ import print_function

from sys import argv, stdout
import json

# https://github.com/aviaryan/googlesearch
from gsearch.googlesearch import search


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
    results = search(query, num_results=10)
    items = []
    if len(results) == 0:
        items.append(makeItem(query, 'Please try again after 20 seconds', 'RATE LIMIT EXCEEDED'))
    for r in results:
        items.append(makeItem(query, r[1], r[0]))
    return makeReturn(items)



if __name__ == '__main__':
    data = main()
    stdout.write(json.dumps(data, indent=4, encoding='utf-8'))

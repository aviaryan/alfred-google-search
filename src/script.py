# -*- coding: utf-8 -*-

from __future__ import print_function

from sys import argv, stdout
import json

# https://github.com/aviaryan/googlesearch
from gsearch.googlesearch import search


def makeItem(query, url, name):
    item = {
        'uid': url,
        'title': name,
        'subtitle': url,
        'arg': url,
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
    results = search(query, num_results=10)
    items = []
    if len(results) == 0:
        items.append(makeItem(query, 'Please try again after 20 seconds', 'RATE LIMIT EXCEEDED'))
    for r in results:
        items.append(makeItem(query, r[1], r[0]))
    # return back
    out = makeReturn(items)
    return json.dumps(out, indent=4, encoding='utf-8') + '\n' # WEIRD BUG


if __name__ == '__main__':
    data = main()
    stdout.write(data)

#!/usr/bin/env python

"""
Pandoc filter for converting Hungarian accented characters 
to Latin characters with flying accents
"""

from pandocfilters import toJSONFilter, Str

def mathaccents(key, value, format, meta):
  if key == 'Math':
    accents = {
      # small letters
      0xe1   : '\\acute{a}',
      0xe9   : '\\acute{e}',
      0xed   : '\\acute{\imath}',
      0xf3   : '\\acute{o}',
      0xf6   : '\\ddot{o}',
      0x0151 : '\\H{o}',
      0xfa   : '\\acute{u}',
      0xfc   : '\\ddot{u}',
      0x0171 : '\\H{u}',
      # capital letters
      0xc1   : '\\acute{A}',
      0xc9   : '\\acute{E}',
      0xcd   : '\\acute{I}',
      0xd3   : '\\acute{O}',
      0xd6   : '\\ddot{O}',
      0x0150 : '\\H{O}',
      0xda   : '\\acute{U}',
      0xdc   : '\\ddot{U}',
      0x0170 : '\\H{U}'
    }
    for charcode, mathstring in accents.iteritems():
      value[1] = value[1].replace(unichr(charcode), mathstring)

if __name__ == "__main__":
  toJSONFilter(mathaccents)

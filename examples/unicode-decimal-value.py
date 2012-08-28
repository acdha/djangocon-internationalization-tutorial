#!/usr/bin/env python
"""Unicode decimal value example: print everything numerically equal to 5"""
from __future__ import print_function, unicode_literals

from unicodedata import decimal, name
import sys

if sys.version_info[0] == 3:
    unichr = chr
    max_char = max(sys.maxunicode, 0x110000)
else:
    # Avoid breaking unichr on Python 2.x narrow builds
    # (see http://www.python.org/dev/peps/pep-0261/)
    max_char = sys.maxunicode

for i in range(0, max_char):
    u = unichr(i)
    if decimal(u, None) == 5:
        print('<span title="%s">&#x%x;</span>' % (name(u), i))

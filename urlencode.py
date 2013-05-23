#!/usr/bin/env python

import urllib
import sys

sys.argv.pop(0)
for (key, val) in zip(sys.argv[::2], sys.argv[1::2]):
    print urllib.urlencode({key:val})


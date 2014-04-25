#!/usr/bin/env python

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

def gen(length):
    return ''.join(random.choice(chars) for _ in xrange(length))

if __name__ == '__main__':
    import sys
    pwlength = 8
    if len(sys.argv) == 2:
        pwlength = int(sys.argv[1])
    print gen(pwlength)


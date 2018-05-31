#!/usr/bin/env python3

import sys

#print("Hello User", file=sys.stdout)
#print("Be careful user", file=sys.stderr)

numbers = [1, 5, 4, 'text', 'vari', 'egg']

for number in numbers:
    if type(number) == int:
        print("Thanks number received", file=sys.stdout)
    else:
        print("Please check input", file=sys.stderr)

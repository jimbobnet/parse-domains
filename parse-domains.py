#!/usr/bin/python3

import fileinput
from tld import get_fld

contents = fileinput.input()
for line in contents:
   domain = get_fld(line, fix_protocol=True, fail_silently=True)
   if domain: print(domain) #Strip null/invalid responses

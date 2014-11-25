from __future__ import print_function
from pylint import epylint as lint
import os
import sys

total_out = 0
total_err = 0
dirfiles = os.listdir(os.curdir)
for dirfile in dirfiles:
    if os.path.isfile(dirfile):
        if os.path.splitext(dirfile)[1] == '.py':
            print(dirfile)
            (stdout, stderr) = lint.py_run(dirfile, True)
            out = stdout.read()
            err = stderr.read()
            if len(out) > 0:
                print(out)
                total_out += 1
            if len(err) > 0:
                print(err)
                total_err += 1

if total_out > 0 or total_err > 0:
    sys.exit("pylint failed on some files")
else:
    sys.exit(0)
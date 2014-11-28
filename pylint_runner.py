"""
Runs pylint on all contained python files in this directory
"""
# pylint: disable=invalid-name

from __future__ import print_function
import os
from pylint.lint import Run

files = []
dirfiles = os.listdir(os.curdir)
for dirfile in dirfiles:
    if os.path.isfile(dirfile):
        if os.path.splitext(dirfile)[1] == '.py':
            files.append(dirfile)

Run(["--output-format=colorized", "-rno"]+files)

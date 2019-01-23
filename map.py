#!/usr/bin/env python2.7

import sys

# input comes from STDIN (standard input)
for each in sys.stdin:
    # remove leading and trailing whitespace
    lines = str(each).split('\n')
    for line in lines:
        line = line.strip()
        # split the line into words
        degree = line.split('\t')
        # increase counters
        print '%s\t%s\t%s' % (degree[0], 'in',1)
        print '%s\t%s\t%s' % (degree[1], 'out',1)

    # for degree in degrees:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        # print '%s\t%s' % (degree, 1)

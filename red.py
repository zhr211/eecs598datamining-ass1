
#!/usr/bin/env python2.7

from operator import itemgetter
import sys

current_node = None
count_in = 0
count_out = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    node, type, count = line.split('\t',1)
        # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if type=='in' and current_node == node:
        count_in +=count
    elif type=='out' and current_node == node:
        count_out +=count
    else:
        if current_node:
            total = count_in+count_out
            print '%s,%s,%s,%s' % (current_node,count_in,count_out,total)
        if types == 'in':
            count_in = count
            count_out = 0
            current_node = node
            # print '%s,%s,%s,%s' % (current_node,count_in,count_out,count_in+count_out)
        else:
            count_out = count
            count_in = 0
            current_node = node
            # print '%s,%s,%s,%s' % (current_node,count_in,count_out,count_in+count_out)

if current_node == node:
    print '%s,%s,%s,%s' % (current_node, count_in,count_out,count_in+count_out)

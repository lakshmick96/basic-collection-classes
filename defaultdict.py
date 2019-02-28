from collections import *

s = [('apple', 5), ('orange', 2), ('apple', 3), ('berry', 4), ('pear', 6)] 
d = defaultdict(list)

for k, v in s:
    d[k].append(v)
print d



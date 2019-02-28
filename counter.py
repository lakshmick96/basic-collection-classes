# Program to get most common n elements of a list.

from collections import *
def most_common(l, n):
    return Counter(l).most_common(n) 


z = ['a', 'd', 's', 'a', 'd', 'f', 's', 'd', 'g','s','d']
print most_common(z, 3)

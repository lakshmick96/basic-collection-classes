from collections import deque

d = deque()

d.append(1)
print d

d.appendleft(2)
print d

d.clear()
print d

d.extend('1')
print d

d.extendleft('25')
print d

print d.count('1')

d.pop()
print d



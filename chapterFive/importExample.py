import math as foobar
print foobar.sqrt(4)

from math import sqrt as foobar
print foobar(4)

# nice formate of python 
x,y,z = 3,4,10
print y,z,x
x,y = y,x
print x,y,z
# more explicit
print "more interesting "
values = 1,2,3
print values
x,y,z = values
print y
scundrel = {'name':'Emon','boyFriend':'sobuj'}
key,value=scundrel.popitem()
print 'popitem using by ',key
print 'value is ',value
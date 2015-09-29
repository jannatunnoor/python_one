x=1
while x<=10:
    print x
    x+=1


for x in range(1,50,2):
    print x

d= {'x':1,'y':2,'z':3}
for key in d:
    print key,'corresponding to',d[key]
print 'length of dictionary is ', len(d)

for key,value in d.items():
     print key,'corresponding to',value

print '**** sorted dictionary ****',sorted(d)

strings = ['avijoy','chaity','sujon','arun','jannat']

for index, string in enumerate(strings):
    if 'jo' in string:
        strings[index] = '[censored]'
    print strings[index]
print strings

from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    print 'root is',root
    if root == int(root):
        print n
        break

for x in range(10):
    if x % 3 == 0:
        print x*x

print [(x, y) for x in range(3) for y in range(3)]
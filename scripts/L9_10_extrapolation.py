import math
#a = [1950, 1955, 1960, 1965, 1970]
#b = [304, 329, 357, 387, 421]
a = [0.10, 0.15, 0.20, 0.25, 0.30]
b = [0.1003, 0.1511, 0.2027, 0.2553, 0.3093]

a = [0, 1, 2, 3]
b = [1, 0, 1, 10]

'''n = int(input("Enter n: ")) 
for i in range(n):
  x = float(input("Enter value of 1st row: "))
  a.append(x)
for i in range(n):
  tanx = float(input("Enter value of 2nd row: "))
  b.append(tanx)
'''
'''for i in a:
  print(i)'''
#y = float(input("Enter the value for that you want to find: "))
y = 4

y0 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []

yall = [b, y0, y1, y2, y3, y4, y5, y6, y7, y8, y9]

alen = len(a)


def cal(child, yl):
    m = 0
    l = len(child)
    for i in range(l-1):
        m = child[i+1]-child[i]
        yl.append(m)


for i in range(alen-1):
    cal(yall[i], yall[i+1])


for i in range(1, alen):
    print('------', i, 'y0------')
    for j in yall[i]:
        print(round(j, 5))
    print('\n')


h = a[1]-a[0]
u = (y - a[0])/h
print('\n\n')
print(round(u, 4))


fact = u


ulist = []
flist = []
ylist = []

for i in range(1, alen):
    for j in yall[i]:
        ylist.append(j)
        break


ulist.append(u)
for i in range(1, alen-1):
    fact = fact*(u-i)
    ulist.append(fact)

for i in range(1, alen):
    flist.append(math.factorial(i))

result = b[0]
for i in range(alen-1):
    result = result + (ulist[i]/flist[i])*ylist[i]

print('Result: ', round(result, 4))

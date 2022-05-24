import math

eq = '1*'+str(input("Enter equation: "))
a = float(input("Enter lower value: "))
b = float(input("Enter upper value: "))
n = int(input("Enter step(n): "))
h0 = input("Enter value of h if any: ")

def math_l12(eq,a,b,n,h0):
  if h0=='':
    h = (b-a)/n
  else:
    h = float(h0)

  x1 = []
  y1 = []

  x0 = a
  x1.append(x0)
  for i in range(1, n+1):
      m = x0 + i*h
      x1.append(m)

  eq = eq.replace(' ', '')
  if eq.find('^'):
      eq = eq.replace('^', '**')
  if eq.find('sqrt'):
      eq = eq.replace('sqrt', 'math.sqrt')
  if eq.find('log'):
      eq = eq.replace('log', 'math.log')
  if eq.find('ln'):
      eq = eq.replace('ln', 'math.log')
  if eq.find('sin'):
      eq = eq.replace('sin', 'math.sin')
  if eq.find('cos'):
      eq = eq.replace('cos', 'math.cos')
  if eq.find('e'):
      eq = eq.replace('e', 'math.e')


  for i in range(len(x1)):
      x = x1[i]
      solv = eval(eq)
      y1.append(solv)

  xlen =len(x1)
  ylen =len(y1)

  print('\n------x------')
  for i in range(xlen):
    print('x'+str(i),round(x1[i],5))
    
  print('\n------y------')
  for i in range(ylen):
    print('y'+str(i),round(y1[i],5))

  s = 0

  for i in range(1,ylen-1):
    s = s+y1[i]

  result = (h/2)*((y1[0]+y1[ylen-1])+2*s)
  print(round(result,4))

math_l12(eq,a,b,n,h0)
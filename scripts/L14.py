import math


def math_l14(eq, a, b, n, h0):
    if h0 == '':
        h = (b-a)/n
    else:
        h = float(h0)

    print('\nh = (b - a)/n')
    print('  =', round(h, 4))

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

    xlen = len(x1)
    ylen = len(y1)

    print('\n------x------')
    for i in range(xlen):
        print('x'+str(i), round(x1[i], 5))

    print('\n------y------')
    for i in range(ylen):
        print('y'+str(i), round(y1[i], 5))

    # Weddle’s Rule-------------
    s1 = 0
    s2 = ''
    count = 0
    for i in range(0, ylen):
        if count == 6:
            count = 0
            s1 = s1+2*y1[i]
            s2 = s2 + '2y' + str(i)
        elif count == 3:
            s1 = s1+6*y1[i]
            s2 = s2 + '6y' + str(i)
        elif count == 5:
            s1 = s1+5*y1[i]
            s2 = s2 + '5y' + str(i)
        elif count == 1:
            s1 = s1+5*y1[i]
            s2 = s2 + '5y' + str(i)
        else:
            s1 = s1+y1[i]
            s2 = s2 + 'y' + str(i)
        if i != ylen-1:
            s2 = s2 + ' + '
        count = count+1

    result = ((3*h)/10)*s1
    print('\nResult = ((3*h)/10)*', s2)
    print('       = ', round(result, 4))


h0 = ''
eq = '1*sqrt(x)'
a = 1
b = 1.3
n = 6

math_l14(eq, a, b, n, h0)

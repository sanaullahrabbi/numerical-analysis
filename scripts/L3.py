import PySimpleGUI as sg
import sympy as sym
def l3_math(eq1, dec, nx , dif):
    print("\t\t\t     ----------Roots of equations (Newton raphson method)----------")
    dec = int(dec)
    eq1 = eq1.replace(' ', '')

    print('f(x) = ', eq1)
    #x=''
    eq2 = sym.diff(eq1,'x')
    if eq1.find('^'):
        eq1 = eq1.replace('^', '**')
    print('f`(x) = ', eq2, '\n')

    l1 = []
    l2 = []
    for i in range(11):
        x = i
        solv = eval(eq1)
        if solv > 0:
            l1.append(i)

        elif solv < 0:
            b = i
            l2.append(i)
    if not l1:
        for i in range(-1,-11,-1):
            x = i
            solv = eval(eq1)
            if solv >= 0:
                l1.append(i)

    if not l2:
        for i in range(-1,-11,-1):
            x = i
            solv = eval(eq1)
            if solv < 0:
                l2.append(i)

    if l1[0] > l2[0]:
        x = l1[0]
        print('f('+str(l1[0])+') = ', eval(eq1), ' >0, Positive', l1[0])
        pos = l1[0]

        l = min(l2, key=lambda x: abs(x-l1[0]))
        neg = l
        x0 = l
        x = l
        print('f('+str(l)+') = ', eval(eq1), ' <0, Negetive', l)
    else:
        x = l2[0]
        print('f('+str(l2[0])+') = ', eval(eq1), ' <0 Negetive', l2[0])
        neg = l2[0]
        l = min(l1, key=lambda x: abs(x-l2[0]))
        pos = l
        x0 = l
        x = l
        print('f('+str(l)+') = ', eval(eq1), ' >0 Positive', l)

    if nx == '':
        print('')
    elif nx!='' and dif=='':
        x0 = float(nx)-0
    else:
        x0 = float(nx)-float(dif)
    x0 = 0
    print('\nTaking x0 = ', x0, '\n')

    z = 0
    m = ''
    n = ''
    while(True):
        x = x0
        m = str(x)
        fx = eval(eq1)
        fp = eval(str(eq2))
        x1 = x - (fx/fp)
        n = str(x1)
        print('for n =', z, '   x'+str(z+1), "= ", 'x'+str(z),
              '-', 'f(' + 'x'+str(z) + ')/ f`('+'x'+str(z)+')')
        print("\t\t= ", round(x, 5), '- (', round(fx, 5), '/', round(fp, 5), ')')
        print('\t\t= ', round(x1, 5))
        print('\n')
        x0 = x1
        if(m[0:2+dec] == n[0:2+dec]):
            print('Required root is: ', m[0:2+dec])
            break
        if z==100:
            print('Required root is: ', m[0:2+dec])
            break
        z = z+1

    eq1 = ''
    dec = 0
    x0 = 0
    pos = 0
    neg = 0

eq1 = 'x^3-6*x+4'
dec = 5
x0 = 0
pos = 0
neg = 0
l3_math(eq1,dec,'','')
print("---------- Roots of equations (Bisection method)----------")

eq = input("Enter your equation: ")
dec = int(input("Correct up to: "))

eq = eq.replace(' ', '')
if eq.find('^'):
    eq = eq.replace('^', '**')

print('f(x) = ', eq, '\n')

l1 = []
l2 = []
for i in range(11):
    x = i
    solv = eval(eq)
    if solv > 0:
        l1.append(i)

    elif solv < 0:
        b = i
        l2.append(i)

if l1[0] > l2[0]:
    x = l1[0]
    print('f('+str(l1[0])+') = ', eval(eq), ' >0, Positive')
    pos = l1[0]
    l = min(l2, key=lambda x: abs(x-l1[0]))
    neg = l
    x = l
    print('f('+str(l)+') = ', eval(eq), ' <0, Negetive')
else:
    x = l2[0]
    print('f('+str(l2[0])+') = ', eval(eq), ' <0 Negetive')
    neg = l2[0]
    l = min(l1, key=lambda x: abs(x-l2[0]))
    pos = l
    x = l
    print('f('+str(l)+') = ', eval(eq), ' >0 Positive')

print('\n')
b = 1
m = str(pos)
n = str(neg)
while(True):
    itr = (pos+neg)/2
    x = round(itr,2)
    a = eval(eq)
    if a > 0:
        print('Iteration ', b, ": let, x"+str(b-1) +
              ' = (', round(pos, 4), '+', round(neg, 4), ')/2')
        print('\t\t\t= ', round(itr, 4))
        print('\t\tf(x'+str(b-1)+') = ', round(a, 4), ">0")
        pos = itr
        m = str(itr)
    elif a < 0:
        print('Iteration ', b, ": let, x"+str(b-1) +
              ' = (', round(pos, 4), '+', round(neg, 4), ')/2')
        print('\t\t\t= ', round(itr, 4))
        print('\t\tf(x'+str(b-1)+') = ', round(a, 4), "<0")
        neg = itr
        n = str(itr)
    print('\tThe required Root lies between: ',
          m[0:4+dec], " and ", n[0:4+dec], '\n')
    if(m[0:2+dec] == n[0:2+dec] and a >= 0):
        print('Result is: ', m[0:2+dec])
        break
    b = b+1

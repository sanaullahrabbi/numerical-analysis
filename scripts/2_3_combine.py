import PySimpleGUI as sg
import re

def diff(eq1):
    ref = re.split(r'(\D)', eq1)
    res = []
    eq = ''

    for i in range(len(ref)):
        if ref[i] == '':
            continue
        res.append(ref[i])

    for i in range(len(res)):
        if res[i] == '^':
            xn = int(res[i+1])
            eq = eq + str(xn)+'*'+res[i-1]+'^'+str(xn-1)

        elif res[i] in '+-':
            eq = eq+res[i]

        elif res[i] == '*':
            eq = eq + res[i-1] + res[i]
        
        elif res[i] == 'x' and (res[i-1] in '+-' and res[i+1] in '+-'):
            eq = eq + '1'

    for i in range(len(eq)-1, -1, -1):
        if eq[i] in '+-*/':
            eq = eq[:i]
        elif eq[i].isalnum:
            break

    if eq.find('^'):
        eq = eq.replace('^', '**')
    return eq

def l2_math(eq,dec):
    print("\t\t\t\t----------Roots of equations (Bisection method)----------")
    dec = int(dec)
    eq = eq.replace(' ', '')
    print('f(x) = ', eq, '\n')
    if eq.find('^'):
        eq = eq.replace('^', '**')

    l1 = []
    l2 = []
    for i in range(101):
        x = i
        solv = eval(eq)
        if solv > 0:
            l1.append(i)

        elif solv < 0:
            b = i
            l2.append(i)
    if not l1:
        for i in range(-1,-101,-1):
            x = i
            solv = eval(eq)
            if solv >= 0:
                l1.append(i)

    if not l2:
        for i in range(-1,-101,-1):
            x = i
            solv = eval(eq)
            if solv < 0:
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
        x = itr
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
        if(m[0:2+dec] == n[0:2+dec] and a > 0):
            print('Result is: ', m[0:2+dec])
            break
        if b==100:
            print('Result is: ', m[0:2+dec])
            break
        b = b+1


def l3_math(eq1, dec, nx , dif):
    print("\t\t\t     ----------Roots of equations (Newton raphson method)----------")
    dec = int(dec)
    eq1 = eq1.replace(' ', '')

    print('f(x) = ', eq1)
    eq2 = diff(eq1)
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
        print("\t\t= ", round(x, 4), '- (', round(fx, 4), '/', round(fp, 4), ')')
        print('\t\t= ', round(x1, 4))
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


sg.theme('DarkGrey2')
def ChatBot():
    layout = [[sg.Text('Enter Equation', size=(21, 1)),sg.InputText(key='-eq-', size=(78, 1))],
              [sg.Text('Correct up to', size=(21, 1)),
               sg.InputText(key='-dec-', size=(40, 1)),sg.T('\t  '),sg.Radio("Bisection Method", group_id='choice1',default=True, key='c1')],
              [sg.Text('Near to x if given', size=(21, 1)),
               sg.InputText(key='-near_to-', size=(40, 1)),sg.T('\t  '),sg.Radio("Newton Raphson Method", group_id='choice1', key='c2')],
              [sg.Text('Difference of Near to x if given', size=(21, 1)),
               sg.InputText(key='-df-', size=(40, 1)),sg.T('\t   ') ,sg.Button('Find Root'), sg.Button('Clear')],
              [sg.Output(size=(100, 25), key=('-Output-'))]]

    window = sg.Window('Roots of equations',
                       layout, default_element_size=(45, 2), size=(750, 500))

    while True:
        event, value = window.read()
        try:
            if event == sg.WIN_CLOSED:
                break

            if (value['-eq-'] == '' or value['-dec-'] == '') and event != 'Clear':
                print('Please enter all data correctly !!!')

            elif event == 'Find Root' and (value['-eq-'] != '' or value['-dec-'] != '') and value['c1']:
                window['-Output-'].update('')
                l2_math(value['-eq-'], value['-dec-'])

            elif event == 'Find Root' and (value['-eq-'] != '' or value['-dec-'] != '') and value['c2']:
                window['-Output-'].update('')
                l3_math(value['-eq-'], value['-dec-'], value['-near_to-'], value['-df-'])

            elif event == 'Clear':
                window['-eq-'].update('')
                window['-dec-'].update('')
                window['-near_to-'].update('')
                window['-df-'].update('')
                window['-Output-'].update('')
        except:
            print("An exception occurred")

    window.close()


ChatBot()
#4*x^3-8*x^2-3*x+9
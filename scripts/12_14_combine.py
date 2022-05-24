import PySimpleGUI as sg
import math

y1 = []
h = 0

def pi_ch(pic):
  pic = '1*'+pic
  if pic.find('pi'):
    pic = pic.replace('pi', 'math.pi')
    return eval(pic)
  else:
    return eval(pic)
def math_l12_14(eq, a, b, n, h0):
    global h
    if h0 == '':
        h = (b-a)/n
        print('h = (b - a)/n')
        print('  =', round(h, 4))
    else:
        h = float(h0)
        print('Given h = ', h)

    x1 = []
    global y1

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


def rule1():
    ylen = len(y1)
    s = 0
    s2 = ''

    for i in range(1, ylen-1):
        s = s+y1[i]
        s2 = s2 + 'y' + str(i)
        if i != ylen-2:
            s2 = s2 + ' + '

    result = (h/2)*((y1[0]+y1[ylen-1])+2*s)
    print('\nResult = (h/2)*[( y0 + y'+str(ylen-1)+' ) + 2(', s2, ')]')
    print('       = ', round(result, 4))
    y1.clear()


def rule2():
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    sq1 = ''
    sq2 = ''
    sq3 = ''
    sq4 = ''
    ylen = len(y1)

    # simpson's 1/3 rule-------------
    for i in range(1, ylen-1):
        if i % 2 == 0:
            s2 = s2+y1[i]
            sq2 = sq2 + 'y' + str(i) + ' + '
            continue
        s1 = s1+y1[i]
        sq1 = sq1 + 'y' + str(i) + ' + '

    result = (h/3)*((y1[0]+y1[ylen-1])+4*s1+2*s2)
    sq1 = sq1[:-3]
    sq2 = sq2[:-3]
    print('\n----1/3 Rule----')
    print('Result = (h/3)*[( y0 + y'+str(ylen-1) +
          ' ) + 4(', sq1, ') + 2(', sq2, ')]')
    print('       = ', round(result, 4))

    # simpson's 3/8 rule-------------
    count = 0
    for i in range(1, ylen-1):
        if count == 2:
            count = 0
            s4 = s4+y1[i]
            sq4 = sq4 + 'y' + str(i) + ' + '
            continue
        s3 = s3+y1[i]
        count = count+1
        sq3 = sq3 + 'y' + str(i) + ' + '

    result = ((3*h)/8)*((y1[0]+y1[ylen-1])+3*s3+2*s4)
    sq3 = sq3[:-3]
    sq4 = sq4[:-3]

    print('\n----3/8 Rule----')
    print('Result = (3*h)/8)*[( y0 + y'+str(ylen-1) +
          ' ) + 3(', sq3, ') + 2(', sq4, ')]')
    print('       = ', round(result, 4))

    y1.clear()


def rule3():
    # Weddle’s Rule-------------
    s1 = 0
    s2 = ''
    ylen = len(y1)
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
    y1.clear()


sg.theme('DarkGrey2')

def lol():
    layout = [[sg.Text('Enter Equation', size=(20, 1)), sg.InputText(key='-eq-', size=(77, 1))],
              [sg.Text('Enter lower value', size=(20, 1)),
               sg.InputText(key='-a-', size=(25, 1)), sg.T('\t\t'), sg.Radio("Trapezoidal Rule", group_id='choice1',
                                                                             default=True, key='c1')],

              [sg.Text('Enter upper value', size=(20, 1)),
               sg.InputText(key='-b-', size=(25, 1)), sg.T('\t\t'), sg.Radio("Simpson’s 1/3 and 3/8 Rules", group_id='choice1', key='c2')],

              [sg.Text('Enter step(n)', size=(20, 1)),
               sg.InputText(key='-n-', size=(25, 1)), sg.T('\t\t'), sg.Radio("Weddle’s Rule", group_id='choice1', key='c3')],

              [sg.Text('Enter value of h if any', size=(20, 1)),
               sg.InputText(key='-h0-', size=(25, 1)), sg.T('\t\t '), sg.Button('Find'), sg.Button('Clear All')],
              [sg.Output(size=(100, 25), key=('-Output-'))]]

    window = sg.Window('Numerical Integration',
                       layout, default_element_size=(45, 2), size=(750, 500))

    while True:
        event, value = window.read()
        try:
            if event == sg.WIN_CLOSED:
                break

            if (value['-eq-'] == '' or value['-a-'] == '' or value['-b-'] == '' or value['-n-'] == '') and event != 'Clear All':
                print('Please enter all data correctly !!!')

            elif event == 'Find' and (value['-eq-'] != '' or value['-a-'] != '' or value['-b-'] != '' or value['-n-'] != '') and value['c1']:
                window['-Output-'].update('')
                eq = '1*'+value['-eq-']
                a = pi_ch(value['-a-'])
                b = pi_ch(value['-b-'])
                n = int(value['-n-'])
                h0 = value['-h0-']

                print('\n\t\t\t\t\t    ----Trapezoidal Rule----')
                math_l12_14(eq, a, b, n, h0)
                rule1()
            elif event == 'Find' and (value['-eq-'] != '' or value['-a-'] != '' or value['-b-'] != '' or value['-n-'] != '') and value['c2']:
                window['-Output-'].update('')
                eq = '1*'+value['-eq-']
                a = pi_ch(value['-a-'])
                b = pi_ch(value['-b-'])
                n = int(value['-n-'])
                h0 = value['-h0-']

                print('\n\t\t\t\t\t    ----Simpson’s 1/3 and 3/8 Rules----')
                math_l12_14(eq, a, b, n, h0)
                rule2()

            elif event == 'Find' and (value['-eq-'] != '' or value['-a-'] != '' or value['-b-'] != '' or value['-n-'] != '') and value['c3']:
                window['-Output-'].update('')
                eq = '1*'+value['-eq-']
                a = pi_ch(value['-a-'])
                b = pi_ch(value['-b-'])
                n = int(value['-n-'])
                h0 = value['-h0-']

                print('\n\t\t\t\t\t    ----Weddle’s Rule----')
                math_l12_14(eq, a, b, n, h0)
                rule3()

            elif event == 'Clear All':
                window['-eq-'].update('')
                window['-a-'].update('')
                window['-b-'].update('')
                window['-n-'].update('')
                window['-h0-'].update('')
                window['c1'].update(value=True)
                window['-Output-'].update('')
        except:
            print("An exception occurred")

    window.close()


lol()

import math
import PySimpleGUI as sg
import re

sg.theme('DarkGrey2')


def math_l8(a, b, y):
    print('\n\t*****Newton-Gregory Formula for forward and backward interpolation/Extrapolation with equal interval*****')

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

    print('\n')
    for i in range(1, alen):
        print('------', i, 'y0------')
        for j in yall[i]:
            print(round(j, 5), )

    # u calculate------------------------------------------------
    forward_check = abs(y - a[0])
    backward_check = abs(y - a[alen-1])
    f_b = (forward_check < backward_check) or (y> a[alen-1])
    h = a[1]-a[0]
    uprint = ''
    if f_b:
        u = (y - a[0])/h
        uprint = 'u = (x - x0)/h\n'+'  = (' + str(y) + '-' + \
            str(a[0]) + ')/' + str(h) + '\n  = '+str(round(u, 4))
        if y>a[alen-1] or y<a[0]:
            print('\n\t\t\t\t\t       Extrapolation')
        else:
            print('\n\t\t\t\t\t       Interpolation')
        print('\n\t\t\t\t\t-----Forward formula-----')

    else:
        u = (y - a[alen-1])/h
        uprint = 'u = (x - xn)/h\n'+'  = (' + str(y) + '-' + \
            str(a[alen-1]) + ')/' + str(h) + '\n  = '+str(round(u, 4))
        print('\n\t\t\t\t\t       Interpolation')
        print('\n\t\t\t\t\t-----Backward formula-----')

    # result data calculate---------------------------------------------
    fact = u
    ulist = []
    flist = []
    ylist = []
    rule = 'u'

    if f_b:
        for i in range(1, alen):
            for j in yall[i]:
                ylist.append(j)
                break

        result = b[0]

        f = 'y(x)  = y0 + u*1y0'
        for i in range(1, alen-1):
            rule = rule+'(u-'+str(i)+')'
            f = f+' + ('+rule+'/'+str(i+1)+'!)*'+str(i+1)+'y0'
    else:
        for i in range(1, alen):
            l = yall[i]
            for j in range(len(yall[i])-1, -1, -1):
                ylist.append(l[j])
                break

        result = b[alen-1]

        f = 'y(x)  = yn + u*1yn'
        for i in range(1, alen-1):
            rule = rule+'(u+'+str(i)+')'
            f = f+' + ('+rule+'/'+str(i+1)+'!)*'+str(i+1)+'yn'

    ulist.append(u)
    if f_b:
        for i in range(1, alen-1):
            fact = fact*(u-i)
            ulist.append(fact)
    else:
        for i in range(1, alen-1):
            fact = fact*(u+i)
            ulist.append(fact)

    for i in range(1, alen):
        flist.append(math.factorial(i))

    #  result calculate-------------------------------------------------------
    rl = str(result)
    for i in range(alen-1):
        result = result + (ulist[i]/flist[i])*ylist[i]
        rl = rl+' + '+'('+str(round(ulist[i], 5)) + \
            '/'+str(flist[i])+')*'+str(round(ylist[i], 5))

    print('calculate u')
    print('----------------')
    print(uprint)
    print('\nCalculate Result')
    print('-----------------------')
    print(f)
    print('y('+str(y)+') =', rl)
    print('      =', round(result, 4), ' (Ans.)')


def ChatBot():
    layout = [[sg.Text('Enter 1st row data', size=(30, 1)), sg.InputText(key='-r1-', size=(66, 1))],
              [sg.Text('Enter 2nd row data', size=(30, 1)),
               sg.InputText(key='-r2-', size=(66, 1))],
              [sg.Text('Enter the value for that you want to find', size=(30, 1)), sg.InputText(
                  key='-r3-', size=(51, 1)), sg.Button('Find'), sg.Button('Clear all', pad=(3, 0),size=(7,1))],
              [sg.Output(size=(100, 25), key=('-Output-'))],
              ]

    window = sg.Window('Newton-Gregory Formula(Forward/Backward)',
                       layout, default_element_size=(30, 2), size=(750, 500))

    while True:
        event, value = window.read()
        try:
            if event == sg.WIN_CLOSED:
                break
            if (value['-r1-'] == '' or value['-r2-'] == '' or value['-r3-'] == '') and event != 'Clear all':
                print('Please enter all data correctly !!!')

            elif event == 'Find' and (value['-r1-'] != '' or value['-r2-'] != '' or value['-r3-'] != ''):
                window['-Output-'].update('')
                a = [x for x in re.compile('\s*[,|\s+]\s*').split(value['-r1-'])]
                a = [float(i) for i in a]

                b = [x for x in re.compile('\s*[,|\s+]\s*').split(value['-r2-'])]
                b = [float(i) for i in b]

                yi = float(value['-r3-'])

                math_l8(a, b, yi)

            elif event == 'Clear all':
                window['-r1-'].update('')
                window['-r2-'].update('')
                window['-r3-'].update('')
                window['-Output-'].update('')
        except:
            print("An exception occurred")

    window.close()


ChatBot()
#1950,1955,1960,1965,1970
#304,329,357,387,421
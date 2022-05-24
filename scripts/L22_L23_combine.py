import PySimpleGUI as sg
import re
def euler(eq, yx, h, xn): 
    yx = yx.replace(' ','')
    res = re.findall(r'\(.*?\)', yx)

    x0 = str(res[0]).replace('(','').replace(')','')
    x0 = float(x0)
    y = float(yx.split("=")[1])
    h = float(h)
    xn = float(xn)
    temp = 0
    i=0
    print('\nf(x,y) = ',eq)
    print('x0 = ',x0)
    print('y0 = ',y)
    print('Also, given that step of size h = ',h,'\n')

    while x0 <xn:
      x = x0
      yp = y
      y = y + (h * eval(eq))
      x0 = x0 + h
      print('The x-iteration formula, with n = ',i,'gives us:')
      print('x'+str(i+1),' = ','x',i,'+','h')
      print('    =',round(x,5),'+',h)
      print('    =',round(x0,5))

      print('And the y-iteration formula, with n = ',i,'gives us:')
      eqp = eq.replace('x','x'+str(i))
      eqp = eqp.replace('y','y'+str(i))
      print('y'+str(i+1),' = y',i,'+','h(',eqp,')')
      print('    = ',round(yp,5),'+',h,'(',round(x,5),'+',round(yp,5),')')
      print('    = ',round(y,5))

      print('\n')
      i=i+1
    
    print("Approximate solution of y at x = ", xn, " is ", "%.5f"% y) 


def eq_cal(x,y,eq):
    return eval(eq)
def rungeKutta(eq, yx, h, xn): 
    yx = yx.replace(' ','')
    res = re.findall(r'\(.*?\)', yx)

    x0 = str(res[0]).replace('(','').replace(')','')
    x0 = float(x0)
    y = float(yx.split("=")[1])
    h = float(h)
    xn = float(xn)
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((xn - x0)/h)  
    # Iterate for number of iterations 
    for i in range(1, n + 1): 
        k1 = h * eq_cal(x0,y,eq) 
        print('K1 = ',k1)
        k2 = h * eq_cal((x0+ h/2), (y + k1/2),eq)
        print('K2 = ',k2)
        k3 = h * eq_cal((x0+ h/2), (y + k2/2),eq)
        print('K3 = ',k3)
        k4 = h * eq_cal((x0 + h),(y + k3),eq) 
        print('K4 = ',k4)

        print('\n')
        # Update next value of y 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        # Update next value of x 
        x0 = x0 + h
 
    print ('The value of y at x is:', y )

sg.theme('DarkGrey2')
def main():
    layout = [[sg.Text('Enter Equation', size=(21, 1)),sg.InputText(key='-eq-', size=(78, 1))],
              [sg.Text('Enter y as y(x) = value', size=(21, 1)),
               sg.InputText(key='-yx-', size=(40, 1)),sg.T('\t  '),sg.Radio("Eular Method", group_id='choice1',default=True, key='c1')],
              [sg.Text('Enter the value of h', size=(21, 1)),
               sg.InputText(key='-step-', size=(40, 1)),sg.T('\t  '),sg.Radio("Runge Kutta Method", group_id='choice1', key='c2')],
              [sg.Text('Find at the Point', size=(21, 1)),
               sg.InputText(key='-fa-', size=(40, 1)),sg.T('\t   ') ,sg.Button('Find Root'), sg.Button('Clear')],
              [sg.Output(size=(100, 25), key=('-Output-'))]]

    window = sg.Window('Roots of equations',
                       layout, default_element_size=(45, 2), size=(750, 500))

    while True:
        event, value = window.read()
        try:
            if event == sg.WIN_CLOSED:
                break

            if (value['-eq-'] == '' or value['-yx-'] == '') and event != 'Clear':
                print('Please enter all data correctly !!!')

            elif event == 'Find Root' and (value['-eq-'] != '' or value['-yx-'] != '') and value['c1']:
                window['-Output-'].update('')
                euler(value['-eq-'], value['-yx-'], value['-step-'], value['-fa-'])

            elif event == 'Clear':
                window['-eq-'].update('')
                window['-yx-'].update('')
                window['-step-'].update('')
                window['-fa-'].update('')
                window['-Output-'].update('')
            elif event == 'Find Root' and (value['-eq-'] != '' or value['-yx-'] != '') and value['c2']:
                window['-Output-'].update('')
                rungeKutta(value['-eq-'], value['-yx-'], value['-step-'], value['-fa-'])
        except:
            print("An exception occurred")

    window.close()


main()
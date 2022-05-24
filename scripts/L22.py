def euler( x0, y, h, xn ,eq): 

    temp = 0
    i=0
    print('\nf(x,y) = ',eq)
    print('x0 = ',x0)
    print('y0 = ',y)
    print('Also, given that step of size ℎ = ',h,'\n')

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
    
    print("Approximate solution at x = ", xn, " is ", "%.5f"% y) 
      
x0 = 0
y0 = 1
h = 0.1

xn = 0.25
eq='1+x*y'

euler(x0, y0, h, xn,eq)
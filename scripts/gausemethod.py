import numpy as np
'''def arr_input():
    elements =np.array(input("elements:").split())
    return elements

matrix =np.array([arr_input(), arr_input()])
int_array = matrix.astype(float)
'''

matrix =np.array([[1,1,1,9],[2,1,-1,0],[2,5,7,52],[0,0,0,0]])
print(matrix)
def zer_po(num1,num2):
    return num2-(num2/num1)
a11 = matrix[0,0]
for i in range(3):
    for j in range(2):
        
        aij = matrix[i+1,j]-(matrix[i,j]*matrix[i+1,j])

        matrix[i+1,j] = aij
        
print(matrix)

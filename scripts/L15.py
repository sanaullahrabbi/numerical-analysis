import numpy as np
'''def arr_input():
    elements =np.array(input("elements:").split())
    return elements

matrix =np.array([arr_input(), arr_input()])
int_array = matrix.astype(float)
'''
#matrix =np.array([[1,1,1,9],[2,1,-1,0],[2,5,7,52]])
#matrix0 =np.array([['1','1','1','9'],['2','1','-1','0'],['2','5','7','52']])
#matrix =np.array([[1,1,1,3],[1,2,2,4],[1,4,9,6]])
#matrix =np.array([[1,3,10,24],[2,17,4,35],[28,4,-1,32]])
#matrix =np.array([[10,1,1,12],[1,10,1,12],[1,1,10,12]])
#matrix =np.array([[1,2,3,-4],[2,4,5,-7],[3,5,6,-10]])
matrix =np.array([[1,1,1,3],[1,2,3,6],[2,3,5,10]])
print(matrix)

matrix = matrix.astype(float)
matrix[0]=(matrix[0]/matrix[0][0]).round(4)

for i in range(1,3):
    a21 = matrix[i,0]
    for j in range(4):

        aij = matrix[i,j]-(a21*abs(matrix[0,j]))
        #print(matrix[i,j])
        matrix[i,j] = round(aij,4)

print('\n',matrix)

for i in range(1,2):
    a22 = matrix[i,1]
    for j in range(4):
        if matrix[i,j]!=0:
            aij = matrix[i,j]/abs(a22)
            matrix[i,j] = round(aij,4)

print('\n',matrix)

for i in range(2,3):
    a32 = matrix[2,1]
    for j in range(4):
        if matrix[i,j]!=0:
            aij = matrix[i,j]-(a32*abs(matrix[1,j]))
            matrix[i,j] = round(aij,4)

print('\n',matrix,'\n')


print(matrix[0,0],'x ',matrix[0,1],'+ y ',matrix[0,2],'+ z = ',matrix[0,3])
print(matrix[1,1],'y ',matrix[1,2],' + z = ',matrix[1,3])
print(matrix[2,2],'z =',matrix[2,3])


constant = matrix[:,[3]].transpose()[0]
matrix = np.delete(matrix, 3, 1)
result = np.linalg.inv(matrix).dot(constant)
print('x=',round(result[0],2),', y=',round(result[1],2),', z=',round(result[2],2),"\n")

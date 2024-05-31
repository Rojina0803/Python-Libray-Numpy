#NUMPY
import numpy as np 
arr_1d = np.array([1,2,3,4,5])
print(arr_1d)

arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

#ARITHMETIC OPERATION
arr_a=np.array([1,2,3])
arr_b= np.array([1,2,3])

print(arr_a+arr_b)
print(arr_a*arr_b)

matrix_a= np.array([[1,2],[4,5]])
matrix_b= np.array([[0,9],[7,6]])
result=np.dot(matrix_a,matrix_b)  #Matrix multiplication
print(result)

arr= np.array([1,2,3,4,5,6,7])
print(arr[0])
print(arr[2:4])
print(arr[1:])
print(arr[-1])
print(arr[:-3])
print(arr[-3:])


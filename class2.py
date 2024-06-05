# #NUMPY
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
print(arr[-2:])


#MEAN:AVERAGE
array = np.arange(15)
print(array)
r1 = np.mean(array)
print("\nMean: ", r1)

a = np.array([[1, 2], [3, 4]])
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
print(np.mean(a, dtype=float ))

#MEDIAN
array = np.arange(25)
print(array)
r1 = np.median(array)
print("\nstd: ", r1)


#Standard deviation
array = np.arange(30)
print(array)
r1 = np.std(array)
print("\nstd: ", r1)

#ARRAY RESHAPING- Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
result = arr.reshape(2, 3, 2)
print(result)
print("\n",arr.reshape(4,3).base)


ary= np.array([[1,2],[3,4]])
result2= ary.reshape(-1)
print(result2)


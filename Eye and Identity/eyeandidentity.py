import numpy

numpy.set_printoptions(legacy ='1.13') # to print nicely

multi = input("N M : ").rstrip().split() # input => N M : 3 3

N = int(multi[0])

M = int(multi[1])

print(numpy.eye(N, M, k = 0)) # N x M k=0 means 1st value will be 1

print("\n",numpy.eye(3, 3, k = 1))

print("\n",numpy.identity(3)) #3 is for  dimension 3 X 3

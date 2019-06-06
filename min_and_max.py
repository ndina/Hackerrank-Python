import numpy
m, n = map(int, input().split())
my_arr = numpy.array([input().split() for i in range(m)], int)
print(numpy.max(numpy.min(my_arr, axis = 1)))

#20
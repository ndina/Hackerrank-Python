import numpy
n,m = map(int,input().split())
ar = numpy.array([input().split() for i in range(n)], int)
print(numpy.prod((numpy.sum(ar,axis=0))))


#20
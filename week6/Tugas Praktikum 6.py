A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = {}

a = A.difference(B)
b = B.difference(A)
c = A.difference(C)
d = B.difference(C)

print("A difference B = ", a)
print("B difference A = ", b)
print("A difference C = ", c)
print("B difference C = ", d)

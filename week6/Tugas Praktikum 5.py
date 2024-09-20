A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = {}

a = A.symmetric_difference(B)
b = B.symmetric_difference(A)
c = A.symmetric_difference(C)
d = B.symmetric_difference(C)

print("A symmetric difference B = ", a)
print("B symmetric difference A = ", b)
print("A symmetric difference C = ", c)
print("B symmetric difference C = ", d)

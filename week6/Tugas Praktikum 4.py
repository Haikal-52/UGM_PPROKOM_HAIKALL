A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

a = A | B
b = B | C
c = B | C | D
d = A | B | C | D

print("A U B = ", a)
print("B U C = ", b)
print("B U C U D = ", c)
print("A U B U C U D = ", d)

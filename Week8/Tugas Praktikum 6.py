data_array =  [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

ganjil = []
genap = [] 

for nilai in data_array:
    if nilai % 2 == 1:
        ganjil.append(nilai)
       
    else: 
        genap.append(nilai)

print("Ganjil = ", ganjil)
print(len(ganjil), "angka")
print("Genap = ", genap)
print(len(genap), "angka")

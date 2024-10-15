nilai_array = [4, 5, 11, 12, 14, 16, 16, 19]

bilangan_prima = []

for bilangan in nilai_array:
    if bilangan < 2:
        continue

    for i in range(2, bilangan):
        if bilangan % i == 0:
            break
    else:
        bilangan_prima.append(bilangan)


print("Bilangan prima dalam data array:", bilangan_prima)

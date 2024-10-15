nilai_array = []

jumlah_elemen = int(input("Masukkan jumlah elemen dalam array : "))

for nilai in range(jumlah_elemen):
   nilai1 = 1 + nilai
   nilai_array.append(nilai1)

print("Data nilai = ", nilai_array)

jumlah_kelipatan = int(input("Masukkan jumlah kelipatan : "))

jumlah_kelipatan1 = []

for kelipatan in nilai_array:
    if kelipatan % jumlah_kelipatan == 0:
        jumlah_kelipatan1.append(kelipatan)

print("Data nilai kelipatan = ", jumlah_kelipatan1)

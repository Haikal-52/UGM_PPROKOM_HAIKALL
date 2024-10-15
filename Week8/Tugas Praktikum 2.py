nilai_list = []

for i in range(5):
    nilai = float(input(f"Masukkan nilai ke-{i+1}:"))
    nilai_list.append(nilai)
    print(nilai_list)

pilihan = str(input("Pilih antara jumlah atau rata-rata : "))

if pilihan == "jumlah":
   jumlah = sum(nilai_list)
   print("Jumlah dari nilai datanya adalah ", jumlah)

elif pilihan == "rata-rata":
   jumlah = sum(nilai_list)
   panjang = len(nilai_list)
   rata_rata = jumlah / panjang
   print("Rata-rata dari nilai datanya adalah ", rata_rata)

else:
   print("Pilihan tidak valid")

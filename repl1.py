# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
n1 = int(input("masukkan data 1 :"))
n2 = int(input("masukkan data 2 :"))
n3 = int(input("masukkan data 3 :"))
rata_rata = n1 + n2 + n3 / 3
print(rata_rata)

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
n1 = int(input("masukkan bilangan minimum :"))
n2 = int(input("masukkan bilangan maksimum :"))
y = int(input("masukkan bilangan kelipatan :"))
jumlah = []

while n1 <= n2:
  if(n1 % y) == 0:
    print(n1)
    jumlah.append(n1)
  n1 += 1
print("jumlah :", len(jumlah))

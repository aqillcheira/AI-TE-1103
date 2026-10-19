
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

angka = [10, 20, 30, 40, 50]
cari = int(input("Masukkan angka yang dicari: "))

hasil = linear_search(angka, cari)

if hasil != -1:
    print("Data ditemukan pada indeks", hasil)
else:
    print("Data tidak ditemukan")

for angka in range(2, 21, 2):
    print(angka)


total_nilai = 0
jumlah_tugas = 0

while True:
    nilai = int(input("Masukkan nilai tugas (-99 untuk selesai): "))

    if nilai == -99:
        break

    total_nilai += nilai
    jumlah_tugas += 1

print("Total akumulasi nilai:", total_nilai)
print("Banyaknya tugas yang diinputkan:", jumlah_tugas)
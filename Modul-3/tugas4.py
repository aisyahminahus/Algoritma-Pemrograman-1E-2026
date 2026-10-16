
jumlah_beasiswa_penuh = 0

for i in range(1, 11):

    print("\nData Mahasiswa ke-", i)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Maaf,", nama, "tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Masukkan penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        print(nama, "mendapatkan beasiswa penuh.")
        jumlah_beasiswa_penuh = jumlah_beasiswa_penuh + 1

    elif penghasilan <= 5000000:
        print(nama, "mendapatkan beasiswa sebagian.")

    else:
        print(nama, "tidak mendapatkan beasiswa.")

    if jumlah_beasiswa_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break


print("\nJumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)
print("Proses seleksi selesai.")

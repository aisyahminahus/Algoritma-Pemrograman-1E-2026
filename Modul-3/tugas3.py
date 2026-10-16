kategori_A = 0
kategori_B = 0
kategori_C = 0
kategori_D = 0
kategori_E = 0

total_nilai = 0

nilai_tertinggi = 0
nilai_terendah = 0
nama_tertinggi = ""
nama_terendah = ""

for i in range(10):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40

    if nilai_akhir >= 85:
        kategori = "A"
        kategori_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        kategori_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        kategori_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        kategoru_D += 1
    else:
        kategori = "E"
        kategori_E += 1

    print("Nilai akhir:", nilai_akhir)
    print("Kategori:", kategori)

    total_nilai += nilai_akhir

    if i == 0:
        nilai_tertinggi = nilai_akhir
        nilai_terendah = nilai_akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if nilai_akhir > nilai_tertinggi:
            nilai_tertinggi = nilai_akhir
            nama_tertinggi = nama

        if nilai_akhir < nilai_terendah:
            nilai_terendah = nilai_akhir
            nama_terendah = nama

rata_rata = total_nilai / 10

print("\n===== REKAPITULASI NILAI =====")
print("Jumlah kategori A:", kategori_A)
print("Jumlah kategori B:", kategori_B)
print("Jumlah kategori C:", kategori_C)
print("Jumlah kategori D:", kategori_D)
print("Jumlah kategori E:", kategori_E)

print("\nNilai tertinggi:", nilai_tertinggi)
print("Nama mahasiswa:", nama_tertinggi)

print("\nNilai terendah:", nilai_terendah)
print("Nama mahasiswa:", nama_terendah)

print("\nRata-rata nilai akhir:", rata_rata)
password = input("Masukkan 3 Digit Password : ")
digit1 = int(password[0])
digit2 = int(password[1])
digit3 = int(password[2])
pelacak_awal = digit1 * digit3


if digit1 % 2 == 1:
    pelacak_pertama = pelacak_awal + 25
else :
    pelacak_pertama = pelacak_awal - digit2

if digit3 % 3 == 0:
    pelacak_akhir = pelacak_pertama // 3
else :
    pelacak_akhir = pelacak_pertama * 2

if pelacak_akhir > 50:
    kategori = "A"
elif pelacak_akhir > 20:
    kategori = "B"
else :
    kategori = "Ditolak"

if pelacak_akhir % 2 == 0:
    status = "Siklus Genap"
else :
    status = "Siklus Ganjil"

print("\n=== HASIL PEMERIKSAAN PASSWORD ===")
print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)
print("Nilai pelacak awal:", pelacak_awal)
print("Pelacak setelah tahap pertama:", pelacak_pertama)
print("Nilai pelacak akhir:", pelacak_akhir)
print("Kategori password:", kategori)
print("Status:", status)
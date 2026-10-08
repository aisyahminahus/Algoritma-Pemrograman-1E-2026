print("\n-----SISTEM KEAMANAN GARASI CIA-----")

pin = input("Masukkan 3 digit PIN           : ")
jam = int(input("Masukkan jam kedatangan (0-23) : "))

digit1 = int(pin[0])
digit2 = int(pin[1])
digit3 = int(pin[2])
pin_angka = int(pin)

if pin_angka % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Dibuka"
    else:
        status = "Garasi Malam Terbuka"
elif pin_angka % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi Pintu Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status = "Akses Ditolak Sepenuhnya"

cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n----- HASIL PEMERIKSAAN -----")
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)
print("Status akses  :", status)
print("Status CCTV   :", cctv)



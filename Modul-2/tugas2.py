print("-----SELAMAT DATANG DI KOPERASI DESO-----")

total_belanja = int(input("\nMasukkan Total Harga Belanja Anda : "))

if total_belanja % 100000 == 0:
    diskon = 100
elif total_belanja % 50000 == 0:
    diskon = 50
elif total_belanja % 10000 == 0:
    diskon = 20
elif total_belanja >= 200000:
    diskon = 10
else: 
    diskon = 0

potongan = int(total_belanja * diskon / 100)
total_bayar = int(total_belanja - potongan)
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("--PERHITUNGAN TOTAL BELANJA--")
print("Total belanja awal  : Rp", total_belanja)
print("Diskon              :", diskon, "%")
print("Potongan harga      : Rp", potongan)
print("Total yang dibayar  : Rp", total_bayar)
print("Status poin         :", status_poin)
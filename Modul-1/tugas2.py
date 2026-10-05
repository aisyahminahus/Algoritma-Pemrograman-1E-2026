#diketahui
jarak = 100
konsumsi_bensin = 40 
#motor dimas menghabiskan 1 liter besin dalam jarak 40km
bensin_awal = 1.5
harga_bensin = 10000

#memasuki rumus
jarakpulang_pergi = jarak * 2
bensin_full = int(jarakpulang_pergi / konsumsi_bensin)
beli_bensin = bensin_full - bensin_awal
biaya_bensin = int(beli_bensin * harga_bensin)

print("\nMENGHITUNG BENSIN YANG DIBUTUHKAN DIMAS DALAM PERJALANAN PULANG-PERGI\n")
print("Diketahui : ")
print("Jarak rumah =", jarak)
print("Konsumsi bensin perliter =", konsumsi_bensin, "km")
print("Bensin awal =", bensin_awal, "liter")
print("Harga bensin =", harga_bensin)

print("\nJawab :")
print("A. Jarak pulang-pergi =", jarakpulang_pergi, "km")
print("B. Bensin motor dimas full-tank =", bensin_full, "liter")
print("C. Bensin yang dibutuhkan agar full-tank =", beli_bensin, "liter")
print("D. Biaya yang dibutuhkan agar full-tank = Rp.", biaya_bensin, "\n")
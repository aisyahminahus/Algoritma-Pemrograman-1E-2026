jarak = 0
penumpang = 0
tarif = 0
total_jarak = 0
total_pendapatan = 0
jarak_terjauh = 0


while True :
    jarak = int(input("Masukkan total jarak yang di tempuh :"))

    if jarak < 0:
        continue
    if jarak == 0:
        break

    if jarak <= 5:
       tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000
    else : 
        tarif = 15000 + 500

    total_jarak += jarak
    penumpang += 1

    if penumpang % 5 == 0 or penumpang % 10 == 0:
       tarif = tarif * 0.5

    total_pendapatan += tarif 

    print("Total yang harus dibayar : Rp ", tarif)

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

if penumpang > 0:
    rata_rata = total_jarak / penumpang
else:
    rata_rata = 0


print("\n====REKAPITULASI KASIR BUS SIDOARJO====")
print("Jumlah penumpang :", penumpang)
print("Total pendapatan : Rp", total_pendapatan)
print("Jarak terjauh    :", jarak_terjauh, "km")
print("Rata rata jarak  :", rata_rata, "km")
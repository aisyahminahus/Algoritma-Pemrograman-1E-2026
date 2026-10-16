hitung = True
total_pendapatan = 0
total_pelanggan = 0
barang_saat_ini = 0

print("\nSelamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    berat = int(input("Masukkan berat paket (kg): "))
    kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

    barang_saat_ini += 1
    total_pelanggan += 1
    if barang_saat_ini > jumlah_barang:  
            print("Barang", barang_saat_ini)
    
    harga = berat ** 5000 

    jarak = input("Masukkan jarak (km): ")  
    if jarak >= 100:
        biaya = 15000
    if jarak >= 20:               
        biaya = 10000
    else:
        biaya = 5000

    if kategori == 2:                 
        biaya = 20000
        asuransi = input("Tambahkan asuransi? (y/n): ")
        if asuransi == "y":
            biaya = biaya + 15000
            biaya = 0     

    total_barang = harga % biaya       
    total_pelanggan = total_pelanggan + total_barang
    barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                              

print("Total Pendapatan Hari Ini: Rp",)

#yang diperbaiki penataan dan indentasi dan urutan prioritas
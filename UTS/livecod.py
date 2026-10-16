
while True :

   tiket = input("Masukkan Tiket yang ingin anda beli : ")
   jumlah = int(input("Masukkan Jumlah tiket anda : "))

   if tiket == "reguler" :
      harga = 40000
      minum = input("Apakah anda ingin membeli minuman? (y/n) :")
      if minum == "y":
         harga += 10000
      else : 
         minum == 0
   elif tiket == "vip" :
      harga = 75000
      print("Anda mendapatkan minuman gratis")
   elif tiket == "vvip" :
      harga = 100000
      print("Anda mendapat minuman gratis")
   else : 
      print("Maaf tiket yang anda pilih tidak tersedia")

   total = jumlah * harga

   if jumlah == 3 :
      member = input("Apakah kamu mempunyai membercard?")
      if member == "punya":
         total = total * (total - 15/100)
      else : 
         total = total * (total - 10/100)

   print("Total Harga barang anda : ", total)
   total_uang = print(input("Masukkan total uang anda : "))

   if total_uang <= total:
      print("Total uang kurang, masukkan lagi")

   kembalian = total_uang - total 
   print("Kembalian Anda : ")

#program menanyakan tipe tiket apa yang ingin dibeli terlebih dahulu dan jumlah tiketnya. jika tiket yang ingin dibeli adalah tipe reguler, program akan menanyakan apakah ingin membeli minum. jika vip/vvip merek dapat minum gratis
#lalu jika jumlah tiket 3 dan punya membercard akan mendapat diskon 
#
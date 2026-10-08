print("\n-----REAKTOR NUKLIR CHERBYNOL-----")

suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (bar): "))

if suhu >= 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    elif tekanan <= 50:
        status = "Bahaya Suhu: Segera Evakuasi!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("\n---[STATUS REAKTOR]---")
print("Suhu reaktor             :", suhu, "°C")
print("Tekanan gas              :", tekanan, "bar")
print("Status reaktor           :", status)
print("Status operasional pompa :", pompa)
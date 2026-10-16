while True: 
    a = int(input("Masukkan tinggi menara (2-15): "))
    if a > 2 and a < 15 :
       break
    print("Tinggi salah, Masukkan angka 2 sampai 15.")

for i in range(1, a + 1):
    print(" " * (a - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

for i in range(a - 1, 0, -1):
    print(" " * (a - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

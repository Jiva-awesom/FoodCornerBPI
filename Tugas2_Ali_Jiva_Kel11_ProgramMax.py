# Judul
print("========== Program Menentukkan Max ==========\n")

# Deklarasi
Bil1 = input("Masukkan bilangan 1: ")
Bil2 = input("Masukkan bilangan 2: ")
Bil3 = input("Masukkan bilangan 3: ")

# Proses & Output
if int(Bil1) >= int(Bil2) >= int(Bil3):
    print("Bilangan terbesar adalah ", Bil1)
elif int(Bil1) <= int(Bil2) >= int(Bil3):
    print("Bilangan terbesar adalah ", Bil2)
elif int(Bil1) <= int(Bil2) <= int(Bil3):
    print("Bilangan terbesar adalah ", Bil3)

# Akhir
print("\n---------------------------------------------")
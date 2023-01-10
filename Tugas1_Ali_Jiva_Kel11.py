# JUDUL
print("============= PROGRAM KASIR 3 BARANG =============")

# DEKLARASI
Barang1 = input("Barang ke-1: ")
Harga1 = input("Harga: Rp. ")
Jumlah1 = input("Jumlah: x ")
Barang2 = input("Barang ke-2: ")
Harga2 = input("Harga: Rp. ")
Jumlah2 = input("Jumlah: x ")
Barang3 = input("Barang ke-3: ")
Harga3 = input("Harga: Rp. ")
Jumlah3 = input("Jumlah: x ")


print(" ")

# PROSES
print("Pelanggan membeli: ")
print("1.", Barang1, "Rp.", int(Harga1), "x", int(Jumlah1), "Rp.", int(Jumlah1)*int(Harga1))
print("2.", Barang2, "Rp.", int(Harga2), "x", int(Jumlah2), "Rp.", int(Jumlah2)*int(Harga2))
print("3.", Barang3, "Rp.", int(Harga3), "x", int(Jumlah3), "Rp.", int(Jumlah3)*int(Harga3))

# PROSES HARGA TOTAL
HargaT = ((int(Harga1)*int(Jumlah1))
          + (int(Harga2)*int(Jumlah2))
          + (int(Harga3)*int(Jumlah3)))

# OUTPUT HARGA TOTAL
print("Total: Rp.", HargaT)

print(" ")

# PROSES DISKON
Diskon = input("Dapat diskon (%): ")
HargaD = int(HargaT)-(int(HargaT)*(int(Diskon)/100))

# OUTPUT HARGA TOTAL + DISKON
print("Total yang harus dibayar:", "Rp.", HargaD)

# PROSES UANG PELANGGAN
Uang = input("Uang Pelanggan: Rp. ")
Kembalian = int(Uang) - int(HargaD)

# OUTPUT KEMBALIAN
print("Kembalian: Rp.", int(Uang)-int(HargaD))

print(" ")

# END
print("Terima kasih telah belanja di toko kami!")
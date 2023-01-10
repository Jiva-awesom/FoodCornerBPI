# JUDUL
print("==========================================")
print("=                                        =")
print("=             TARIF PARKIR               =")
print("=                                        =")
print("==========================================")

# DEKLARASI
jampertama = 3500  # Harga 0
jamselanjut = 2000  # Harga 1

JamMasuk = input("Jam Masuk: ")  # Jam 0
JamKeluar = input("Jam Keluar: ")  # Jam 1
JamTotal = int(JamKeluar) - int(JamMasuk)  # ? Jam

print("==========================================")

# PROSES
if JamTotal <= 0:  # Format 12 Jam
    if JamTotal+12 > 0:
        print("Durasi: ", JamTotal+12, "Jam")
        print("Tarif Parkir: Rp", int(jampertama) + (int(JamTotal+12 - 1)*jamselanjut))
    elif JamTotal+12 <= 0:
        print("Gagal, Angka Waktu harus antara 0-12")

elif JamTotal > 0:  # Format 24 Jam
    print("Durasi: ", JamTotal, "Jam")
    print("Tarif Parkir: Rp", int(jampertama) + (int(JamTotal - 1) * jamselanjut))
else:  # Bisi ada kesalahan tapi gtw apa
    print("Gagal, Error tidak diketahui")

# AKHIR
print("==========================================")

# Kelompok 11
# Ketua: Pasa
# Ngetik : (Ali) Jiva
# Bantu : Rafie
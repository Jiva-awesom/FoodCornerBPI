# DEKLARASI
Saldo = 1000000
SPP = Saldo * float(0.025)
print(f"Saldo: Rp. {float(Saldo)}")
print(f"Pengeluaran Uang: Rp. {float(SPP)}")

# PROSES
if Saldo >= SPP:
    SaldoSisa = float(int(Saldo) - float(SPP))
else:
    SaldoSisa = Saldo
    print("Saldo tidak mencukupi. Tidak ada uang yang dikeluarkan")

# OUTPUT
print(f"\nSisa Saldo: Rp. {float(SaldoSisa)}")
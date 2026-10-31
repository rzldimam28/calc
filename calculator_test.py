# ===== PENGUJI OTOMATIS =====
# Letakkan file ini di folder yang sama dengan kalkulator.py
# Jalankan: python test_kalkulator.py

from calculator import tambah, kurang, kali, bagi, calc

lolos = 0
gagal = 0


def periksa(keterangan, fungsi, argumen, harapan):
    global lolos, gagal
    try:
        hasil = fungsi(*argumen)
    except Exception as e:
        print("  GAGAL  ", keterangan, "-> program error:",
              type(e).__name__, e)
        gagal = gagal + 1
        return

    if hasil == harapan:
        print("  LULUS  ", keterangan, "->", repr(hasil))
        lolos = lolos + 1
    else:
        print("  GAGAL  ", keterangan, "-> dapat", repr(hasil),
              ", harusnya", repr(harapan))
        gagal = gagal + 1


print("--- Fungsi dasar ---")
periksa("tambah(10, 3)", tambah, (10, 3), 13)
periksa("kurang(10, 3)", kurang, (10, 3), 7)
periksa("kali(10, 3)", kali, (10, 3), 30)
periksa("bagi(10, 4)", bagi, (10, 4), 2.5)

print()
print("--- Pembagian nol ---")
periksa("bagi(10, 0)", bagi, (10, 0), "Tidak bisa dibagi nol")

print()
print("--- calc dengan operasi sah ---")
periksa('calc(10, 3, "+")', calc, (10, 3, "+"), 13)
periksa('calc(10, 3, "-")', calc, (10, 3, "-"), 7)
periksa('calc(10, 3, "*")', calc, (10, 3, "*"), 30)
periksa('calc(10, 4, "/")', calc, (10, 4, "/"), 2.5)

print()
print("--- calc dengan kasus tepi ---")
periksa('calc(10, 0, "/")', calc, (10, 0, "/"), "Tidak bisa dibagi nol")
periksa('calc(10, 3, "^")', calc, (10, 3, "^"), "Operasi tidak dikenal")
periksa('calc(10, 3, "tambah")', calc, (10, 3, "tambah"), "Operasi tidak dikenal")
periksa('calc(10, 3, "")', calc, (10, 3, ""), "Operasi tidak dikenal")

print()
print("--- Harus return, bukan print ---")
periksa("tambah mengembalikan nilai", lambda: tambah(2, 3) is not None, (), True)
periksa("calc mengembalikan nilai", lambda: calc(2, 3, "+") is not None, (), True)

print()
print("====================================")
print("  LULUS :", lolos)
print("  GAGAL :", gagal)
print("  NILAI :", round(lolos / (lolos + gagal) * 100), "/ 100")
print("====================================")
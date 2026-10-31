# Tes Fungsi — Kalkulator

Pertemuan 6 · Foundry

---

## Yang Dikerjakan

Buat file baru, `calculator.py`, yg dicopy dari `calculator_placeholder`.

```python
tambah(a, b)
kurang(a, b)
kali(a, b)
bagi(a, b)
calc(num_1, num_2, op)
```

`op` berupa `"+"`, `"-"`, `"*"`, atau `"/"`.

---

## Aturan

1. `bagi(a, 0)` mengembalikan teks `Tidak bisa dibagi nol` — bukan error.
2. `calc` dengan `op` yang tidak dikenal mengembalikan teks `Operasi tidak dikenal`.
3. **`calc` sebaiknya tidak memakai `if`, `elif`, atau `else`.**
---

## Menguji Sendiri

Sudah ada penguji otomatis di folder ini. 

```bash
python calculator_test.py
```

15 kasus uji. Kejar 100.
Penguji ini tidak memeriksa aturan nomor 4. Itu diperiksa manual.
nilai = int(input("Masukkan angka: "))
while nilai < 0:
    print("Harus positif ya!")
    nilai = int(input("Masukkan angka: "))
print(f"Angka yang diterima: {nilai}")
print("Program selesai")
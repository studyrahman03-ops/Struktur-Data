nama_asli = "rahman"

nama = input("Masukkan nama anda: ")
while nama.lower() != nama_asli:
    print("Silahkan coba lagi")
    nama = input("Masukkan nama anda: ")

print("Nama benar, lanjut ke program...\n")
angka = int(input("Masukkan angka: "))

for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")
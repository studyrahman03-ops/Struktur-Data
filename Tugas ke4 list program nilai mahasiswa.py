data_mahasiswa = [
    ["pandu", 44],
    ["anam", 60],
    ["menah", 78],
    ["dora", 90]
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        print("\nDaftar Mahasiswa")
        for data in data_mahasiswa:
            print("Nama:", data[0], "| Nilai:", data[1])

    elif pilihan == "2":
        nama = input("Masukkan Nama: ")
        nilai = int(input("Masukkan Nilai: "))
        data_mahasiswa.append([nama, nilai])
        print("Data berhasil ditambahkan!")

    elif pilihan == "3":
        nama = input("Masukkan nama yang akan diubah: ")

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data[0] = input("Nama baru: ")
                data[1] = int(input("Nilai baru: "))
                print("Data berhasil diubah!")
                break
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Masukkan nama yang akan dihapus: ")

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data_mahasiswa.remove(data)
                print("Data berhasil dihapus!")
                break
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "5":
        nama = input("Masukkan nama yang dicari: ")

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                print("Nama :", data[0])
                print("Nilai:", data[1])
                break
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "6":
        data_mahasiswa.sort(key=lambda x: x[1], reverse=True)

        print("\nData setelah diurutkan:")
        for data in data_mahasiswa:
            print("Nama:", data[0], "| Nilai:", data[1])

    elif pilihan == "7":
        total = 0

        for data in data_mahasiswa:
            total += data[1]

        rata_rata = total / len(data_mahasiswa)

        print("Rata-rata nilai =", rata_rata)

    elif pilihan == "8":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")

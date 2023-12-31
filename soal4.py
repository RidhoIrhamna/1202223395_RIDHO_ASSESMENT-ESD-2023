def cek_duplikat(data):
    # Menggunakan set untuk menyimpan nilai yang telah muncul sebelumnya
    duplikat = set()
    
    # Iterasi melalui setiap angka dalam data
    for angka in data:
        # Jika angka sudah ada dalam set duplikat, maka ada duplikat
        if angka in duplikat:
            return True
        # Tambahkan angka ke set duplikat jika belum ada
        duplikat.add(angka)
    
    # Jika tidak ditemukan duplikat setelah iterasi selesai
    return False

# Contoh penggunaan fungsi
data_1 = [1, 2, 3, 4, 5]
data_2 = [1, 2, 3, 4, 2]

hasil_1 = cek_duplikat(data_1)
hasil_2 = cek_duplikat(data_2)

# Menampilkan hasil
if hasil_1:
    print("True")
else:
    print("False")

if hasil_2:
    print("True")
else:
    print("False")

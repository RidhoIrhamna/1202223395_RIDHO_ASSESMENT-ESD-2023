from itertools import product

def hitung_kombinasi_username(nama_lengkap, panjang_max):
    # Menggabungkan nama lengkap menjadi satu string tanpa spasi dan diubah menjadi huruf kecil
    nama_lengkap = nama_lengkap.replace(" ", "").lower()
    panjang_nama = len(nama_lengkap)
    
    # Membuat kombinasi dari karakter dalam nama_lengkap sesuai panjang maksimal yang diinginkan
    kombinasi = []
    for i in range(1, panjang_max + 1):
        kombinasi.extend([''.join(c) for c in product(nama_lengkap, repeat=i)])

    return kombinasi

# Nama lengkap
nama_lengkap = "Naip Lovyu"

# Panjang maksimal username
panjang_max_username = 6

# Menghitung kombinasi username yang mungkin
kombinasi_username = hitung_kombinasi_username(nama_lengkap, panjang_max_username)

# Menampilkan jumlah kombinasi username yang mungkin
print(f"Jumlah kombinasi username yang mungkin dari nama '{nama_lengkap}' adalah: {len(kombinasi_username)}")

# Data produk
produk = [
    {"nama": "TV", "kategori": "elektronik", "harga": 1000},
    {"nama": "headphone", "kategori": "elektronik", "harga": 200},
    {"nama": "baju", "kategori": "fashion", "harga": 50},
    {"nama": "gitar", "kategori": "musik", "harga": 300},
    {"nama": "sepatu", "kategori": "olahraga", "harga": 80},
    {"nama": "kamera", "kategori": "elektronik", "harga": 600}
]

# Data pelanggan
pelanggan = [
    {"nama": "Rina", "minat": ["elektronik", "musik"], "beli": ["TV", "headphone"]},
    {"nama": "Budi", "minat": ["fashion", "musik"], "beli": ["baju", "gitar"]},
    {"nama": "Hartono", "minat": ["olahraga", "elektronik"], "beli": ["sepatu", "kamera"]}
]

# Fungsi untuk memberikan rekomendasi produk berdasarkan minat
def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = [pel['minat'] for pel in pelanggan if pel['nama'] == nama_pelanggan][0]
    produk_terpilih = []
    
    for prod in produk:
        if prod['kategori'] in minat_pelanggan and prod['nama'] not in produk_terpilih:
            produk_terpilih.append(prod['nama'])
    
    return produk_terpilih

# Memperoleh rekomendasi produk untuk setiap pelanggan
for pel in pelanggan:
    nama_pelanggan = pel['nama']
    rekomendasi = rekomendasi_produk(nama_pelanggan)
    print(f"{nama_pelanggan}: {rekomendasi}")

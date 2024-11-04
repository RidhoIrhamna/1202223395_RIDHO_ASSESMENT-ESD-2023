# Harga setiap item menu
harga_ayam_goreng = 15000
harga_ayam_puk_puk = 13000
harga_ayam_bakar = 20000
harga_es_teh = 5000
harga_es_jeruk = 7000

# Pesanan masing-masing sahabat
rehan_pesanan_ayam_bakar = 2
rehan_pesanan_es_teh = 1

amba_pesanan_ayam_puk_puk = 1
amba_pesanan_es_teh = 3

faiz_pesanan_ayam_goreng = 1
faiz_pesanan_ayam_puk_puk = 1
faiz_pesanan_ayam_bakar = 1
faiz_pesanan_es_teh = 1
faiz_pesanan_es_jeruk = 1

# Menghitung total biaya untuk masing-masing sahabat
total_rehan = (rehan_pesanan_ayam_bakar * harga_ayam_bakar * 1.05) + (rehan_pesanan_es_teh * harga_es_teh * 1.03)
total_amba = (amba_pesanan_ayam_puk_puk * harga_ayam_puk_puk * 1.05) + (amba_pesanan_es_teh * harga_es_teh * 1.03)
total_faiz = (faiz_pesanan_ayam_goreng * harga_ayam_goreng * 1.05) + (faiz_pesanan_ayam_puk_puk * harga_ayam_puk_puk * 1.05) + (faiz_pesanan_ayam_bakar * harga_ayam_bakar * 1.05) + (faiz_pesanan_es_teh * harga_es_teh * 1.03) + (faiz_pesanan_es_jeruk * harga_es_jeruk * 1.03)

# Menghitung pajak transaksi untuk setiap sahabat
total_rehan *= 1.15
total_amba *= 1.15
total_faiz *= 1.15

# Menampilkan total biaya yang harus dibayar oleh masing-masing sahabat (dikonversi ke integer)
print("Biaya yang harus dibayar oleh Rehan Whangsap:", int(round(total_rehan, 0)))
print("Biaya yang harus dibayar oleh Amba Roni:", int(round(total_amba, 0)))
print("Biaya yang harus dibayar oleh Faiz ngawi:", int(round(total_faiz, 0)))

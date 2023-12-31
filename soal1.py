def analisis_rating_aplikasi(data_review):
    if not data_review:
        return None, None, None

    min_rating = min(data_review)
    max_rating = max(data_review)
    rata_rata_rating = sum(data_review) / len(data_review)

    return min_rating, max_rating, round(rata_rata_rating, 1)

# Contoh data review aplikasi
data_review = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]

# Memanggil fungsi untuk menganalisis data review aplikasi
output = analisis_rating_aplikasi(data_review)

# Menampilkan hasil
print("Rating terendah:", output[0])  # Rating terendah
print("Rating tertinggi:", output[1])  # Rating tertinggi
print("Rata-rata rating:", output[2])  # Rata-rata rating
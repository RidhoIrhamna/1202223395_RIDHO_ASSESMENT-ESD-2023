def cek_palindrom(kata):
    # Menghapus spasi dan mengubah ke huruf kecil
    kata = kata.replace(" ", "").lower()

    # Mengecek apakah kata merupakan palindrom atau bukan
    return kata == kata[::-1]

# Contoh penggunaan fungsi untuk mengecek palindrom
input_1 = "Angsa"
input_2 = "KataK"
input_3 = "kasur empuk"
input_4 = "Aku Suka Kamu"
input_5 = "Ibu Ratna antar ubi."


hasil_1 = cek_palindrom(input_1)
hasil_2 = cek_palindrom(input_2)
hasil_3 = cek_palindrom(input_3)
hasil_4 = cek_palindrom(input_4)
hasil_5 = cek_palindrom(input_5)


# Menampilkan hasil
if hasil_1:
    print(f"'{input_1}' = eureeka! ")
else:
    print(f"'{input_1}' = suka blyat ")

if hasil_2:
    print(f"'{input_2}' = eureeka! ")
else:
    print(f"'{input_2}' = suka blyat ")

if hasil_3:
    print(f"'{input_3}' = eureeka! ")
else:
    print(f"'{input_3}' = suka blyat ")

if hasil_4:
    print(f"'{input_4}' = eureeka! ")
else:
    print(f"'{input_4}' = suka blyat ")

if hasil_5:
    print(f"'{input_5}' = eureeka! ")
else:
    print(f"'{input_5}' = suka blyat ")
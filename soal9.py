from collections import Counter

# Fungsi untuk menentukan anak nakal berdasarkan input
def anak_nakal(daftar_nama):
    counter_nama = Counter(daftar_nama)
    jumlah_kemunculan = counter_nama.most_common()

    if jumlah_kemunculan[0][1] == 1:
        return "Semuanya anak baik"
    elif jumlah_kemunculan[0][1] == jumlah_kemunculan[1][1]:
        anak_nakal = " dan ".join([nama for nama, count in jumlah_kemunculan if count == jumlah_kemunculan[0][1]])
        return f"{anak_nakal} Nakal"
    else:
        anak_nakal = jumlah_kemunculan[0][0]
        return f"{anak_nakal} Nakal"

# Test case
input_1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
output_1 = anak_nakal(input_1)
print(output_1)

input_2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
output_2 = anak_nakal(input_2)
print(output_2)

input_3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]
output_3 = anak_nakal(input_3)
print(output_3)

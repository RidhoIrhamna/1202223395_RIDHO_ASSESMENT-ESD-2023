def siapa_yang_mengambil_kue():
    # Kue masih utuh saat Xiao memotretnya
    xiao_menemukan_kue_utuh = True

    # Ningguang memeriksa kue sebelum memberikan kado
    ningguang_memeriksa_kue = True

    # Hutao langsung memberikan kado tanpa memperhatikan kue
    hutao_menyumbang_kado_tanpa_memeriksa_kue = True

    # Childe selalu membawa air mineral dan meletakkannya di meja sebelum memberikan kado
    childe_melepas_air_mineral = False

    # Menggunakan logika sederhana untuk menentukan siapa yang mungkin mengambil kue
    if not xiao_menemukan_kue_utuh and not ningguang_memeriksa_kue:
        return "Ningguang"
    elif hutao_menyumbang_kado_tanpa_memeriksa_kue:
        return "Hutao"
    elif childe_melepas_air_mineral:
        return "Childe"
    else:
        return "Tidak dapat menentukan"

# Memanggil fungsi untuk menentukan siapa yang mungkin mengambil kue
pelaku_pencurian = siapa_yang_mengambil_kue()

# Menampilkan hasil
if pelaku_pencurian != "Tidak dapat menentukan":
    print(f"Berdasarkan logika sederhana, {pelaku_pencurian} adalah yang paling mungkin mengambil kue.")
else:
    print("Tidak dapat menentukan siapa yang mengambil kue berdasarkan informasi yang diberikan.")

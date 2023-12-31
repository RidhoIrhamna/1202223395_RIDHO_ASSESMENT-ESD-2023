def hitung_kembalian(total_pembayaran, total_belanja):
    uang_kembali = total_pembayaran - total_belanja
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    hasil_kembalian = {}

    for pecahan in pecahan_uang:
        if uang_kembali >= pecahan:
            jumlah_pecahan = uang_kembali // pecahan
            hasil_kembalian[str(pecahan)] = jumlah_pecahan
            uang_kembali -= jumlah_pecahan * pecahan

    return hasil_kembalian

# Test cases
test_case_1 = hitung_kembalian(10000, 7500)
print(test_case_1)  # Output: {'500': 1, '2000': 1}

test_case_2 = hitung_kembalian(5000, 1100)
print(test_case_2)  # Output: {'200': 2, '500': 1, '1000': 1, '2000': 1}

test_case_3 = hitung_kembalian(178000, 90500)
print(test_case_3)  # Output: {'500': 1, '2000': 1, '5000': 1, '10000': 1, '20000': 1, '50000': 1}

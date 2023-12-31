def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - 5
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            else:
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Isi chat yang akan didekripsi
encrypted_chats = [
    "xfqfr bfmdz",
    "gjxtp lzj rfz ifkyfw jxi snm",
    "gwt, gjxtp qz rfz rfpfs in bfwlty lfp?",
    "fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz",
    "dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"
]

# Melakukan dekripsi pada setiap pesan
for index, chat in enumerate(encrypted_chats, start=1):
    decrypted = decrypt(chat)
    print(f"i. Dekripsi isi chat {index}: {decrypted}")

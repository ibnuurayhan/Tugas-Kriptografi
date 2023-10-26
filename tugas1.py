def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Hanya proses karakter alfabet
            shift = 65 if char.isupper() else 97  # ASCII kode untuk 'A' atau 'a'
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_char = char  # Jika bukan alfabet, biarkan seperti itu
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Hanya proses karakter alfabet
            shift = 65 if char.isupper() else 97  # ASCII kode untuk 'A' atau 'a'
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted_char = char  # Jika bukan alfabet, biarkan seperti itu
        decrypted_text += decrypted_char
    return decrypted_text

# Contoh penggunaan
plaintext = "Ini adalah contoh pesan rahasia"
key = 3  # Kunci pergeseranx

encrypted_text = caesar_encrypt(plaintext, key)
decrypted_text = caesar_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)

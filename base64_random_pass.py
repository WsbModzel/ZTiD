#ex 1
import base64

def encrypt_base64(text):
    # Convert text to bytes
    text_bytes = text.encode('utf-8')
    
    # Encrypt using base64
    encrypted = base64.b64encode(text_bytes)
    
    # Decode to a string
    result = encrypted.decode('utf-8')
    
    return result



text_to_encrypt = "Hello, Boss!"
encrypted_text = encrypt_base64(text_to_encrypt)

print("Text to encrypt:", text_to_encrypt)
print("Encrypted text:", encrypted_text)

# Decrypted text
decrypted_text = base64.b64decode(encrypted_text).decode('utf-8')

print("Decrypted text:", decrypted_text)


#ex 2
import random
import string

def generate_secure_password():
    # Define character sets for each password requirement
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation

    # Combine all character sets
    all_char = lower_letters + upper_letters + digits + special_char

    # Ensure the password is at least 8 and max between 12 and 18 characters long
    password_length = max(8, random.randint(12, 18))
    password = random.sample(lower_letters, 1) + random.sample(upper_letters, 1) + \
               random.sample(digits, 1) + random.sample(special_char, 1) + \
               random.sample(all_char, password_length - 4)

    # Shuffle the characters to make the password random
    random.shuffle(password)

    # Convert the list of characters to a string
    secure_password = ''.join(password)

    return secure_password

#ex 1
password_result = generate_secure_password()
print("Generated secure password:", password_result)

###Question_1###
def encrypt_text(file_in, file_out, n, m):
    """
    Encrypt the content of a file based on the given rules and save to a new file.
    """
    with open(file_in, "r") as fin:
        raw_text = fin.read()

    encrypted_text = ""
    for char in raw_text:
        if 'a' <= char <= 'm':  # Lowercase, first half
            encrypted_text += chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
        elif 'n' <= char <= 'z':  # Lowercase, second half
            encrypted_text += chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
        elif 'A' <= char <= 'M':  # Uppercase, first half
            encrypted_text += chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
        elif 'N' <= char <= 'Z':  # Uppercase, second half
            encrypted_text += chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
        else:  # Special characters and numbers remain unchanged
            encrypted_text += char

    with open(file_out, 'w') as fout:
        fout.write(encrypted_text)

def decrypt_text(file_in, file_out, n, m):
    """
    Decrypt the content of a file based on the given rules and save to a new file.
    """
    with open(file_in, 'r') as fin:
        encrypted_text = fin.read()

    decrypted_text = ""
    for char in encrypted_text:
        if 'a' <= char <= 'm':  # Lowercase, first half
            decrypted_text += chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
        elif 'n' <= char <= 'z':  # Lowercase, second half
            decrypted_text += chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
        elif 'A' <= char <= 'M':  # Uppercase, first half
            decrypted_text += chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        elif 'N' <= char <= 'Z':  # Uppercase, second half
            decrypted_text += chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
        else:  # Special characters and numbers remain unchanged
            decrypted_text += char

    with open(file_out, 'w') as fout:
        fout.write(decrypted_text)

def check_decryption(original_file, decrypted_file):
    """
    Compare the original file with the decrypted file to ensure correctness.
    """
    with open(original_file, 'r') as f1, open(decrypted_file, 'r') as f2:
        original_text = f1.read()
        decrypted_text = f2.read()
    
    return original_text == decrypted_text

def main():
    input_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Get user inputs
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    # Encrypt the text
    encrypt_text(input_file, encrypted_file, n, m)
    print(f"Encrypted text written to {encrypted_file}")

    # Decrypt the text
    decrypt_text(encrypted_file, decrypted_file, n, m)
    print(f"Decrypted text written to {decrypted_file}")

    # Check decryption correctness
    if check_decryption(input_file, decrypted_file):
        print("Decryption is correct.")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()

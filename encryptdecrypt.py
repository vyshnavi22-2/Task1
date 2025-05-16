def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Tool")
    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, (Q)uit: ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("Invalid input. Shift must be an integer.")
                continue
            if choice == 'E':
                encrypted = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {encrypted}")
            else:
                decrypted = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {decrypted}")
        else:
            print("Invalid choice. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()
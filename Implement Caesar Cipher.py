def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode - encrypt (e) or decrypt (d): ").lower()
    if mode not in ['e', 'd']:
        print("Invalid mode selected. Please choose 'e' or 'd'.")
        return
    
    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Shift value must be an integer.")
        return
    
    if mode == 'd':
        shift = -shift
    
    result = caesar_cipher(message, shift)
    print("Result:", result)

if __name__ == "__main__":
    main()


    
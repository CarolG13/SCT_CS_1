def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

while True:
    # Get user input
    message = input("Enter the message (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        continue

    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        continue

    # Perform encryption or decryption
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}\n")

text = input("Enter the message: ")
shift = int(input("Enter shift key: "))
choice = input("Enter E for Encode or D for Decode: ").upper()

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')

        if choice == 'E':
            result += chr((ord(ch) - base + shift) % 26 + base)
        elif choice == 'D':
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            print("Invalid choice!")
            break
    else:
        result += ch

if choice in ['E', 'D']:
    print("Result:", result)
    
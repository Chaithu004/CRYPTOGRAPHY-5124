import math

def main():
    message = input("Enter message: ")
    key = int(input("Enter key [2-%s]: " % (len(message) - 1)))
    mode = input("Encryption/Decryption [e/d]: ")

    if mode.lower().startswith("e"):
        text = encryptMessage(key, message)
    elif mode.lower().startswith("d"):
        text = decryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print("Output:\n%s" % (text + "|"))


def encryptMessage(key, message):
    
    cipherText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return "".join(cipherText)


# Example usage
if _name_ == "_main_":
    main()

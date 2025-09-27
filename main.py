import string
#user input
#Shift
#Alphabets
#shift ahead new alphabet
#replace orig with new
#print new string
def ceaser_cypher(sentence, shift):
    new_sentence = ""
    alphabets = string.ascii_letters
    for word in sentence:
        if word in alphabets:
            index = alphabets.index(word)
            new_sentence += alphabets[(index + shift) % len(alphabets)]
        else:
            new_sentence += word
    return new_sentence

def decypher(sentence, shift):
    new_sentence = ""
    alphabets = string.ascii_letters
    for word in sentence:
        if word in alphabets:
            index = alphabets.index(word)
            new_sentence += alphabets[(index - shift) % len(alphabets)]
        else:
            new_sentence += word
    return new_sentence

def main():
    option = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if option == 'd':
        sent = input("Enter the sentence you want to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_sentence = decypher(sent, shift)
        print("Decrypted sentence:", decrypted_sentence)
        return
    elif option == 'e':
        sent = input("Enter the sentence you want to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_sentence = ceaser_cypher(sent, shift)
        print("Encrypted sentence:", encrypted_sentence)

if __name__ == "__main__":
    main()
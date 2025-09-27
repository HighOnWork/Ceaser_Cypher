#user input
#Shift
#Alphabets
#shift ahead new alphabet
#replace orig with new
#print new string
def ceaser_cypher(sentence, shift):
    pass

def main():
    sent = input("Enter the sentence you want to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_sentence = ceaser_cypher(sent, shift)
    print("Encrypted sentence:", encrypted_sentence)

if __name__ == "__main__":
    main()
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#encode (plain text to cipher code)
def encode_plain_text(plain_text,shifting_alphabets):
    cipher_text=""
    for letter in plain_text:
        if letter in "aeiou":
            index_position=alphabet.index(letter)
            new_position=index_position+(shifting_alphabets+1)
            new_alphabet=alphabet[new_position]
            cipher_text+=new_alphabet 
        elif letter == " ":
            cipher_text+=" "
        elif letter not in alphabet:
            cipher_text+="~"      
        else:
            index_position=alphabet.index(letter)
            new_position=index_position+shifting_alphabets
            new_alphabet=alphabet[new_position]
            cipher_text+=new_alphabet
    print(f"your cipher code is= {cipher_text}")
#decode (cipher code to plain text)
def decode_cipher_code(cipher_code,shifting_alphabets):
    plain_message=""
    for letter in cipher_code:
        if letter in "aeiou":
            index_position=alphabet.index(letter)
            new_position=index_position-(shifting_alphabets-1)
            new_alphabet=alphabet[new_position]
            plain_message+=new_alphabet
        elif letter == " ":
            cipher_text+=" "
        elif letter not in alphabet:
            cipher_text+="~"  
        else:
            index_position=alphabet.index(letter)
            new_position=index_position-shifting_alphabets
            new_alphabet=alphabet[new_position]
            plain_message+=new_alphabet
    print(f"your plain_text is= {plain_message}")
start=True
while start:
    choice=input("What do you want (encode/decode) ?")
    choice1=choice.lower()
    message=input("Enter your message you want to encode/decode = ")
    shift=int(input("how much shifting your want ="))
    if choice1=="encode":
        encode_plain_text(message,shift)
        start=False
    elif choice1=="decode":
        decode_cipher_code(message,shift)
        start=False
    else:
        print(f"you hit the wrong direction")





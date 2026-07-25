from string import ascii_lowercase
def validate_text(char):
    return char.isalpha()
def encode_text(shift_amount, msg):
    alphabet = ascii_lowercase
    txt = ""

    for char in msg:
        if validate_text(char):
            pos = alphabet.index(char)
            new_pos = (pos + shift_amount) % 26
            txt += alphabet[new_pos]
        else:
            txt += char

    return txt


def decode_text(shift_amount, msg):
    alphabet = ascii_lowercase
    txt = ""

    for char in msg:
        if validate_text(char):
            pos = alphabet.index(char)
            new_pos = (pos - shift_amount) % 26
            txt += alphabet[new_pos]
        else:
            txt += char

    return txt


def main():
    while True:
        msg = input("Enter message:\n").lower()
        shift_amount = int(input("Enter shift amount:\n"))

        mode = input("Enter mode (encrypt/decrypt):\n").lower()

        if mode == "encrypt":
            result = encode_text(shift_amount, msg)

        elif mode == "decrypt":
            result = decode_text(shift_amount, msg)

        else:
            print("Invalid mode")
            continue

        print(f"Result: {result}")

        again = input("Continue? yes/no:\n").lower()

        if again != "yes":
            break

if __name__=="__main__":
    main()
              
        
           
               
        
               
               
               
                
                
            
            
    
        
               
    
                
            
    

            
            
        
print("Welcome to the world of cryptography")
def main():
    print()
    print("Choose an option: ")
    choice=int(input("1.Encryption\n2.Descryption\nChoose (1,2):"))
    if choice==1:
        encryption()
    elif choice==2:
        decryption()
    else:
        print("Invalid Choice! Try Again.")
        
def encryption():
    print("Encryption")
    message=input("Enter Your Message : ")
    key=int(input("Enter Key 1-94 : "))
    encrypted_message="" 
    for i in range(len(message)):
        temp=(ord(message[i])+key)
        if temp > 126:
            temp=temp-127+32
        encrypted_message+=chr(temp)
    print("encrypted:",encrypted_message)
    main()

def decryption():
    print("Decryption")
    encrypted_message=input("Enter Encrypted Message : ")
    key=int(input("Enter Key 1-94 : "))
    decrypted_message=""
    for i in range(len(encrypted_message)):
        temp=(ord(encrypted_message[i])-key)
        if temp < 32:
            temp=temp+127-32
        decrypted_message+=chr(temp)
    print("decrypted text :",decrypted_message)

main()
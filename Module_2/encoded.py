message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if ch.isalpha():
        shift = offset
        if ch.islower():
            start = ord('a')
        elif ch.isupper():
            start = ord('A')
        encoded_ch = chr(start + (ord(ch) - start + shift) % 26)
    else:
        encoded_ch = ch
    encoded_message += encoded_ch

print("Encoded Message: ", encoded_message)

        
    
        
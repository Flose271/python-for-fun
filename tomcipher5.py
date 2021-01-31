
print("----------")
print("Welcome to Tom's Cipher program")
print("----------")

while True:
    while True:
        ans = input("Would you like to code or decode?")
        ans = str.lower(ans)
        if(ans == 'code' or ans == 'decode'):
            break
        else:
            print("Invalid response. Please re-answer.")

    key = input('Please enter the keyword: ')


                       
    if(ans == 'code'):

        new = []
        x = []
        
        string = input("Enter your message to be ciphered: ")
        
        for i in range(0,len(string)):
            x.append(key)

        key = ''.join(x)

            
        for i in range(0,len(string)):

            c = ord(string[i])
            
            t = ord(key[i])
            c = c + t
            if(c > 126):
                c = c - 95
            c = chr(c)
            
            new.append(c)

        new = ''.join(new)

        print(new)
        
            
            
    if(ans == 'decode'):

        new = []
        x = []
        
        string = input("Enter your string to be deciphered: ")
        
        for i in range(0,len(string)):
            x.append(key)

        key = ''.join(x)

            
        for i in range(0,len(string)):

            c = ord(string[i])

            t = ord(key[i])
            c = c - t
            if(c < 32):
                c = c + 95
            c = chr(c)
            
            new.append(c)

        new = ''.join(new)

        print(new)
            
    print("----------")


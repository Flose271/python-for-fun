ask = input("Test or run? (t/r): ")
if(ask == "t"):
    v = input("Starting Positive Integer: ")
    v = int(v)
    while True:
        if(v%2 == 0):
            v = v/2
            print(v)
        else:
            v = (v*3) + 1
            print(v)
        if(v == 1):
            break
elif(ask == "r"):
    for i in range (1,100):
       print("----------")
       print(i)
       print("----------") 
       v = int(i)
       while True:
        if(v%2 == 0):
            v = v/2
            print(v)
        else:
            v = (v*3) + 1
            print(v)
        if(v == 1):
            break
        

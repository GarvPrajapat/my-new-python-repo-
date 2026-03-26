def printop(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")

printop(firstName = "Garv", lastName = "Prajapat")
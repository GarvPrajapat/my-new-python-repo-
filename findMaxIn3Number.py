# WAP to find the greatest of 3 numbers entered by the user.
num1 = int (input("Enter the 1st number: "))
num2 = int (input("Enter the 2nd number: "))
num3 = int (input("Enter the 3rd number: "))

if(num1>num2 and num1>num3):
    print("\n",num1,"is greatest")
elif(num2>num3):
    print("\n",num2,"is greatest")
else:
    print("\n",num3,"is greatest")
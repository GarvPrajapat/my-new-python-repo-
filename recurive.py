def fact(num: int) -> int:
    if num <=1:
        return 1
    else:
        return num * fact(num-1)

Num: int = int(input("Enter the number for factorial: "))
print(f"the factorial of Number {Num} is : {fact(Num)}")  
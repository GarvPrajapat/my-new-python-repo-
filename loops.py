# first of all in very interst in about loop :)

# i=5
# while i:
#     print(i)
#     i-=1

# List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i<len(List):
#     print(List[i])
#     i+=1


arr = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = int(input("Enter the number you want to find in list :"))
for i in arr:
    if(i==num):
        print(f"the value is at index {i}")
        break
else:
    print("the number is not found in array")

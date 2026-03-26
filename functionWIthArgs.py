def sum(*arr):
    sum = 0 
    for i in arr:
        sum +=i
    return sum 

print(sum(2,3,5))
print(sum(2,3,5,32,523))
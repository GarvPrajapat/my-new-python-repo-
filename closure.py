# this code give a little explaination of closure in python

def power(p:int):
    def expo(x:int) -> int:
        return x**p
    return expo

power2 = power(2)

print(power2(3))
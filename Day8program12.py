def checkEven(num1):
    if num1%2==0:
        return "Even"
def checkOdd(num1):
    if num1%2==1:
        return "Odd"
    return None

num=int(input("enter a number:"))
x=checkEven(num)
y=checkOdd(num)
print("x=",x)
print("y=",y)

print(checkEven(num))
print(checkOdd(num))

##x="hello"
##
##if not type(x) is int:
##    raise TypeError("only integers are allowed")

a=10
b=9
try:
    if a<0 or b<0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("please enter valid integer value")

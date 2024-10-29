def calculator ():
    x=float(input("input integer 1"))
    operand=input("input operand")
    y=float(input("input integer 2"))

    if operand == "+":
        print(x+y)
    elif operand == "-":
        print(x-y)
    elif operand == "/":
        print(x/y)
    elif operand == "*":
        print(x*y)

calculator ()




def calc(m, x, n):
    if x == "+":
       return int(m)+int(n)
    elif x == "-":
        return int(m)-int(n)
    elif x == "*":
        return int(m)*int(n)
    elif x == "/":
        return int(m)/int(n)

var1=input("Enter n1")
var2=input("Enter n2")
var3=input("Enter operand")
print(calc(var1,var3,var2))


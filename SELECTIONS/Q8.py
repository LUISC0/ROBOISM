def total(x):
    var=0
    sum=0
    for ch in x:
        if(ch.isdigit()):
            var += int(ch)
    return var

x=input("Enter a string:")
print(total(x))


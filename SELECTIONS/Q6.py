v1 = int(input("Enter the lower limit : "))
v2 = int(input("Enter the upper limit : "))
for n in range(v1,v2 + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n,end=" ")
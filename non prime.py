a=int(input("enter a number:"))
b=int(input("enter a number:"))
for x in range(a,b+1):
    if x>1:
        for i in range(2,x):
            if(x%i)==0:
              print(x)
              break

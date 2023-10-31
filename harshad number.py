num=int(input("enter a number:"))
sum=rem=0
temp=num
while temp>0:
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if num%sum==0:
    print("harshad number")
else:
    print("not a harshad number")
   

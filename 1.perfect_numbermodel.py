num=int(input("Enter value of num: "))  
sum=0  
for i in range(1,num):  
    if (num%i==0):  
        sum=sum+i  
if(sum==num):  
    print(num,"it is a perfect number")  
else:  
    print(num,"It is not a perfect number") 

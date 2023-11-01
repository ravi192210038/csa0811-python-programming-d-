num=int(input('Enter value of num: '))
Sum=0
temp = num
while temp>0:
   digit=temp%10
   Sum+=digit
   temp=temp//10
print("Sum of Digits:", Sum)

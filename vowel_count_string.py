s1 = input("enter a string:")
s2 = input("enter a string:")
n = int(input("n="))
output = ""
i = 0
j = 0
while i<len(s1) and j<len(s2):   
    output += s1[i:i+n] + s2[j:j+n]
    i += n
    j += n
output += s1[i:] + s2[j:]
print(output)

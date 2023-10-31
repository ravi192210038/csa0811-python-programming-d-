def countstrings(n,start):
    if n==0:
        return 1
    cnt=0
for i in range(start,5):
    cnt+=countstring(n-1,i)    
    return cnt
def countvowelstring(n):
    return countstrings(n,0)
n=int(input("n="))
print(countvowelstring(n))
 

def compositeCount(arr, n):
	Sum = 0
	max_val = max(arr)
	prime = [True for i in range(max_val + 1)]
	prime[0] = True
	prime[1] = True
	for p in range(2, max_val + 1):
		if p * p > max_val:
			break
		if (prime[p] == True):
			for i in range(p * 2, max_val + 1, p):
				prime[i] = False
				count = 0
	for i in range(n):
		if (prime[arr[i]] == False):
			count += 1
			Sum = Sum + arr[i]
	
	return count, Sum
arr = [15,18,27,16,23,21,19]
n = len(arr)
count, Sum = compositeCount(arr, n)
print("Count of Composite Numbers = ", count)
print("Sum of Composite Numbers = ", Sum)


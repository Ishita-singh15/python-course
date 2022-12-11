def rec(n):
	if n == 1:
		return n
	return n*rec(n-1)


n = int(input())
print("By Using Rec")
print(rec(n))
print("By using for loop")
fact = 1
for i in range(1,n+1):
	fact *= i

print(fact)

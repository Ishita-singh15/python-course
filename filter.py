a = [1,2,3,4,5,6,7,8,9]
b = [2,4,6,7,8]

I = filter(lambda x: x in a,b)

print(list(I))


# Odd Even

res = filter(lambda x: x%2 == 0,a)
print(list(res))
print(type(res))
res = filter(lambda x: x%2 != 0,a)
print(list(res))

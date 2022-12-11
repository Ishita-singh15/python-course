file = open("demo.txt",'w+')

st = "Welcome to python"

file.write(st)
file.seek(0)
print(file.read(6))

file.close()
file2 = open("demo.txt",'r')
file2.seek(5)
print(file2.read(7))


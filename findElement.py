myList = [1,2,3,4,5,6,7,8,9,0]
start = 0
end = len(myList)

no = int(input("Enter number: "))

def divnconq(no,lis,start,end):
	mid = end//2
	if no == lis[mid]:
		print(mid)
	elif no < lis[mid]:
		divnconq(no,lis,0,mid)
	elif no > lis[mid]:
		divnconq(no,lis,mid,end)

print(divnconq(no,myList,start,end))


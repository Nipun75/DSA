l=[7,42,11,133]
target=144
def two_pointer(target,l):
	l.sort()
	start=0
	end=len(l)-1
	while(start<end):
		if(l[start]+l[end]==target):
			return (l[start],l[end])
		elif(l[start]+l[end]>target):
			end-=1
		else:
			start+=1

a=two_pointer(target,l)
print(a)
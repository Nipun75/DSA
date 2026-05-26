l=[7,42,11,133]
target=144

def naive(l,target):
	for i in range(0,len(l)):
		for j in range(i+1,len(l)):
			if(l[i]+l[j]==target):
				return (l[i],l[j])
a=naive(l,target)
print(a)
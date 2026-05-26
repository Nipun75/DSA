def hashmap(l,target):
	hash={}
	for i in range(len(l)):
		hash.update({l[i]:i})
		
	for i in l:
		if(hash.get(target-i)):
			return (i,target-i)

l=[7,42,11,133]
target=144
a=hashmap(l,target)
print(a
l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]

print(list(zip(l1,l2)))

def addlist(list1,list2):
	sumlist = []
	for v1,v2 in zip(list1,list2):
		sumlist.append(v1+v2)
	return sumlist

'''
def addlist(list1,list2):
	sumlist = []
	for index in list(range(len(11)):
		summation = list1[index] + list2[index]
		sumlist.append(summation)
	return sumlist
'''

result = addlist(l1,l2)
print(result)



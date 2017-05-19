list1 = [2,3,1,4]
index = 0
for i in [0,1,2]:
	if list1[i] > list1[i+1]:
		t = list1[i+1]
		list1[i+1] = list1[i]
		list1[i] = t
	else:
		print("Swap not needed")
index = 0
for i in [0,1,2]:
	if list1[i] > list1[i+1]:
		t = list1[i+1]
		list1[i+1] = list1[i]
		list1[i] = t
	else:
		print("Swap not needed")
print(list1)

def bubblesort(list):
	for x in range(len(list)-1,0,-1):
		for i in range(x):
			if list[i]>list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1]= temp


true = 0
alist = []
while true == 0:
	str = raw_input()
	if str == "n":
		break
	else:
		alist.append(int(str))
bubblesort(alist)
print alist




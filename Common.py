print "Enter numbers into first list(n to stop):"
en = 0
a=[]
b=[]
while en == 0:
	str = raw_input()
	if str == 'n':
		break
	else:
		a.append(int(str))

		
print "Enter numbers into second list(n to stop):"
while en == 0:
	str = raw_input()
	if str == 'n':
		break
	else:
		b.append(int(str))

		
common = []
i = 0
while i<len(a):
	j = 0
	while j<len(b):
		if a[i]==b[j]:
			common.append(a[i])
		j=j+1
	i=i+1

	

common.sort();
k = 1
while k<len(common):
	if common[k]==common[k-1]:
		common.pop(k)
	k=k+1
print common

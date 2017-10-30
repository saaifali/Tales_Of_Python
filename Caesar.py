def CaesarEncrypt(str,key):
	ls = list(str)
	cipher = []
	for x in ls:
		temp = ''
		if x!=' ':
			temp2 = ord(x)+key
			k=0
			
			temp = chr(temp2)
			if x.islower():
				if temp2>ord('z'):
					diff = ord('z')-ord(x)
					while temp2>ord('z'):
						temp2=temp2-1
						k=k+1
					val = ord('a')-diff
					temp = chr((val+k))
			else:
				if temp2>ord('Z'):
					diff = ord('Z')-ord(x)
					while temp2>ord('Z'):
						temp2-=1
						k=k+1
					val = ord('A')-diff
					temp = chr((val+k))
		else:
			temp = x
		cipher.append(temp)
	CT = ''.join(cipher)
	return CT
	
def CaesarDecrypt(str,key):
	ls = list(str)
	plain = []
	for x in ls:
		temp = ''
		if x!=' ':
			temp2 = ord(x)-key
			k=0
			temp = chr(temp2)
			if x.islower():
				if temp2<ord('a'):
					diff = ord(x)-ord('a')
					while temp2<ord('a'):
						temp2=temp2+1
						k=k+1
					val = ord('z')
					temp = chr((val-k+diff))
			else:
				if temp2<ord('A'):
					diff = ord(x)-ord('A')
					while temp2<ord('A'):
						temp2+=1
						k=k+1
					val = ord('Z')
					temp = chr((val-k+diff))
		else:
			temp = x
		plain.append(temp)
	CT = ''.join(plain)
	return CT
	
	

PT = raw_input("Enter the Plain text : ")
key = input("Enter Key : ")
print "Cipher text = ",CaesarEncrypt(PT,key)
CT = raw_input("Enter Cipher Text : ")
key = input("Enter key : ")
print "Plain Text = ",CaesarDecrypt(CT,key)
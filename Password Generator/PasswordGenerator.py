import itertools
import sys
import os

def permute(rest,start=''):
	res = []
	if len(rest)<=1:
		res+= [start + rest]
	else:
		for i,c in enumerate(rest):
			s = rest[:i]+rest[i+1:]
			for perm in permute(s,c):
				res+=[start + perm]
	return res
	
def permute2(s):
	res = []
	if len(s)==1:
		return [s]
	else:
		for i,c in enumerate(s):
			for perm in permute2(s[:i]+s[i+1:]):
				res+= [c+perm]
	return res
	
def permute3(s,length):
	return [''.join(x) for x in itertools.permutations(s,length)]
	
def display(passwords):
	try:
		print ("ALL PASSWORDS FOR GIVEN SEQUENCE")
		print ('-'*60)
		print (passwords)
	except KeyboardInterrupt:
		print ("Display Stopped!")
	
def lib_optimize(filename):
	print "Library optimization initiated...\n"
	keys = []
	try:
		f = open(filename,"r")
	except IOError:
		print "File doesn't exist!"
		return
	for key in f:
		keys.append(key)
	keys.sort()
	before = len(keys)
	keys = list(set(keys))
	after = len(keys)
	f.close()
	f = open("PasswordLibrary.txt","w")
	for x in keys:
		f.write(x)
	f.close()
	print "Library optimization complete...\n%d Duplicate passwords removed!"%(before-after)
		

print '-'*60
print """Welcome to Password Generator!"""
print '-'*60
ch = 0
passwords = []
s = raw_input("Enter the sequence : ")
while True:
	raw_input("Press Enter to continue...")
	os.system("cls")
	print "Create Password:\n	1. Of same length.\n	2. Of upto same length\n	3. Of fixed length"
	print "4. Add to Library(Adds the last set of passwords generated!)\n5. Display Password Library\n6. Optimize Library\n7. Enter new sequence\nPress any other key to Exit."
	ch = input()
	if ch==1:
		passwords = permute2(s)#,len(s))
		display(passwords)
		
	elif ch==2:
		p = []
		for i in range(1,len(s)+1):
			p.extend(permute3(s,i))
		passwords = p
		display(passwords)
		
	elif ch==3:
		length = input("Enter fixed length value(< = %d) : "%len(s))
		passwords = permute3(s,length)
		display(passwords)
		
	elif ch==4:
		f = open("PasswordLibrary.txt","a")
		for x in passwords:
			f.write(x+"\n")
		f.close()
		print "Library updated!"
	elif ch==5:
		try:
			f = open("PasswordLibrary.txt","r")
		except IOError:
			print "File doesn't exist!"
			continue
		os.system("PasswordLibrary.txt")
		#print "COMPLETE LIBRARY"
		#print '-'*60
		#print f.read()
		f.close()
	elif ch==6:
		lib_optimize("PasswordLibrary.txt")
	elif ch ==7:
		s = raw_input("Enter new sequence : ")
	else:
		print "EXITED SUCCESSFULLY..."
		sys.exit()
	
	
		

def tables(n=1):		#defining a function to print n th table
	for i in range (1,21):
		print i,"*",n,"=",i*n
	print "\n\n\n"

s=input("enter the N th number:")
for i in range(1,s+1):
    tables(s)

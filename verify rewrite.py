'''f1=open("bhavanee.txt","r")
f2=open("shortyy.txt","a")
for data in f1:
    f2.write(data)'''

# open both files
with open('bhavanee.txt','r') as firstfile, open('shortyy.txt','w') as secondfile:
	
	# read content from first file
	for line in firstfile:
			
			# write content to second file
			secondfile.write(line)


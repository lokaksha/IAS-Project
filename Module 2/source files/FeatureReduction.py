file=open("myfile.csv","r")
b=[]
for x in file:
	(a)=x.split(",")
	b.append(a)

for i in range(50):
	del b[i][26767]

n=26766
i=0
while i < n:
	count=0
	for j in range(50):
		if b[j][i]=="0":
			count+=1
	print i,n,count
	if count>40:
		for j in range(50):
			del b[j][i]
		i-=1
		n-=1
	i+=1

print n

with open('new.csv','w') as f:
    for sublist in b:
        for item in sublist:
            f.write(str(item) + ',')
        f.write('\n')
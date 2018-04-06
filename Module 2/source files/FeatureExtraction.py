from sklearn.feature_extraction.text import CountVectorizer
import numpy
import os
import csv

x=os.listdir("Malware")
data=[]
count=0
for i in x:
	count+=1
	file=open("Malware/"+i,"r")
	s=""
	for l in file:
		s=s+l[:l.find("//")]
	s=''.join([i for i in s if not i.isdigit()])
	data.append(s)

mal=count

x=os.listdir("Benign")
for i in x:
	count+=1
	file=open("Benign/"+i,"r")
	s=""
	for l in file:
		s=s+l[:l.find("//")]
	s=''.join([i for i in s if not i.isdigit()])
	data.append(s)

vectorizer = CountVectorizer()
a=vectorizer.fit_transform(data).todense()
zx=[]
for j in range(count):
	zx.append(numpy.array(a)[j].tolist())
	if j < mal:
		zx[j].append(0)
	else:
		zx[j].append(1)

#t=0
#for j in zx[0]:
	t+=1

#for j in range(count):
#	print zx[j][t-1]

# print( vectorizer.vocabulary_ )
# with open("output.csv","wb") as f:
# 	writer=csv.writer(f)
# 	writer.writerows(zx)

with open('myfile.csv','w') as f:
    for sublist in zx:
        for item in sublist:
            f.write(str(item) + ',')
        f.write('\n')

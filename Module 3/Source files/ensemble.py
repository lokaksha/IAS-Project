import numpy as np

file=open("new.csv","r")
b=[]
c=[]
i=0
for x in file:
	(a)=x.split(",")
	b.append(a)
	i+=1
	if b[i-1][-1] == "1\n":
		c.append(1)
		b[i-1].pop()
	else:
		c.append(0)
		b[i-1].pop()

train=[]
for i in range(100):
	if i%10 != 0:
		a=[]
		for j in range(3121):
			a.append(float(b[i][j]))
		train.append(a)

test=[]
for i in range(100):
	if i%10 == 0:
		a=[]
		for j in range(3121):
			a.append(float(b[i][j]))
		test.append(a)

train_class=[]
for i in range(100):
	if i%10 != 0:
		train_class.append(c[i])

test_class=[]
for i in range(100):
	if i%10 == 0:
		test_class.append(c[i])
print test_class
X = np.array(train)
Y = np.array(train_class)

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

temp1 = GaussianNB()
temp1.fit(X, Y)
ans1=list(temp1.predict(test))

temp2 = SVC()
temp2.fit(X, Y) 
ans2=list(temp2.predict(test))

temp3 = RandomForestClassifier(max_depth=2, random_state=0)
temp3.fit(X, Y)
ans3=list(temp3.predict(test))

print ans1
print ans2
print ans3

ans=[]
for i in range(10):
	count=ans1[i]+ans2[i]+ans3[i]
	if count > 1:
		ans.append(1)
	else:
		ans.append(0)
print ans
acc=0.0
for i in range(10):
	if ans[i]==test_class[i]:
		acc+=1
acc=acc*100/10
print "Accuracy = "+str(acc)+"%"
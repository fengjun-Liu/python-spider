alist=list(map(int,input().split()))
one=[]
two=[]
middle=int(len(alist)/2)
for i in range(0,middle):
	one.append(alist[i])
	two.append(alist[i+middle])
result={"1":one,"2":two}
print(result)
alist=list(map(int,input().split()))
lens=len(alist)
blist=[]
for i in range(1,lens+1):
    blist.append(alist[0-i])
print(blist)
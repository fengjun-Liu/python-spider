s=str(input())
n=int(input())
length=len(s)
left=s[0:n:1]
right=s[n:length:1]
s=right+left
print(s)

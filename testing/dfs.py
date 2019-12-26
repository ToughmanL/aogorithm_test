
def dfs(a,n,k):
    a=2*a+k
    f.append(k)
    if a==n:
        return "".join(f)
    elif a>n:
        a=(a-k)/2
        f.pop()
        return
    else:
        dfs(a,n,1)
        dfs(a,n,2)



n=input()
f=[]
a=0
k=1
re=dfs(a,n,k)
print(re)

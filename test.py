a=[1,3,5,7]
n=10

l=0
u=min(a)*n

for i in range(u):
    sum=0
    mid=(l+u)//2
    for j in range(len(a)):
        sum= sum + (mid//a[j])
    if sum<n:
        l=mid+1

    else:
        u=mid

    if l==u:
        break
print(l)
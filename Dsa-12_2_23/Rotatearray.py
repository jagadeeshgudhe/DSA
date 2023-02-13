l=list(map(int,input().split()))
r=int(input())
r=r%len(l)
l=l[-r:]+l[:-r]
print(l)

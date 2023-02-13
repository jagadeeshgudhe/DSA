l=list(map(int,input().split()))
d=[]
for i in range(len(l)):
      if l.count(l[i])>1 and l[i] not in d:
            d.append(l[i])
print(d)

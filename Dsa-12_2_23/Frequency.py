l=list(map(int,input().split()))
f={}
for i in l:
      if i in f:
            f[i]+=1
      else:
            f[i]=1
      hf=max(f.values())
      mf=[key for key,value in f.items() if value==hf]
print(mf[0])


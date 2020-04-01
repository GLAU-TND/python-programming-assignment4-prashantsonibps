m=eval(input())
n=int(input())
new=[]
for i in m:
  if i[0] not in new:
    new.append(i[0])
dct={}
for i in new:
  dct[i]=[]
for i in dct:
  for j in m:
    if i==j[0]:
      dct[i].append(j[m])
dct2={}
r=0
for i in range(len(dct)):
  for j in range(i+1,len(dct)):
    res= len(set(dct[list(dct)[i]]) & set(dct[list(dct)[j]]))/float(len(set(dct[list(dct)(i)]) | set(dct[list(dct)[j]])))*100
    if 1!=j:
      dct2[r]=[round(res,2),list(dct)[j],list(dct)[i]]
      r=r+1
p=list(dct2.values())
for k in range(len(p)):
  if p[k][1]>p[k][2]:
    c=p[k][1]
    p[k][1]=p[k][2]
    p[k][2]=c

p.sort(key = lambda p: p[0],reverse=True)
m=[]
for q in range(n):
  m+=[(p[q][1],p[q][2])]
print(m)
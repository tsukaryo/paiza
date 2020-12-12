n=int(input())

lists = list(map(int, input().split()))
#連続何日間？
o=[]


count=0
for l in range(len(lists)-6):
    for i in range(0,7):
        if(lists[l+i]==0):
            count=count+1
    if(count>=2):
        o.append(1)
    else:
        o.append(0)
    count=0
    #print(l)
w=[]
ma=0
c=0
#print(o)
for t in o:
    if(t==1):
        c=c+1
    else:
        w.append(c)
        c=0
    
w.append(c)
#print(w)
ma=max(w)
ans=0
if(ma!=0):
    ans=ma+7-1
else:
    ans=0
print(ans)
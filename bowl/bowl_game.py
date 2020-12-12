a=0
b=0
n=0
a,b,n=input().split()
a=int(a)
b=int(b)
n=int(n)
#print(a,b,n)
i=0
#今なんフレーム目？
f=1
#前スペア？
spare=0
#前ストライク？
strike=0
num=[]
#それぞれ投げた時の倒れたピンの数
lis=[]
lists = list(map(str, input().split()))
for li in lists:
    if(li=='G'):
        lis.append('0')
    else:
        lis.append(li)

lis = [int(s) for s in lis]
t=0
for i in range(0,len(lis)-2):
    
    if(lis[t]!=b):
        s=lis[t]+lis[t+1]

        if(s==b):
            s=s+lis[t+2]
        t=t+2     
        
    else:
        s=lis[t]+lis[t+1]+lis[t+2]
        t=t+1
    
    num.append(s)
    if(t+3>=len(lis)):
        break
    
if(lis[t]!=b):
    s=lis[t]+lis[t+1]
    if(s==b):
        s=s+2*lis[t+2]
else:
    s=lis[t]+2*(lis[t+1]+lis[t+2])

num.append(s)    






print(sum(num))
    


print(num)
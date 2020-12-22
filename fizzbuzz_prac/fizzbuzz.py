f = open('input.txt', 'r')
num=[]
str=[]
a=0
n=''
s=''
i=0
datalist=f.readlines()

for data in datalist:
    print(data)
    for d in data:
        if d!=':' and a==0:
            n=n+d
        elif d==':' and a==0:
            num.append(int(n))
            a=1
            n=''
        elif a==1:
            s=s+d
        
    str.append(s)
    s=''
    
    a=0
for nu in num:
    if(int(n)%nu==0):
        print(nu)
        i=i+1
print(int(n))
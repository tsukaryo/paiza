d,n = list(map(int, input().split()))
a=[]
for i in range(n):
    a.append(int(input()))

now_position=d
w=0
rooting=[]

for i in range(n*n+1):
    now_position=d
    root=bin(i)[2:]
    for t in range(len(bin(i)[2:]),n):
        root='0'+root
    
    for j in range(n):
        if root[j]=="0":
            now_position=now_position-a[j]
            
            if now_position < 0:
                rooting=[]
                break
            else:
                rooting.append('L')
        else:
            now_position=now_position+a[j]
            
            if now_position > 2*d:
                rooting=[]
                break
            else:
                rooting.append('R')


    if rooting!=[] and j==n-1:
        w=1
        print(''.join(rooting))
        
        break
    

            

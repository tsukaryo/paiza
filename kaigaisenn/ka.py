h,w = list(map(int, input().split()))
s=[]

for i in range(h):
    s.append(list(map(str, input().split())))

print(s)
#面積　
t=[]
#周りwと面積p
w=0
p=0
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            continue
        else:
            while True:
                ori_i=i
                ori_j=j
                if s[i][j+1]=='#' and j!=w:
                    w=w+1
                    p=p+1
                    s[i][j]='.'
                    j=j+1
                    continue
                elif s[i+1][j]=='#' and i!=h:
                    w=w+1
                    p=p+1
                    s[i][j]='.'
                    i=i+1
                    continue
                elif s[i][j-1]=='#' and j!=0:
                    w=w+1
                    p=p+1
                    s[i][j]='.'
                    j=j-1
                    continue
                elif s[i-1][j]=='#' and i!=0:
                    w=w+1
                    p=p+1
                    s[i][j]='.'
                    i=i-1
                    continue
                else:
                    if (c>=3 and (i+1 == ori_i or i-1 == ori_i or i == ori_i) and (j+1 == ori_j or j-1 == ori_j or j == ori_j)):
                        #一周していることになる
                    else:
                        #一周できていないことになる
                        p=w*2+2
                        






    
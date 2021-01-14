import numpy as np
n,k = list(map(int, input().split()))


d=[i for i in range(2*n)]
def comb(n, m):
    if m == 1:
        for i in range(n):
            yield [i]
    else:
        # n個からm-1個取り出す組み合わせを求め、その末尾にm個目の選択要素をくっつける
        for c in comb(n, m - 1):
            for i in range(c[-1] + 1, n):
                yield c + [i]

count=0

for c in comb(2*n, n):
    e=list(set(d) - set(c))
    a=np.array(c)
    b=np.array(e)
    if abs(a-b).sum()<=k:
        count=count+1

print(count)


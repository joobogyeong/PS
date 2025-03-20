T=int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(len(A)):
    T-=A[i]
    if T<=0:
        break
    else:
        print(A[i])

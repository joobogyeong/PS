A=[1, -1, 3, -4, 5, -4, 6, -2]
S=len(A)
max_sum=0
for i in range(S):
    for j in range(S):
        if i<j :
            for k in range(i, j):#O(n^2)
                sum+=A[k]
            if max_sum<sum:#O(n)
                max_sum=sum
        sum=0
print(max_sum)
#O(n^3)

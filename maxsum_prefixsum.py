A = [1, -1, 3, -4, 5, -4, 6, -2]
S = len(A)

prefix_sum = [0] * (S + 1)
for i in range(1, S + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

max_sum = float('-inf')
for i in range(S):
    for j in range(i + 1, S + 1):
        current_sum = prefix_sum[j] - prefix_sum[i]
        max_sum = max(max_sum, current_sum)

print(max_sum)
#O(n^2)
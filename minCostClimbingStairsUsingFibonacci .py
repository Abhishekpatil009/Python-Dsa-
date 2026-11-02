def minCostofClimbingStairsfibonacci(N, A, B):
# Step 1: Generate Fibonacci jump lengths
fib = [1, 2]

```
while fib[-1] + fib[-2] <= N - 1:
    fib.append(fib[-1] + fib[-2])

# Step 2: Initialize DP array
dp = [float('inf')] * (N + 1)

# Starting position has zero cost
dp[1] = 0

# Step 3: Calculate minimum cost to reach each step
for i in range(1, N + 1):
    if dp[i] == float('inf'):
        continue

    # Try every Fibonacci jump
    for k in fib:
        next_step = i + k

        if next_step <= N:
            jump_cost = A + B * k

            # Update only if we find a cheaper route
            dp[next_step] = min(
                dp[next_step],
                dp[i] + jump_cost
            )

# Step 4: Return minimum cost to reach step N
return dp[N]
```

N, A, B = map(int, input().split())
print(minCostofClimbingStairsfibonacci(N, A, B))





# def minCostofClimbingStairsfibonacci(N, A, B):

#     fib=[1,2]
#     while fib[-1]+fib[-2]<=N-1:
#         fib.append(fib[-1]+fib[-2])
    
#     dp=[float('inf')] * (N+1)

#     dp[1]=0

#     for i in range(1,N+1):
#         if dp[i]==float('inf'):
#             continue

#         for k in  fib:
#             next_step=i+k
#             if next_step <=N:
#                 jump_cost=A+B*k
#                 dp[next_step]=min(dp[next_step],jump_cost+dp[i])

#     return dp[N]            




# N,A,B=map(int, input().split())
# print(minCostofClimbingStairsfibonacci(N,A,B))
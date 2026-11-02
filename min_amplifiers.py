
def upper_bound(arr, target, start):
    left = start
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def min_amplifiers(posts, r, K):

    n = len(posts)

    INF = float('inf')

    # DP table
    # dp[i][k] = minimum amplifiers needed
    # to cover first i posts using exactly k super amplifiers

    dp = [[INF] * (K + 1) for _ in range(n + 1)]

    # Initially, zero posts covered with zero amplifiers
    dp[0][0] = 0

    # Traverse all DP states
    for i in range(n):

        for k in range(K + 1):

            # Skip if this state is unreachable
            if dp[i][k] == INF:
                continue

            # OPTION 1: Use normal amplifier

            normal_limit = posts[i] + 2 * r

            next_normal = upper_bound(
                posts, normal_limit, i
            )

            dp[next_normal][k] = min(
                dp[next_normal][k],
                dp[i][k] + 1
            )

            # OPTION 2: Use super amplifier

            if k < K:

                super_limit = posts[i] + 4 * r

                next_super = upper_bound(
                    posts, super_limit, i
                )

                dp[next_super][k + 1] = min(
                    dp[next_super][k + 1],
                    dp[i][k] + 1
                )

    # Minimum amplifiers after covering all posts
    return min(dp[n])


# Input
posts = [1, 3, 5, 7, 10]
r = 2
K = 1

# Function call
answer = min_amplifiers(posts, r, K)

# Output
print("Minimum amplifiers:", answer)

def lcs(a, b):
    dp = []
    for i in range(len(a)+1):
        dp.append([[]] * (len(b)+1))
    for i in range(len(a)):
        for j in range(len(b)):
            print(a[i], b[j])
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j].copy() + [a[i]]
            else:
                if len(dp[i][j+1]) > len(dp[i+1][j]):
                    dp[i+1][j+1] = dp[i][j+1].copy()
                else:
                    dp[i+1][j+1] = dp[i+1][j].copy()
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            print(dp[i][j])


if __name__ == '__main__':
    a = [1, 5, 2, 6, 8, 7]
    b = [1, 2, 3, 5, 6, 9, 8, 4]

    lcs(a, b)
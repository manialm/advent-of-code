with open('input.txt') as f:
    s = f.read().split(',')

arr = [int(i) for i in s]
dp = [0]*9

for i in arr:
    dp[i] += 1
    
for _ in range(256):
    
    new_dp = dp[:]
    for i in range(9):
        if i == 8:
            new_dp[8] = dp[0]
        elif i == 6:
            new_dp[6] = dp[7] + dp[0]
        else:
            new_dp[i] = dp[i+1]
    
    dp = new_dp[:]

print(sum(dp))
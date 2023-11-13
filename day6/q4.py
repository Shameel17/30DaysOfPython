a = int(input())
b = int(input())
result = []
ans = 0
for i in range(1000, 2001):
    if i % a == 0 and i % b == 0:
        result.append(i)
for j in range(len(result)):
    ans = ans + result[j]
print(ans)

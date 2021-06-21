a,r,d,n = map(int, input().split())

result = 0
for i in range(n-1):
  result += r**i

print(a*r**(n-1)+d*result)
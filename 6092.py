n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

d = [0] * 24

for i in range(n):
  d[a[i]] += 1

for n in d[1:]:
  print(n, end=" ")
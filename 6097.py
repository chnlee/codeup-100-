a,b = map(int, input().split())

lst = [[0]*b for i in range(a)]

n = int(input())

for m in range(n):
  l,d,x,y = map(int, input().split())
  if d == 0:
    for j in range(l):
      lst[x-1][y+j-1] = 1
  elif d == 1:
    for k in range(l):
      lst[x+k-1][y-1] = 1

for o in range(a):
  for p in range(b):
    print(lst[o][p], end =" ")
  print()
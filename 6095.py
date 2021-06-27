#리스트 컴프리헨션
#case 1
d = [[0 for j in range(20)] for i in range(20)]
#case 2 
d = [[0] * 20 for i in range(20)]

n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  d[a][b] = 1

for i in range(1,20):
  for j in range(1, 20):
    print(d[i][j], end=" ")
  print()



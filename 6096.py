# 2차원 리스트 입력 받는 좋은 방법
# LIST COMPREHENSHION
d = [[int(x) for x in input().split()] for y in range(19)]

n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  for i in range(19):
    if d[i][b-1] == 0:
      d[i][b-1] = 1
    else:
      d[i][b-1] = 0
  for j in range(19):
    if d[a-1][j] == 0:
      d[a-1][j] = 1
    else:
      d[a-1][j] = 0
for i in range(19):
  for j in range(19):
    print(d[i][j], end=" ")
  print()



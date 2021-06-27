d = [[int(x) for x in input().split()] for i in range(10)]

i = 1
j = 1
while(i<10):
  if d[i][j] == 0:
    d[i][j] = 9
    j += 1
  elif d[i][j] == 1:
    i += 1
    j -= 1
  else:
    d[i][j] = 9
    break

for i in range(10):
  for j in range(10):
    print(d[i][j], end =" ")
  print()
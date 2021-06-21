num = int(input())

result = 0
p = 1
while True:
  result +=p
  p+=1
  if result >= num:
    break
print(result)
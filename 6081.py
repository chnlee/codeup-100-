A = input()
A = int(A,16)
for i in range(1,16):
  print('%X'%A,'*%X'%i,'=%X'%(A*i),sep="")
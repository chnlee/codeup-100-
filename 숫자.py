import random
secretLen = 4

# 비밀 숫자 생성
secretList = random.sample(range(10), secretLen) # 0~9 중 3개 랜덤 선택
secret = ''
for i in range(secretLen):
 secret += str(secretList[i]) # 문자열로 변환

for chance in range(10, 0, -1): # 10번의 기회
 # 추론 숫자 입력
 while True:
  guess = input(("You have %d chance(s). " %chance) + "Guess my four-digit number: ")
  if len(guess) == secretLen and guess.isdigit():
    break
 # 추론 숫자 분석
 strike = 0 # 스트라이크 초기화
 ball = 0 # 볼 초기화
 for i in range(secretLen):
  if secret[i] == guess[i]:
    strike += 1 # 스트라이크 증가
  elif secret[i] in guess:
    ball += 1 # 볼 증가
 # 분석 결과 출력
 if strike == secretLen:
   print('You guessed my number!!')
   break
 if strike > 0:
   if ball > 0:
     print("%d strike(s) and %d ball(s)\n" % (strike, ball))
   else:
     print("%d strike(s)\n" % strike)
 else:
   if ball > 0:
     print ("%d ball(s)\n" % ball)
   else:
     print ("Out\n")
else:
  print ('You failed to guess my number..')


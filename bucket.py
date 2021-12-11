# 1. 장바구니 기능 구현
# 각각 함수의 기능에 알맞게 구현하세요.
shopping_bag = [] # 장바구니 리스트 이름임, 바꾸지 말 것 
selling_list = [1,2,3,4]


def bag_insert():         
   # 함수정의     
  b = int(input("구매할 물건을 선택하세요:"))
  if b not in shopping_bag:
    if b not in selling_list:
      print('잘못된 입력')
    else: 
      shopping_bag.append(b)
  else: 
    print('장바구니에 이미 있는 물건입니다.')
         

def bag_del():
         # 함수정의     
    if len(shopping_bag) > 0:
      c = int(input("삭제할 물건 번호를 입력하세요:"))
      if c in shopping_bag:
        shopping_bag.remove(c)
        print("삭제 완료")
      else:
        print("장바구니에 없습니다.")
    else:
      print('장바구니가 비어있습니다.')

def bag_print():
         # 함수정의
    if 1 in shopping_bag:
        print('과자')
    if 2 in shopping_bag:
        print('물')   
    if 3 in shopping_bag:
        print('라면')
    if 4 in shopping_bag:
        print('쌀')       

def bag_buy():
         # 함수정의
         total = sum(shopping_bag) * 1000
         print("======================")
         print('<구매한 목록>')
         bag_print()
         print("구매 금액: "+ str(total))


while True:
    a = int(input("<장바구니 기능을 선택하세요>>>>>>"))
    
    if a == 1:
        bag_insert()
    elif a == 2:
        bag_del()
    elif a == 3:
        bag_print() 
    elif a == 4:
        bag_buy()
        break
        
    else:
        print('잘못된 입력')

        


# 2. 함수 호출 부분 구현 (반복문 삽입)
# 아래 주석 부분을 참고하여 코드를 작성하세요. 
'''
While 참/거짓:
    if 1인 경우
        bag_insert()
    elif 2인 경우
        bag_del()
    elif 3인 경우
        bag_print()
    elif 4인 경우
        bag_buy()
        break
    else:
''' 
      

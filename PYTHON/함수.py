# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print(f"입금이 완료되었습니다. 잔액은 {balance + money}원입니다.")
#     return balance + money # 반환 순서 balance = 0 원인 deposit(0, 1000) 을 deposit 함수에 대입 후 balance + money 를 실행한 값을 반환하는것

# def withdraw(balance, money) : # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money}원입니다")
#         return balance - money
#     else:
#         print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원입니다")
#         return balance

# def withdraw_night(balance, money) : # 저녁에 출금 수수료 
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000) # 출금 안됨
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print(f"수수료 {commission} 원이며, 잔액은 {balance}원 입니다")

# 기본값
# def profile(name, age, main_lang):
#     print(f"이름 : {name}\t 나이 : {age}\t 사용 언어 : {main_lang}")

# profile("유재석", 20, "python")
# profile("김태호", 25, "Java")

## 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age = 17, main_lang = "Python"):
#     print(f"이름 : {name}\t 나이 : {age}\t 사용 언어 : {main_lang}")

# profile("유재석")
# profile("김태호")


def profile(name, age, *language): # lang1, lang2, lang3 ...
     print(f"이름 : {name}\t 나이 : {age}" , end =" ")
     for lang in language:
          print(lang, end =" ")
     print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "kotlin", "Swift")
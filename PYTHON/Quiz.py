## 1 

# 변수명 : station

# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력

# 출력 문장 : XX 행 열차가 들어오고 있습니다.

# station = []
# station.append("사당")
# station.append("신도림")
# station.append("인천공항")

# for i in station:
#     print(f"{i}행 열차가 들어오고 있습니다.")


## 2 
# from random import *

# Days = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(Days)+ "일로 선정되었습니다.")


## 3
# url = "http://naver.com"

# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f'{url}의 비밀번호는 {password}입니다 ')

## 4

# 댓글 작성자들 중에 추첨을 통해 1명 치킨, 3명 커피 쿠폰

# 조건1 : 편의상 댓글은 20명 작성 아이디 1~20 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

## 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# from random import *
# list = [i for i in range(1, 21)]
# print(list)
# shuffle(list)
# print(list)

# winners = sample(list, 4) # 4명 중 1명은 치킨

# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print("-- 축하합니다 --")

## 5

# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램 작성

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭

# (출력문 예제)
# [0] 1 번째 손님 (소요시간 : 15분)
# [ ]  2 번째 손님 (소요시간 : 50분)
# 총 탑승 승객 : 2분

# from random import *

# cnt = 0 # 총 탑승 승객 수 초기화

# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= i <= 15:
#         print(f"[O] {i} 번째 손님 (소요시간 : {time}분)")
#         cnt += 1
#     else:
#         print(f"[] {i} 번째 손님 (소요시간 : {time}분)")
# print(f"총 탑승 승객 : {cnt}")

## 6 

# 표준 체중을 구하는 프로그램 작성
# 표준 체중 : 남 : 키(m) X 키(m) X 22, 여 : 키(m) X 키(m) X 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산 
  ### 함수명 : std_weight
  ### 전달값 : 키(height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째 자리까지 표시

# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
    

## 7

# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# for X in range(1,51):
#     with open(f"{str(X)}주차.txt", 'w', encoding = "utf-8") as report:
#         report.write(f"- {str(X)} 주차 주간보고 -")
#         report.write("\n부서 : ")
#         report.write("\n이름 : ")
#         report.write("\n업무 요약 : ")
        
    
## 8

# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# 출력 예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/ 50 2000년

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\
#               ,self.price, self.completion_year)
        
        


# Apart = []
# Apart1 = House("강남", "아파트", "매매", "10억", "2010년")
# Apart2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# Apart3 = House("송파", "빌라", "월세", "500 / 50", "2000년")

# Apart.append(Apart1)
# Apart.append(Apart2)
# Apart.append(Apart3)

# print(f"총 {len(Apart)}대의 매물이 있습니다.")

# for house in Apart:
#     house.show_detail()


## 9

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
# 출력 메시지 : "잘못된 값을 입력하였습니다"

# 조건2 : 대기손님이 주문할 수 있는 치킨량 10마리 한정
# 출력 메시지 : "재고가 소진되어 더 이상 주문 받지 않습니다"

class SoldOutError(Exception):
    pass
    

chicken = 10
waiting = 1
while(True):
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까??"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print(f"[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문 받지 않습니다")
        break
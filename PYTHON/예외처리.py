# try:
#     print("나누기 전용 계산기")
#     nums =[]
#     nums.append(int(input("첫 번째 숫자 :")))
#     nums.append(int(input("두 번째 숫자 :")))
#     # nums.append(int(nums[0]/ nums[1]))
#     print(f"{nums[0]} / {nums[1]} = {nums[2]}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러 발생")
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자 입력: "))
#     num2 = int(input("첫 번째 숫자 입력: "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError  ##  raise 사용 
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값 입력 한 자리만 입력 ")

class BigNum(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 입력: "))
    num2 = int(input("첫 번째 숫자 입력: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNum(f"입력값 : {num1}, {num2}")  ##  raise 사용 
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값 입력 한 자리만 입력 ")
except BigNum as err:
    print("에러 발생")
    print(err)
finally: #무조건 출력
    print("계산기를 이용해주셔서 감사합니다") 
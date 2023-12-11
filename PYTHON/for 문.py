# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_num in [1,2,3,4]:
#     print(f"대기번호 : {waiting_num}")

# for waiting_num in range(1,5):
#         print(f"대기번호 : {waiting_num}")

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print(f"{customer}, 커피가 준비되었습니다.")

## for 문 1줄로
# students = [1,2,3,4,5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# 학생 이름 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

students = ["Iron man", "Thor", "I am groot"]
students =[i.upper() for i in students]
print(students)
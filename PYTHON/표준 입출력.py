# print("Python", "Java")
# print("Python" + "Java")
# print("Python", "Java", sep = " , ") # 사이에 , 추가
# print("Python", "Java", sep = " VS ") # 사이에 VS 추가
# print("Python", "Java", sep = " , ", end = "?")  # 뒷 문장과 한 줄로 표현
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file = sys.stdout) # 표준 출력
# print("python", "java", file = sys.stderr) # 표준 에러

# 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(8), sep = ":") # ljust = 왼쪽정렬, rjust = 오른쪽 정렬


# 은행 대기순번표

#001, 002, 003 ...

# for num in range(1,21):
#     # print("대기번호 : " + str(num))
#     print("대기번호 : " + str(num).zfill(3))  # 값이 없는 것을 0으로 채워주라 3칸중에

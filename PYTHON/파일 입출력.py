# A.txt 파일 쓰기
# score_file = open("A.txt", "w", encoding = "utf-8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# A.txt 파일 추가
# score_file = open("A.txt", "a", encoding = "utf-8")  # append
# score_file.write("과학 : 80")  # write로 작성시 줄 바꿈 없음
# score_file.write("\n코딩 : 100") #\n 해줘야함
# score_file.close()

# A.txt 파일 읽기
# score_file = open("A.txt", "r", encoding = "utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("A.txt", "r", encoding = "utf-8")
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# score_file = open("A.txt", "r", encoding = "utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

# score_file = open("A.txt", "r", encoding = "utf-8")
# lines = score_file.readlines()  # list 형태로 저장

# for line in lines:
#     print(line, end = "")
# score_file.close()

## pickle

# import pickle
# # profile_file = open("profile.pickle", "wb") # pickle은 w뒤에 binary 써줘야하고 encoding 쓸 필요 없음
# # profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # profile.file.close()

# profile_file = open("profile.pickle", "rb") # pickle은 w뒤에 binary 써줘야하고 encoding 쓸 필요 없음
# profile = profile.load(profile_file)  # file에 있는 정보를 profile에서 불러옴
# print(profile)
# profile_file.close()

# with 는 close 해줄 필요 없음
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding ="utf-8")  as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding ="utf-8")  as study_file:
    print(study_file.read())
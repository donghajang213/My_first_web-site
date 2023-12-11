# 딕셔너리 {}

# cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet[100])

# # print(cabinet.get(3))
# # # print(cabinet[5]) ## keyError:5 출력
# # print(cabinet.get(5)) ## None 출력
# # print(cabinet.get(5, "사용가능")) ## 사용가능 출력
# # print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3" : "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"]  = "김종국" # A-3 덮어씌움 
# cabinet["C-20"] = "조세호"  
# print(cabinet)

# # 간 손님

# del cabinet["A-3"]
# print(cabinet)

# # key 출력
# print(cabinet.keys())

# # value 출력
# print(cabinet.values())

# # 전체 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)
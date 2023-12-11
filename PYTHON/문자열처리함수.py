python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자가 맞는지
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 두 번째 n 찾기위한 식
print(index)

print(python.find("n"))
print(python.count("n"))
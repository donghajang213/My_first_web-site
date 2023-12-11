absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): #1 ~ 10
    if student in absent:
        continue  # absent 빼고 계속 진행
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break # 7에서 바로 멈춤
    print(f"{student}, 책을 읽어봐")
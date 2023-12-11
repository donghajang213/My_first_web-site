## while
customer = "토르"
idx = 5
while idx >= 1:
    print(f"{customer} 고객님 커피가 준비 되었습니다. {idx}번 남으셨어요!")
    idx -= 1
    if idx == 0:
        print(f"{customer} 고객님 쿠폰이 모두 소진되셨습니다!")
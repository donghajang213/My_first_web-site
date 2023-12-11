gun = 10  # 전역 공간

def checkpoint(soldiers): 
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f"[함수 내] 남은 총: {gun}")

print(f"전체 총 : {gun}")
checkpoint(2) # 2명이 경계 근무 나감
print(f"남은 총 : {gun}")
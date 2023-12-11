print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)
print(5 % 3) # 나머지
print(6 // 2)  # 몫
print(2**3) # print 2 ^  3 # 제곱
print(3>=5) # False
print(3 == 3) ## 정수만 가능 Float은 안됨 뒤에 소수점으로 인해 
print(1 != 3) # True  ! = not
print((3 > 0) and (3 < 5))
print((3>2) & (3>2))
print((3>5) or (2 == 2 ))
print((3>5) | (2 == 2 ))
print(5 > 4 > 3)
print(5 > 4 > 7) # False

num = 5 
num += 5
print(num)
num *= 2
print(num)
num -= 5
print(num)
num /= 2
print(num)

print(abs(-5)) # 절댓값
print(pow(4,2)) # 4^2
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 반올림 3

from math import * # 사용해야 밑에 것들 사용가능
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근  4
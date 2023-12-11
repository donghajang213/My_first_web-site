class Unit:
    def __init__(self, name, hp, damage): ## 객체 Unit에 포함된 Instence self는 필수
        self.name = name  # 멤버 변수
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력: {self.hp}, 공격력: {self.damage} ")

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# marine1 = Unit("마린",) # 사용 불가능 init에 포함된 객체 다 사용해야함
# marine1 = Unit("마린", 40)# 사용 불가능 init에 포함된 객체 다 사용해야함

wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}")  # 멤버 변수에서 가져옴

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #외부 멤버 변수

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
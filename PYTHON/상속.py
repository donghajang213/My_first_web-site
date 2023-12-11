# 상속
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp): ## 객체 Unit에 포함된 Instence self는 필수
#         self.name = name  # 멤버 변수
#         self.hp = hp

# # 공격 유닛
# class AttackUnit(Unit): # 상속받은 Unit
#     def __init__(self, name, hp, damage): ## 객체 Unit에 포함된 Instence self는 필수
#         Unit.__init__(self, name, hp) # 적어줘야함
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name}의 체력이 {self.hp}만큼 남았습니다.")

#         if self.hp <= 0:
#             print(f"{self.name}은 사망하였습니다.")

## 다중 상속 부모가 둘 이상

class Unit:
    def __init__(self, name, hp): ## 객체 Unit에 포함된 Instence self는 필수
        self.name = name  # 멤버 변수
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 상속받은 Unit
    def __init__(self, name, hp, damage): ## 객체 Unit에 포함된 Instence self는 필수
        Unit.__init__(self, name, hp) # 적어줘야함
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}의 체력이 {self.hp}만큼 남았습니다.")

        if self.hp <= 0:
            print(f"{self.name}은 사망하였습니다.")
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlybaleAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 
valkyrie = FlybaleAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "6시") #Flyable은 이름이 없어서 별도로 이름 추가
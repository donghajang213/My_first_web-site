# class Unit:
#     def __init__(self, name, hp, damage): ## 객체 Unit에 포함된 Instence self는 필수
#         self.name = name  # 멤버 변수
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛이 생성 되었습니다.")
#         print(f"체력: {self.hp}, 공격력: {self.damage} ")

# class AttackUnit:
#     def __init__(self, name, hp, damage): ## 객체 Unit에 포함된 Instence self는 필수
#         self.name = name  # 멤버 변수
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name}의 체력이 {self.hp}만큼 남았습니다.")

#         if self.hp <= 0:
#             print(f"{self.name}은 사망하였습니다.")

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

### 메소드 오버라이딩

class Unit:
    def __init__(self, name, hp, speed): ## 객체 Unit에 포함된 Instence self는 필수
        self.name = name  # 멤버 변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다 [속도 {self.speed}]")

# 공격 유닛
class AttackUnit(Unit): # 상속받은 Unit
    def __init__(self, name, hp, speed, damage): ## 객체 Unit에 포함된 Instence self는 필수
        Unit.__init__(self, name, hp, speed) # 적어줘야함
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
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# # 발키리 
# valkyrie = FlybaleAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "6시") #Flyable은 이름이 없어서 별도로 이름 추가

# 벌쳐

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루져

# battlecrusier = FlybaleAttackUnit("배틀크루져", 500, 20, 3)

# vulture.move("11시")
# battlecrusier.move("9시")


## pass  (아무것도 안하고 오류있어도 넘어간다)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# Supplydepoit = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.") # 이것만 출력 pass 때문에

# def game_over():  
#     pass

# game_start()
# game_over()


### super

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) ## super는()필요하고 self 정보 X
#         self.location = location

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):  # (Unit, Flyable)시 "Unit 생성자" 출력 부모클래스에서 앞에 것만 출력하는 단점이 있음
    def __init__(self):
        super().__init()



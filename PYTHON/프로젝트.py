from random import *
class Unit:
    def __init__(self, name, hp, speed): ## 객체 Unit에 포함된 Instence self는 필수
        self.name = name  # 멤버 변수
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다") # name 써도

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다 [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}의 체력이 {self.hp}만큼 남았습니다.")

        if self.hp <= 0:
            print(f"{self.name}은 사망하였습니다.")
    

# 공격 유닛
class AttackUnit(Unit): # 상속받은 Unit
    def __init__(self, name, hp, speed, damage): ## 객체 Unit에 포함된 Instence self는 필수
        Unit.__init__(self, name, hp, speed) # 적어줘야함
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 스킬 추가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (hp 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 사용이 불가합니다.")

class Tank(AttackUnit):
    seize_developed = False 
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seizemode = False

    def set_seizemode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때
        if self.seizemode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seizemode = True

        # 현재 시즈모드일 때
        else: 
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seizemode = False


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

class Wraith(FlybaleAttackUnit):

    def __init__(self):
        FlybaleAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드 해제")
            self.clocked = False

        else:
            print(f"{self.name} : 클로킹 모드 설정합니다")
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.") 

def game_over():  
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일관 관리

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동

for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 상태")

# 공격 모드 준비 

for unit in attack_units:
    if isinstance(unit, Marine):  ## 클래스 instance 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seizemode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격 랜덤으로 5 ~ 20

#게임 종료 

game_over()
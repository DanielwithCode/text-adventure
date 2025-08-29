import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.location = "마을"
        self.gold = 50
        self.experience = 0
        self.level = 1
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"✅ {item}을(를) 획득했습니다!")
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item):
        return item in self.inventory
    
    def heal(self, amount):
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        healed = self.health - old_health
        if healed > 0:
            print(f"❤️ 체력이 {healed} 회복되었습니다! (현재: {self.health}/{self.max_health})")
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"💥 {amount}의 피해를 입었습니다! (현재 체력: {self.health}/{self.max_health})")
        
        if self.health <= 0:
            print("😵 체력이 모두 소진되었습니다...")
            return False
        return True
    
    def gain_experience(self, exp):
        self.experience += exp
        print(f"✨ 경험치 {exp}을 얻었습니다!")
        
        # 레벨업 체크
        while self.experience >= self.level * 100:
            self.experience -= self.level * 100
            self.level += 1
            self.max_health += 20
            self.health = self.max_health
            print(f"🎉 레벨업! 레벨 {self.level}이 되었습니다!")
            print(f"❤️ 최대 체력이 증가했습니다! ({self.max_health})")
    
    def add_gold(self, amount):
        self.gold += amount
        print(f"💰 금화 {amount}개를 얻었습니다! (보유: {self.gold}개)")
    
    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def show_status(self):
        print("\n" + "="*40)
        print(f"📊 {self.name}의 상태")
        print("="*40)
        print(f"🎯 레벨: {self.level}")
        print(f"❤️ 체력: {self.health}/{self.max_health}")
        print(f"⭐ 경험치: {self.experience}/{self.level * 100}")
        print(f"💰 골드: {self.gold}개")
        print(f"📍 현재 위치: {self.location}")
        print(f"🎒 인벤토리: {', '.join(self.inventory) if self.inventory else '비어있음'}")
        print("="*40)

def clear_screen():
    """화면 정리 (Replit에서도 작동)"""
    print("\n" * 3)

def slow_print(text, delay=0.03):
    """텍스트를 천천히 출력하는 함수"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wait_for_enter():
    """엔터 키를 누를 때까지 대기"""
    input("\n계속하려면 엔터를 누르세요...")

class TextAdventure:
    def __init__(self):
        self.player = None
        self.game_over = False
    
    def start_game(self):
        """게임 시작"""
        clear_screen()
        slow_print("🌟 환상의 대륙 모험기 🌟")
        slow_print("=" * 30)
        
        name = input("\n용감한 모험가여, 당신의 이름은 무엇입니까? ")
        self.player = Player(name)
        
        slow_print(f"\n환영합니다, {name}님!")
        slow_print("당신은 작은 마을에서 모험을 시작합니다...")
        wait_for_enter()
        
        self.main_game_loop()
    
    def main_game_loop(self):
        """메인 게임 루프"""
        while not self.game_over and self.player.health > 0:
            self.show_location_menu()
            
            try:
                choice = input("\n선택하세요: ")
                self.handle_main_choice(choice)
            except KeyboardInterrupt:
                print("\n\n👋 게임을 종료합니다. 안녕히 가세요!")
                break
    
    def show_location_menu(self):
        """현재 위치의 메뉴 표시"""
        clear_screen()
        print(f"🏰 현재 위치: {self.player.location}")
        print(f"👤 {self.player.name} (레벨 {self.player.level}) | ❤️ {self.player.health}/{self.player.max_health} | 💰 {self.player.gold}")
        print("\n" + "="*40)
        print("어디로 가시겠습니까?")
        print("="*40)
        print("1. 🌲 마법의 숲 탐험")
        print("2. 🏰 고대 던전 탐험")
        print("3. 🏪 상점 방문")
        print("4. 🏠 여관에서 휴식")
        print("5. 📊 상태 확인")
        print("6. 🎒 인벤토리 확인")
        print("7. 💾 게임 종료")
        print("="*40)
    
    def handle_main_choice(self, choice):
        """메인 메뉴 선택 처리"""
        if choice == "1":
            self.forest_adventure()
        elif choice == "2":
            self.dungeon_adventure()
        elif choice == "3":
            self.visit_shop()
        elif choice == "4":
            self.rest_at_inn()
        elif choice == "5":
            self.player.show_status()
            wait_for_enter()
        elif choice == "6":
            self.show_inventory()
        elif choice == "7":
            self.end_game()
        else:
            print("❌ 올바른 번호를 선택해주세요!")
            time.sleep(1)
    
    def forest_adventure(self):
        """숲 모험"""
        self.player.location = "마법의 숲"
        clear_screen()
        slow_print("🌲 마법의 숲에 들어왔습니다...")
        slow_print("신비로운 기운이 느껴집니다.")
        
        # 랜덤 이벤트
        events = [
            self.forest_fairy_encounter,
            self.forest_wolf_encounter,
            self.forest_treasure_find,
            self.forest_herb_gather
        ]
        
        event = random.choice(events)
        event()
        
        self.player.location = "마을"
        wait_for_enter()
    
    def forest_fairy_encounter(self):
        """요정 만남 이벤트"""
        slow_print("\n✨ 갑자기 작은 요정이 나타났습니다!")
        slow_print("🧚‍♀️ 요정: '모험가님, 도움이 필요해 보이네요!'")
        
        print("\n요정이 무엇을 해줄까요?")
        print("1. 체력 회복 요청")
        print("2. 마법의 물약 요청")
        print("3. 정보 요청")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            self.player.heal(30)
            slow_print("🧚‍♀️ 요정: '따뜻한 빛이 당신을 감쌉니다.'")
        elif choice == "2":
            self.player.add_item("마법의 물약")
            slow_print("🧚‍♀️ 요정: '이 물약이 도움이 될 거예요!'")
        elif choice == "3":
            slow_print("🧚‍♀️ 요정: '던전에는 강력한 몬스터가 살고 있어요. 조심하세요!'")
        
        self.player.gain_experience(20)
    
    def forest_wolf_encounter(self):
        """늑대 만남 이벤트"""
        slow_print("\n🐺 갑자기 큰 늑대가 나타났습니다!")
        slow_print("늑대가 으르렁거리며 당신을 노려봅니다...")
        
        print("\n어떻게 하시겠습니까?")
        print("1. ⚔️ 싸운다")
        print("2. 🏃 도망간다")
        print("3. 🍖 음식으로 달랜다 (음식이 있다면)")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            if self.player.has_item("칼"):
                slow_print("⚔️ 칼을 휘둘러 늑대와 싸웁니다!")
                if random.random() < 0.7:  # 70% 승리 확률
                    slow_print("🎉 늑대를 물리쳤습니다!")
                    self.player.add_gold(30)
                    self.player.gain_experience(50)
                    if random.random() < 0.3:  # 30% 확률로 아이템 획득
                        self.player.add_item("늑대 가죽")
                else:
                    slow_print("💥 늑대의 반격에 당했습니다!")
                    self.player.take_damage(25)
            else:
                slow_print("⚔️ 맨손으로 늑대와 싸웁니다!")
                slow_print("💥 늑대가 더 강합니다!")
                self.player.take_damage(40)
                if self.player.health > 0:
                    slow_print("🏃 간신히 도망쳤습니다...")
        
        elif choice == "2":
            slow_print("🏃 재빠르게 도망쳤습니다!")
            if random.random() < 0.3:  # 30% 확률로 부상
                slow_print("💥 도망치다가 나무에 부딪혔습니다!")
                self.player.take_damage(10)
        
        elif choice == "3":
            if self.player.has_item("빵") or self.player.has_item("고기"):
                food = "빵" if self.player.has_item("빵") else "고기"
                self.player.remove_item(food)
                slow_print(f"🍖 {food}을 늑대에게 던졌습니다.")
                slow_print("🐺 늑대가 음식을 먹고 만족해하며 떠났습니다!")
                self.player.gain_experience(30)
            else:
                slow_print("❌ 음식이 없습니다!")
                slow_print("🐺 늑대가 공격합니다!")
                self.player.take_damage(20)
    
    def forest_treasure_find(self):
        """보물 발견 이벤트"""
        slow_print("\n💎 숲 속에서 반짝이는 보물상자를 발견했습니다!")
        slow_print("하지만 상자에 자물쇠가 걸려있습니다...")
        
        print("\n어떻게 하시겠습니까?")
        print("1. 🔓 열쇠로 연다 (열쇠가 있다면)")
        print("2. 🔨 강제로 부순다")
        print("3. 🚶 그냥 지나간다")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            if self.player.has_item("열쇠"):
                self.player.remove_item("열쇠")
                slow_print("🔓 상자가 열렸습니다!")
                treasure = random.choice(["마법의 반지", "황금 목걸이", "고급 물약"])
                self.player.add_item(treasure)
                self.player.add_gold(50)
                self.player.gain_experience(40)
            else:
                slow_print("❌ 열쇠가 없습니다!")
        
        elif choice == "2":
            slow_print("🔨 상자를 강제로 부숩니다!")
            if random.random() < 0.6:  # 60% 성공 확률
                slow_print("💰 상자 안에서 금화를 발견했습니다!")
                self.player.add_gold(25)
                self.player.gain_experience(20)
            else:
                slow_print("💥 상자가 폭발했습니다! 함정이었나봅니다!")
                self.player.take_damage(15)
        
        elif choice == "3":
            slow_print("🚶 조심스럽게 지나갑니다...")
            slow_print("때로는 신중함이 최선의 선택입니다.")
    
    def forest_herb_gather(self):
        """약초 채집 이벤트"""
        slow_print("\n🌿 희귀한 약초들이 자라는 곳을 발견했습니다!")
        slow_print("이 약초들은 체력 회복에 도움이 될 것 같습니다.")
        
        herbs_found = random.randint(1, 3)
        for _ in range(herbs_found):
            self.player.add_item("치료 약초")
        
        self.player.gain_experience(15)
        slow_print(f"🌿 총 {herbs_found}개의 약초를 채집했습니다!")
    
    def dungeon_adventure(self):
        """던전 모험"""
        self.player.location = "고대 던전"
        clear_screen()
        slow_print("🏰 고대 던전에 들어왔습니다...")
        slow_print("어둠 속에서 무언가가 움직이는 소리가 들립니다...")
        
        if self.player.level < 2:
            slow_print("⚠️ 경고: 이곳은 위험합니다! (권장 레벨: 2 이상)")
        
        # 던전 이벤트
        events = [
            self.dungeon_skeleton_fight,
            self.dungeon_treasure_room,
            self.dungeon_trap_room,
            self.dungeon_boss_encounter
        ]
        
        event = random.choice(events)
        event()
        
        self.player.location = "마을"
        wait_for_enter()
    
    def dungeon_skeleton_fight(self):
        """스켈레톤 전투"""
        slow_print("\n💀 갑자기 스켈레톤이 나타났습니다!")
        slow_print("뼈다귀가 덜걱거리며 당신을 공격합니다!")
        
        skeleton_hp = 60
        
        while skeleton_hp > 0 and self.player.health > 0:
            print(f"\n💀 스켈레톤 체력: {skeleton_hp}")
            print(f"❤️ 당신의 체력: {self.player.health}")
            print("\n무엇을 하시겠습니까?")
            print("1. ⚔️ 공격")
            print("2. 🛡️ 방어")
            print("3. 💊 물약 사용")
            print("4. 🏃 도망")
            
            choice = input("선택하세요: ")
            
            if choice == "1":
                damage = random.randint(20, 35)
                if self.player.has_item("칼"):
                    damage += 10
                    slow_print("⚔️ 칼로 강력하게 공격합니다!")
                else:
                    slow_print("👊 주먹으로 공격합니다!")
                
                skeleton_hp -= damage
                slow_print(f"💥 스켈레톤에게 {damage}의 피해를 입혔습니다!")
                
                if skeleton_hp <= 0:
                    break
            
            elif choice == "2":
                slow_print("🛡️ 방어 자세를 취합니다!")
                skeleton_damage = random.randint(5, 15)  # 방어로 피해 감소
            
            elif choice == "3":
                if self.player.has_item("마법의 물약"):
                    self.player.remove_item("마법의 물약")
                    self.player.heal(40)
                elif self.player.has_item("치료 약초"):
                    self.player.remove_item("치료 약초")
                    self.player.heal(20)
                else:
                    slow_print("❌ 사용할 수 있는 치료 아이템이 없습니다!")
                    continue
            
            elif choice == "4":
                if random.random() < 0.5:  # 50% 도망 성공
                    slow_print("🏃 성공적으로 도망쳤습니다!")
                    return
                else:
                    slow_print("💥 도망치지 못했습니다!")
            
            # 스켈레톤 공격
            if skeleton_hp > 0:
                if choice == "2":  # 방어했을 때
                    skeleton_damage = random.randint(5, 15)
                else:
                    skeleton_damage = random.randint(15, 25)
                
                if not self.player.take_damage(skeleton_damage):
                    return  # 플레이어가 죽었으면 종료
        
        if skeleton_hp <= 0:
            slow_print("🎉 스켈레톤을 물리쳤습니다!")
            self.player.add_gold(40)
            self.player.gain_experience(80)
            
            if random.random() < 0.4:  # 40% 확률로 아이템 획득
                item = random.choice(["고대의 열쇠", "마법의 물약", "은화"])
                self.player.add_item(item)
    
    def dungeon_treasure_room(self):
        """보물방 이벤트"""
        slow_print("\n💰 보물로 가득한 방을 발견했습니다!")
        slow_print("금은보화가 반짝이고 있습니다...")
        
        if random.random() < 0.3:  # 30% 확률로 함정
            slow_print("⚠️ 하지만 이것은 함정이었습니다!")
            slow_print("💥 독가스가 분출됩니다!")
            self.player.take_damage(20)
        else:
            gold_found = random.randint(50, 100)
            self.player.add_gold(gold_found)
            
            treasures = ["다이아몬드", "루비", "사파이어", "마법의 구슬"]
            treasure = random.choice(treasures)
            self.player.add_item(treasure)
            
            self.player.gain_experience(60)
    
    def dungeon_trap_room(self):
        """함정방 이벤트"""
        slow_print("\n🕳️ 바닥에 이상한 압력판이 있는 방입니다...")
        
        print("\n어떻게 하시겠습니까?")
        print("1. 🚶 조심스럽게 걸어간다")
        print("2. 🏃 빠르게 뛰어간다")
        print("3. 🪨 돌을 던져서 함정을 작동시킨다")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            if random.random() < 0.7:  # 70% 성공
                slow_print("✅ 조심스럽게 함정을 피해 지나갔습니다!")
                self.player.gain_experience(30)
            else:
                slow_print("💥 함정에 걸렸습니다!")
                self.player.take_damage(25)
        
        elif choice == "2":
            if random.random() < 0.5:  # 50% 성공
                slow_print("🏃 빠르게 달려서 함정을 피했습니다!")
                self.player.gain_experience(25)
            else:
                slow_print("💥 달리다가 함정에 빠졌습니다!")
                self.player.take_damage(30)
        
        elif choice == "3":
            slow_print("🪨 돌을 던져서 함정을 먼저 작동시켰습니다!")
            slow_print("💡 영리한 판단입니다!")
            slow_print("✅ 안전하게 지나갔습니다!")
            self.player.gain_experience(40)
    
    def dungeon_boss_encounter(self):
        """보스 조우 이벤트"""
        if self.player.level < 3:
            slow_print("\n👹 던전 깊숙한 곳에서 강력한 기운이 느껴집니다...")
            slow_print("⚠️ 아직 맞설 준비가 되지 않은 것 같습니다.")
            slow_print("🏃 조용히 돌아갑니다...")
            return
        
        slow_print("\n👹 던전의 주인, 고블린 왕이 나타났습니다!")
        slow_print("거대한 도끼를 들고 으르렁거립니다!")
        
        print("\n어떻게 하시겠습니까?")
        print("1. ⚔️ 용감하게 싸운다")
        print("2. 🏃 도망간다")
        print("3. 💎 보물로 협상을 시도한다")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            if self.player.has_item("칼") and self.player.health > 50:
                slow_print("⚔️ 장비를 갖추고 용감하게 싸웁니다!")
                slow_print("🎉 힘든 싸움 끝에 고블린 왕을 물리쳤습니다!")
                self.player.add_gold(200)
                self.player.gain_experience(200)
                self.player.add_item("왕의 왕관")
                slow_print("👑 전설적인 아이템을 획득했습니다!")
            else:
                slow_print("💥 준비가 부족했습니다!")
                self.player.take_damage(40)
                slow_print("🏃 간신히 도망쳤습니다...")
        
        elif choice == "2":
            slow_print("🏃 신중하게 도망쳤습니다!")
            slow_print("때로는 후퇴가 최선의 선택입니다.")
        
        elif choice == "3":
            if self.player.has_item("다이아몬드") or self.player.gold >= 100:
                slow_print("💎 보물을 제시하며 협상합니다!")
                slow_print("👹 고블린 왕이 관심을 보입니다...")
                
                if self.player.has_item("다이아몬드"):
                    self.player.remove_item("다이아몬드")
                    slow_print("💎 다이아몬드와 교환으로 평화 협정을 맺었습니다!")
                else:
                    self.player.spend_gold(100)
                    slow_print("💰 금화로 협상에 성공했습니다!")
                
                self.player.gain_experience(100)
                self.player.add_item("고블린의 우정")
            else:
                slow_print("❌ 협상할 만한 보물이 없습니다!")
                slow_print("👹 고블린 왕이 화를 냅니다!")
                self.player.take_damage(30)
    
    def visit_shop(self):
        """상점 방문"""
        clear_screen()
        slow_print("🏪 마을 상점에 들어왔습니다.")
        slow_print("👨‍💼 상인: '어서오세요! 좋은 물건들이 많이 있습니다!'")
        
        while True:
            print(f"\n💰 보유 금화: {self.player.gold}개")
            print("\n🛒 상점 목록:")
            print("=" * 30)
            print("1. ⚔️ 칼 (100골드)")
            print("2. 💊 마법의 물약 (50골드)")
            print("3. 🍖 고기 (20골드)")
            print("4. 🍞 빵 (10골드)")
            print("5. 🔑 열쇠 (80골드)")
            print("6. 💎 아이템 판매")
            print("7. 🚪 상점 나가기")
            print("=" * 30)
            
            choice = input("무엇을 하시겠습니까? ")
            
            if choice == "1":
                if self.player.spend_gold(100):
                    self.player.add_item("칼")
                    slow_print("👨‍💼 상인: '좋은 선택입니다! 이 칼은 매우 날카롭습니다!'")
                else:
                    slow_print("👨‍💼 상인: '금화가 부족하시네요.'")
            
            elif choice == "2":
                if self.player.spend_gold(50):
                    self.player.add_item("마법의 물약")
                    slow_print("👨‍💼 상인: '이 물약은 상처를 즉시 치료해줍니다!'")
                else:
                    slow_print("👨‍💼 상인: '금화가 부족하시네요.'")
            
            elif choice == "3":
                if self.player.spend_gold(20):
                    self.player.add_item("고기")
                    slow_print("👨‍💼 상인: '신선한 고기입니다!'")
                else:
                    slow_print("👨‍💼 상인: '금화가 부족하시네요.'")
            
            elif choice == "4":
                if self.player.spend_gold(10):
                    self.player.add_item("빵")
                    slow_print("👨‍💼 상인: '갓 구운 빵입니다!'")
                else:
                    slow_print("👨‍💼 상인: '금화가 부족하시네요.'")
            
            elif choice == "5":
                if self.player.spend_gold(80):
                    self.player.add_item("열쇠")
                    slow_print("👨‍💼 상인: '이 열쇠는 많은 자물쇠를 열 수 있습니다!'")
                else:
                    slow_print("👨‍💼 상인: '금화가 부족하시네요.'")
            
            elif choice == "6":
                self.sell_items()
            
            elif choice == "7":
                slow_print("👨‍💼 상인: '또 오세요!'")
                break
            
            else:
                slow_print("❌ 올바른 번호를 선택해주세요!")
    
    def sell_items(self):
        """아이템 판매"""
        sellable_items = {
            "늑대 가죽": 40,
            "다이아몬드": 150,
            "루비": 120,
            "사파이어": 100,
            "마법의 구슬": 80,
            "황금 목걸이": 200,
            "마법의 반지": 180,
            "은화": 30
        }
        
        print("\n💰 판매 가능한 아이템:")
        sell_list = []
        for item in self.player.inventory:
            if item in sellable_items:
                sell_list.append(item)
                print(f"- {item} ({sellable_items[item]}골드)")
        
        if not sell_list:
            slow_print("판매할 수 있는 아이템이 없습니다.")
            return
        
        item_name = input("\n판매할 아이템 이름을 입력하세요 (취소하려면 엔터): ")
        
        if item_name in sell_list:
            self.player.remove_item(item_name)
            gold_earned = sellable_items[item_name]
            self.player.add_gold(gold_earned)
            slow_print(f"👨‍💼 상인: '{item_name}을 {gold_earned}골드에 사겠습니다!'")
        elif item_name:
            slow_print("❌ 그 아이템은 판매할 수 없거나 보유하고 있지 않습니다.")
    
    def rest_at_inn(self):
        """여관에서 휴식"""
        clear_screen()
        slow_print("🏠 아늑한 여관에 들어왔습니다.")
        slow_print("👵 여관 주인: '피곤해 보이시네요. 휴식이 필요하시겠어요?'")
        
        print(f"\n💰 보유 금화: {self.player.gold}개")
        print("❤️ 현재 체력: {}/{} ".format(self.player.health, self.player.max_health))
        print("\n휴식 옵션:")
        print("1. 💤 간단한 휴식 (무료) - 체력 20 회복")
        print("2. 🛏️ 편안한 잠자리 (30골드) - 완전 회복")
        print("3. 🍽️ 호화로운 휴식 (50골드) - 완전 회복 + 임시 체력 증가")
        print("4. 🚪 여관 나가기")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            self.player.heal(20)
            slow_print("👵 여관 주인: '조금 나아지셨나요?'")
        
        elif choice == "2":
            if self.player.spend_gold(30):
                self.player.health = self.player.max_health
                slow_print("💤 푹 잤습니다! 체력이 완전히 회복되었습니다!")
                slow_print("👵 여관 주인: '잘 쉬셨나요?'")
            else:
                slow_print("👵 여관 주인: '금화가 부족하시네요.'")
        
        elif choice == "3":
            if self.player.spend_gold(50):
                self.player.health = self.player.max_health + 20
                slow_print("🍽️ 맛있는 음식과 최고급 침실에서 휴식했습니다!")
                slow_print("❤️ 체력이 완전 회복되고 임시로 20 증가했습니다!")
                slow_print("👵 여관 주인: '최고의 서비스였습니다!'")
            else:
                slow_print("👵 여관 주인: '금화가 부족하시네요.'")
        
        elif choice == "4":
            slow_print("👵 여관 주인: '언제든 오세요!'")
        
        else:
            slow_print("❌ 올바른 번호를 선택해주세요!")
        
        if choice in ["1", "2", "3"]:
            wait_for_enter()
    
    def show_inventory(self):
        """인벤토리 표시"""
        clear_screen()
        print("🎒 인벤토리")
        print("=" * 30)
        
        if not self.player.inventory:
            print("인벤토리가 비어있습니다.")
        else:
            item_count = {}
            for item in self.player.inventory:
                item_count[item] = item_count.get(item, 0) + 1
            
            for item, count in item_count.items():
                if count > 1:
                    print(f"- {item} x{count}")
                else:
                    print(f"- {item}")
        
        print("=" * 30)
        
        # 아이템 사용 옵션
        usable_items = ["마법의 물약", "치료 약초", "빵", "고기"]
        usable_in_inventory = [item for item in self.player.inventory if item in usable_items]
        
        if usable_in_inventory:
            print("\n사용 가능한 아이템:")
            for i, item in enumerate(set(usable_in_inventory), 1):
                print(f"{i}. {item}")
            print(f"{len(set(usable_in_inventory)) + 1}. 돌아가기")
            
            try:
                choice = int(input("사용할 아이템 번호: "))
                if 1 <= choice <= len(set(usable_in_inventory)):
                    item_to_use = list(set(usable_in_inventory))[choice - 1]
                    self.use_item(item_to_use)
            except ValueError:
                pass
        
        wait_for_enter()
    
    def use_item(self, item):
        """아이템 사용"""
        if item == "마법의 물약":
            self.player.remove_item(item)
            self.player.heal(40)
            slow_print("💊 마법의 물약을 사용했습니다!")
        
        elif item == "치료 약초":
            self.player.remove_item(item)
            self.player.heal(20)
            slow_print("🌿 치료 약초를 사용했습니다!")
        
        elif item == "빵":
            self.player.remove_item(item)
            self.player.heal(15)
            slow_print("🍞 빵을 먹었습니다!")
        
        elif item == "고기":
            self.player.remove_item(item)
            self.player.heal(25)
            slow_print("🍖 고기를 먹었습니다!")
    
    def end_game(self):
        """게임 종료"""
        clear_screen()
        slow_print("🌟 모험의 기록 🌟")
        print("=" * 40)
        print(f"모험가: {self.player.name}")
        print(f"최종 레벨: {self.player.level}")
        print(f"보유 골드: {self.player.gold}")
        print(f"수집한 아이템: {len(self.player.inventory)}개")
        print("=" * 40)
        
        if self.player.level >= 5:
            slow_print("🏆 전설의 모험가가 되었습니다!")
        elif self.player.level >= 3:
            slow_print("⭐ 숙련된 모험가입니다!")
        else:
            slow_print("🌱 모험을 시작한 새내기입니다!")
        
        slow_print(f"\n{self.player.name}님의 모험을 마칩니다.")
        slow_print("언제든 다시 모험을 떠나보세요! 👋")
        
        self.game_over = True

# 게임 실행
if __name__ == "__main__":
    try:
        game = TextAdventure()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\n게임이 중단되었습니다. 👋")
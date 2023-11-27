import random, time
import os
import datetime
print("\n\nПеред началом игры будет создана папка для сохранения результатов игры.")
input("\nВведите Enter, чтобы продолжить.")
e = "Папка для сохранения логов создана успешно"
try:
    os.mkdir("log")
except OSError as ex:
    print("\nПапка для сохранения логов была создана ранее.")
    e = str(ex)
with open("log\log.txt", "a") as file:
    file.write(f"{datetime.datetime.today()}:{str(e)}\n")
input("\nВведите Enter, чтобы продолжить.")



player_victory_1 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━━─≪Победа≫━─━──━──━─━─━━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    С вашими храбрыми действиями и стратегией вы сумели преодолеть силы Зеленого Рыцаря Леса. Ваши мечебные удары 
    и магические артефакты разгоняют магию природы, и Зеленый Рыцарь Леса поддается вашей силе.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""
player_victory_2 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━━─≪Победа≫━─━──━──━─━─━━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Когда последний удар наносится, Зеленый Рыцарь Леса исчезает в тумане, и ваши ноги опять унесут вас к алтарной 
    площади. Там, в центре, блеск светящегося Кристалла Света ослепляет вас.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""
player_victory_3 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━━─≪Победа≫━─━──━──━─━─━━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Вы тщательно поднимаете Кристалл Света, ощущая тепло его магии. Силы природы подчинены вам, и Темный Лес 
    отзывается на ваш вызов. Свет Кристалла наполняет все вокруг, разгоняя тень, и вы понимаете, что теперь вы 
    обладаете несокрушимой магией.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""
player_victory_4 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━━─≪Победа≫━─━──━──━─━─━━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    С этой победой вы выходите из Темного Леса, Кристалл Света в руках. Вы стали легендой, и ваше имя будет 
    помниться в истории как того, кто смог победить Зеленого Рыцаря Леса и освободить магию Кристалла Света 
    для блага мира.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""

player_defeat_1 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━━─≪Поражение≫━─━──━───━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Зеленый Рыцарь Леса оказывается слишком могущественным, и ваши усилия не достаточны, чтобы его победить. 
    Ваши артефакты тускнеют, и вы ощущаете, как силы природы обрушиваются на вас. Зеленый Рыцарь Леса, 
    выиграв бой, отправляет вас в таинственный лесный лабиринт, где ваша душа будет блуждать вечно.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""
player_defeat_2 = """
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━━─≪Поражение≫━─━──━──━─━━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Вы поглотены Темным Лесом, став частью его древней магии. Ваше приключение заканчивается, и ваши следы 
    стираются под зеленым покровом древних деревьев. Темный Лес сохраняет свои тайны, а Кристалл Света остается 
    недоступным для тех, кто не достаточно силен, чтобы преодолеть его испытание.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
"""


print("""

██╗░░░░░░█████╗░░██████╗████████╗  ██╗███╗░░██╗  ████████╗██╗░░██╗███████╗
██║░░░░░██╔══██╗██╔════╝╚══██╔══╝  ██║████╗░██║  ╚══██╔══╝██║░░██║██╔════╝
██║░░░░░██║░░██║╚█████╗░░░░██║░░░  ██║██╔██╗██║  ░░░██║░░░███████║█████╗░░
██║░░░░░██║░░██║░╚═══██╗░░░██║░░░  ██║██║╚████║  ░░░██║░░░██╔══██║██╔══╝░░
███████╗╚█████╔╝██████╔╝░░░██║░░░  ██║██║░╚███║  ░░░██║░░░██║░░██║███████╗
╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░  ╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░██████╗░██╗░░██╗  ███████╗░█████╗░██████╗░███████╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║░░██║███████║██████╔╝█████═╝░  █████╗░░██║░░██║██████╔╝█████╗░░╚█████╗░░░░██║░░░
██║░░██║██╔══██║██╔══██╗██╔═██╗░  ██╔══╝░░██║░░██║██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░
██████╔╝██║░░██║██║░░██║██║░╚██╗  ██║░░░░░╚█████╔╝██║░░██║███████╗██████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
""")
# Запрос имени пользователя
NAME_USER = ""
while len(NAME_USER) == 0:
    NAME_USER = input("ВВЕДИТЕ ВАЩЕ ИМЯ: ")

time.sleep(0.2)
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Вы - отважный искатель приключений, который решает исследовать таинственный Темный Лес, известный своими древними
    тайнами и сказочными существами. Ваша цель - отыскать легендарный Кристалл Света, который, по преданию, обладает
    магической силой, способной изменить ход судьбы.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.6)
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Ваш путь ведет вглубь густого леса, где каждое дерево кажется живым, а пенистые тропинки сменяют друг друга,
    как лабиринт. По мере продвижения вы встречаете различные преграды и загадочные существа.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.6)
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Однажды, вы натыкаетесь на древнюю алтарную площадь, на которой стоит величественный Кристалл Света. Но ваше
    приближение к алтарю привлекло внимание стража леса - могущественного Древнего Древа, охраняющего свои земли.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.6)
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Древний Дуб, пробудившись от векового сна, объявляет вам условие: чтобы получить Кристалл Света, вы должны
    сразиться с его чемпионом, Зеленым Рыцарем Леса.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.6)
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━━─≪✠≫━─━──━───━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Зеленый Рыцарь Леса - сила природы во плоти, обладающий магией деревьев и способен вызывать силы природы на
    свою защиту.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.3)
input("Нажмите Enter, чтобы продолжить.")
print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━━≪Бой≫━─━──━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    ПЕРЕД БОЕМ ВАМ ПРЕДСТОИТ ВЫБРАТЬ ПРЕДМЕТЫ ОТ КОТОРЫХ БУДЕТ ЗАВИСИТЬ ВАША ПОБЕДА
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
time.sleep(0.3)
input("Нажмите Enter, чтобы продолжить.")

# Бой# урон, защита, исцеление, уклонение, мана
arsenal_all = {
    "Огненный клинок": [50, 10, 0, 6, 15],
    "Меч Зверобоя": [60, 15, 5, 0, 15],
    "Копье Лунного Сияния": [50, 5, 0, 10, 15],
    "Плащ Исцеляющего Света": [5, 5, 0, 20, 30],
    "Плащ скрытности": [5, 5, 0, 40, 30],
    "Эликсир Живой Воды": [0, 0, 70, 0, 100],
    "Эликсир Замедленного Времени": [0, 70, 0, 0, 100],
    "Эликсир Каменной Крепости": [0, 0, 50, 0, 100],
    "Щит Боевого Мага": [10, 70, 0, 14, 12],
    "Щит Драконьей Кожи": [13, 75, 0, 16, 12],
    "Броня Пламенного Сердца": [9, 80, 0, 11, 16],
    "Магическая Броня Сокрытых Теней": [5, 80, 0, 12, 16],
    "Броня Кровавой Зари": [5, 82, 0, 10, 17]
}


count = 1
for i in arsenal_all:
    print(f"{count}. {i}")
    count += 1
arsenal_characteristics = list()    # список свойств выбранных предметов
a = tuple(arsenal_all)    # конвертируем словарь во множество
arsenal_player = set()    # создадим множество предметов персонажа
while len(arsenal_player) != 4:    # цикл выбора предметов игроком
    try:
        b = int(input("\nВ видите номер предмета: ")) - 1  # выводим на экран получаемый предмет
        arsenal_player.add(a[b])  # добавляет
        print(f"Арсенал игрока: {arsenal_player}")
        arsenal_characteristics.append(arsenal_all.get(a[b]))  # добавляет характеристики выбранных предметов в список
    except ValueError as ex:
        e = str(ex) + "- тип данных str недопустим"
        print("Нужно вводить числа!")
        print("Попробуйте снова.")
    except IndexError as ex:
        e = str(ex) + "- превышено допустимое число"
        print("Под данным номером нет предметов!")
        print("Попробуйте снова.")
    with open("log\log.txt", "a") as file:
        file.write(f"{datetime.datetime.today()}:{str(e)}\n")

# сложение характеристик оружия
result_characteristics = list()
for i in range(5):
    result_characteristics.append(sum(j[i] for j in arsenal_characteristics))



class Characteristic():
    'хорактеристика персонажа'

    def __init__(self, damage, defense, healing, evasion, mana):  # урон, защита, исцеление, уклонение, мана
        self.damage = damage
        self.defense = defense
        self.healing = healing
        self.evasion = evasion
        self.mana = mana
        self.hp_player = (self.damage + self.defense + self.healing + self.evasion + self.mana)
        self.hp_npc = self.hp_player + random.randint(20, 50)
        self.npc_defense = self.defense
        self.rating = 0  # Рейтинг персонажа

    def main_player(self):
        print(f"""
        ИГРОК       
------------------------
Сила удара:{self.damage}
Защита:    {self.defense}
Исцеление: {self.healing}
Уклонение: {self.evasion}
Мана:      {self.mana}
Здоровье:  {self.hp_player}
        """)

# бой с npc
class NpcCombat(Characteristic):
    "бой"
    def combat(self):
        while self.hp_npc > 0 and self.hp_player > 0:  # Выполняется пока хп персонажей больше 0
            self.rating += 10  # Рейтинг персонажа
            r = input("Нанести удар ил пропустить y/n: ")
            if r == "y":
                if self.defense > 0:  # если у персонажа еще есть броня
                    self.defense -= random.randint(5, 15)  # Сначала крашится броня
                    if self.defense < 0:  # округляет броню до 0
                        self.defense = 0
                if self.hp_player > 0 and self.defense == 0:  # если хп игрока больше 0 и защита больше 0
                    self.hp_player -= random.randint(10, 30)
                if self.hp_player < 0:  # Предлогает восстановить здоровье игроку если есть очки исцеления
                    self.hp_player = 0
                    x = input("Восстановить здоровье y/n: ")
                    if self.healing > 0:
                        self.hp_player += self.healing
                        self.healing = 0
                        print(f"Вы восстановили здоровье в размере {self.healing}")
                    else:
                        print(f"У вас нет очков исцеления")
                self.mana -= random.randint(5, 10)    # расходует ману на удр по противнику
                if self.npc_defense > 0 and self.mana > 0:
                    self.npc_defense -= random.randint(7, 15)  # Сначала крашится броня противника
                    if self.npc_defense < 0:  # округляет броню до 0
                        self.npc_defense = 0
                elif self.hp_npc > 0 and self.npc_defense == 0 and self.mana > 0:  # если у противника есть хп защита
                    self.hp_npc -= random.randint(10, 30)
                elif self.mana <= 0:
                    self.mana = 0
                    self.mana += random.randint(30, 50)
                    print("У ВАС НЕТ МАНЫ ДЛЯ УДАРА")
                    print("ВЫ ПРОПУСКАЕТЕ ХОД")
                    print("ПРОПУСТИВ ХОД ВЫ ВОСТАНОВЫИЛИ МАНУ")
                    input("Нажмите Enter чтобы продолжить")

                if self.hp_npc < 0:
                    self.hp_npc = 0
                print(f"""
        ИГРОК       
------------------------
Сила удара:{self.damage}        
Защита:    {self.defense}       
Исцеление: {self.healing}       
Уклонение: {self.evasion}       
Мана:      {self.mana}          
Здоровье:  {self.hp_player} 

        NPC
------------------------ 
Защита:    {self.npc_defense}   
Здоровье:  {self.hp_npc}
                        """)

        if self.hp_npc <= 0:
            print("ТЫ ПОБЕДИЛ")
            time.sleep(0.6)
            print(player_victory_1)
            time.sleep(0.6)
            print(player_victory_2)
            time.sleep(0.6)
            print(player_victory_3)
            time.sleep(0.6)
            print(player_victory_4)
        elif self.hp_player <= 0:
            print("ТЫ ПРОИГРАЛ")
            time.sleep(0.6)
            print(player_defeat_1)
            time.sleep(0.6)
            print(player_defeat_2)

    def get_rating(self):
        return self.rating

m = NpcCombat(*result_characteristics)

print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─≪Бой≫━─━──━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    ПЕРЕД ВАМИ ВСТАЛ ВЫБОР
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")

q = "1. Атаковать: Вы решаете напасть на Зеленого Рыцаря Леса, использовав свой арсенал."
w = "2. Сбежать: Вы решаете скрыться с поля боя. И вернуться домой."
r = "3. Обороняться: Вы решаете сосредоточиться на защите, блокируя атаки Зеленого Рыцаря Леса и ища возможности для контратак."

print(q)
print(w)
print(r)
res = 0
while res != 1 and res != 2 and res != 3:
    try:
        res = int(input("\nВведите номер ответа: "))
        if res == 1:
            m.main_player()
            m.combat()
        elif res == 2:
            print("""
╭━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━─━─━━─≪Игра окончена≫━─━──━━─━─━─━─━─━─━─━─━─━─━─━─━─━─━──━─━─━─━─━─━─━━─╮
    Сбежав от Зеленого Рыцаря Леса, вы сохраняете свою жизнь, но тайны Кристалла Света остаются недоступными. 
    Темный Лес навсегда остается загадкой, но вы выбрали свою жизнь над смертельным боем.
╰━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─≪✠≫━─━──━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━─━━─━─━━─╯
""")
        elif res == 3:
            m.main_player()
            m.combat()
    except ValueError as ex:
        e = str(ex) + "- тип данных str недопустим"
        print("Нужно вводить числа!")
        print("Попробуйте снова.")
    with open("log\log.txt", "a") as file:
        file.write(f"{datetime.datetime.today()}:{str(e)}\n")




class LogRatingExit(Characteristic):
    "меню в конце игры"
    def exit(self):
        wh = None
        while wh != 6:
            print(f"""
╔ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - ╗
            1. Показать ошибки    3. Сохранить результаты рейтинга        5. Очистить рейтинг |   ВАШ РЕЙТИНГ
            2. Очистить ошибки    4. Показать весь рейтинг                6. Выход            |     {m.get_rating()}
╚ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - ╝
                """)
            try:
                wh = int(input("Введите номер действия ➤  "))
                if wh == 1:
                    with open("log\log.txt", "r") as file:
                        for line in file:
                            print(line, end="")
                elif wh == 2:
                    with open("log\log.txt", "w") as file:
                        file.write("Ошибок нет")
                elif wh == 3:
                    with open("log\Rating.txt", "a") as file:
                        file.write(f"{datetime.datetime.now()}: {NAME_USER} - {m.get_rating()} очков.\n")
                elif wh == 4:
                    with open("log\Rating.txt", "r") as file:
                        for line in file:
                            print(line, end="")
                elif wh == 5:
                    with open("log\Rating.txt", "w") as file:
                        file.write("")
                elif wh == 6:
                    print("Вы вышли из игры!")
                    break
            except ValueError as ex:
                e = str(ex) + "- тип данных str недопустим"
                print("Нужно вводить числа!")
                print("Попробуйте снова.")
n = LogRatingExit(*result_characteristics)
n.exit()
import random
import time

# Globalne zmienne
life = 300
mana = 150
gold = 50
experience = 0
level = 1
skills = {"Miecz": 1, "Magia": 1, "Obrona": 1}
max_experience = 100
inventory = []
opponents = {
    "Jaskinia": [
        ["Mały Goblin", 15, 5],
        ["Camera Men", 30, 10],
        ["Slime", 10, 3]
    ],
    "Zamek": [
        ["Skibidi Toilet", 25, 7],
        ["Zombie", 40, 8],
        ["Witch", 50, 12]
    ],
    "Góra": [
        ["Dragon", 150, 25],
        ["Troll", 70, 15],
        ["Cyclops", 120, 30]
    ],
    "Las": [
        ["Goblin Archer", 20, 5],
        ["Ork", 40, 10],
        ["Giant Spider", 30, 8]
    ],
    "Morze": [
        ["Sea Monster", 80, 20],
        ["Kraken", 100, 25],
        ["Pirate", 50, 15]
    ],
    "Podziemia": [
        ["Skeleton Warrior", 60, 12],
        ["Necromancer", 60, 18],
        ["Zombie", 40, 8]
    ],
    "Ruiny": [
        ["Vampire", 80, 25],
        ["Mummy", 50, 15],
        ["Ancient Golem", 120, 35]
    ],
    "Zamek Wampira": [
        ["Vampire", 80, 25],
        ["Bat Swarm", 40, 10],
        ["Vampire Lord", 150, 30]
    ],
    "Zamarznięta Kraina": [
        ["Ice Golem", 100, 20],
        ["Snow Beast", 70, 18],
        ["Yeti", 120, 25]
    ],
    "Mroczna Dolina": [
        ["Shadow Demon", 100, 20],
        ["Wraith", 90, 15],
        ["Grim Reaper", 150, 40]
    ]
}

lokacje = [
    "Jaskinia", "Zamek", "Góra", "Las", "Morze", "Podziemia", "Ruiny", "Zamek Wampira", "Zamarznięta Kraina", "Mroczna Dolina"
]

quests = [
    {"name": "Pokonaj Małego Goblina", "reward": 20, "status": False},
    {"name": "Zdobądź Miksturę Many", "reward": 30, "status": False},
    {"name": "Zabij Smoka", "reward": 100, "status": False},
    {"name": "Odwiedź Zamek", "reward": 50, "status": False},
    {"name": "Pokonaj Necromancera", "reward": 80, "status": False},
    {"name": "Pokonaj Wampira", "reward": 150, "status": False},
    {"name": "Zdobądź Złoto z Zamarzniętej Krainy", "reward": 200, "status": False},
    {"name": "Odwiedź Mroczną Dolinę", "reward": 100, "status": False}
]

# Funkcje

def rozwój_postaci():
    """Funkcja rozwijająca postać przy awansie na wyższy poziom."""
    global experience, level, max_experience, life, mana
    if experience >= max_experience:
        level += 1
        experience = 0
        max_experience += 100
        life += 30
        mana += 20
        print(f"Awansowałeś na poziom {level}! Twoje życie to teraz {life}, mana {mana}.")
        rozwój_umiejętności()

def rozwój_umiejętności():
    """Funkcja pozwalająca rozwijać umiejętności postaci."""
    global skills
    print("Wybierz umiejętność do rozwoju:")
    print("1 - Miecz")
    print("2 - Magia")
    print("3 - Obrona")
    wybor = input("Twój wybór: ")
    if wybor == "1":
        skills["Miecz"] += 1
        print("Twoje umiejętności w walce mieczem wzrosły!")
    elif wybor == "2":
        skills["Magia"] += 1
        print("Twoje umiejętności magiczne wzrosły!")
    elif wybor == "3":
        skills["Obrona"] += 1
        print("Twoje umiejętności obronne wzrosły!")
    else:
        print("Nieznany wybór, spróbuj ponownie.")
        rozwój_umiejętności()

def przedmiot():
    """Funkcja przyznająca przedmiot po pokonaniu przeciwnika."""
    przedmioty = ["Mikstura zdrowia", "Mikstura many", "Mikstura siły", "Złoto", "Mikstura wytrzymałości", "Mikstura szybkości", "Miecz", "Zbroja", "Pierścień mocy", "Eliksir Wampira"]
    item = random.choice(przedmioty)
    if item == "Złoto":
        amount = random.randint(10, 30)
        global gold
        gold += amount
        print(f"Znalazłeś {item} ({amount} szt.)! Twoje złoto: {gold}.")
    else:
        inventory.append(item)
        print(f"Znalazłeś przedmiot: {item}!")

def sklep():
    """Funkcja umożliwiająca zakupy w sklepie."""
    global gold
    print("Witamy w sklepie! Masz do wyboru:")
    print("1. Mikstura zdrowia (30 HP) - 15 złota")
    print("2. Mikstura many (40 many) - 15 złota")
    print("3. Mikstura siły (10 obrażeń) - 20 złota")
    print("4. Mikstura wytrzymałości (50 HP przez 5 tur) - 30 złota")
    print("5. Mikstura szybkości (zwiększa szybkość ataku) - 20 złota")
    print("6. Miecz (zwiększa obrażenia) - 40 złota")
    print("7. Zbroja (zwiększa obronę) - 50 złota")
    print("8. Pierścień mocy (zwiększa moc magiczną) - 60 złota")
    print(f"Twoje złoto: {gold}")
    wybor = input("Co chcesz kupić? (1/2/3/4/5/6/7/8): ")
    if wybor == '1' and gold >= 15:
        gold -= 15
        global life
        life += 30
        print(f"Zakupiłeś miksturę zdrowia! Twoje życie to teraz {life}.")
    elif wybor == '2' and gold >= 15:
        gold -= 15
        global mana
        mana += 40
        print(f"Zakupiłeś miksturę many! Twoja mana to teraz {mana}.")
    elif wybor == '3' and gold >= 20:
        gold -= 20
        print("Zakupiłeś miksturę siły! Twoje obrażenia rosną!")
    elif wybor == '4' and gold >= 30:
        gold -= 30
        print("Zakupiłeś miksturę wytrzymałości! Twoje życie wzrasta o 50 przez 5 tur!")
    elif wybor == '5' and gold >= 20:
        gold -= 20
        print("Zakupiłeś miksturę szybkości! Zwiększysz szybkość ataków!")
    elif wybor == '6' and gold >= 40:
        gold -= 40
        inventory.append("Miecz")
        print("Zakupiłeś miecz! Twoje obrażenia wzrosły!")
    elif wybor == '7' and gold >= 50:
        gold -= 50
        inventory.append("Zbroja")
        print("Zakupiłeś zbroję! Twoja obrona wzrosła!")
    elif wybor == '8' and gold >= 60:
        gold -= 60
        inventory.append("Pierścień mocy")
        print("Zakupiłeś pierścień mocy! Twoja moc magiczna wzrosła!")
    else:
        print("Nie masz wystarczającej ilości złota lub wybór jest nieprawidłowy!")

def losowe_wydarzenie():
    """Funkcja losująca wydarzenie podczas podróży."""
    wydarzenia = [
        "Spotkałeś tajemniczego NPC, który daje Ci cenne wskazówki!",
        "Znalazłeś skarb w postaci złota!",
        "Napotkałeś dziwny artefakt, który wzmacnia Twoje umiejętności.",
        "Znalazłeś ukryty punkt, który regeneruje Twoje życie i manę.",
        "Natrafiłeś na zamek, w którym możesz odpocząć i zregenerować siły."
    ]
    print(random.choice(wydarzenia))

def losowy_przeciwnik(lokacja):
    """Funkcja losująca przeciwnika zależnie od lokacji."""
    print(f"Losowanie przeciwnika w lokacji: {lokacja}")
    przeciwnik = random.choice(opponents[lokacja])
    print(f"Spotkałeś {przeciwnik[0]}! Życie: {przeciwnik[1]}, Obrażenia: {przeciwnik[2]}")
    return przeciwnik

def walka(lokacja):
    """Funkcja obsługująca walkę z przeciwnikiem."""
    global life, mana, experience, gold
    rozwój_postaci()
    przeciwnik = losowy_przeciwnik(lokacja)
    while life > 0 and przeciwnik[1] > 0:
        print(f"Twoje życie: {life}, mana: {mana}")
        print(f"Przeciwnik ma {przeciwnik[1]} HP.")
        print("1 - Atak mieczem")
        print("2 - Użyj fireballa")
        print("3 - Użyj mikstury zdrowia")
        wybor = input("Twój wybór: ")
        if wybor == '1':
            obrażenia = random.randint(5, 15) + skills["Miecz"]
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń!")
        elif wybor == '2' and mana >= 5:
            mana -= 5
            obrażenia = random.randint(15, 20) + skills["Magia"]
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń przy użyciu fireballa!")
        elif wybor == '3':
            if "Mikstura zdrowia" in inventory:
                life += 30
                inventory.remove("Mikstura zdrowia")
                print(f"Użyłeś miksturę zdrowia. Twoje życie: {life}")
            else:
                print("Nie masz mikstury zdrowia!")
        else:
            print("Nieznany wybór!")
        
        if przeciwnik[1] <= 0:
            print(f"Pokonałeś {przeciwnik[0]}!")
            experience += 10
            gold += 20
            przedmiot()
            break

        # Przeciwnik atakuje
        damage = przeciwnik[2]
        print(f"Przeciwnik atakuje! Zadaje {damage} obrażeń.")
        life -= damage
        time.sleep(1)

def explore():
    """Funkcja pozwalająca na zwiedzanie różnych lokacji."""
    global life, mana, gold, experience
    print("Wybierz lokację do odwiedzenia:")
    for idx, lokacja in enumerate(lokacje, 1):
        print(f"{idx}. {lokacja}")
    wybor = input("Twój wybór: ")
    try:
        lokacja_wybrana = lokacje[int(wybor) - 1]
        print(f"Podróżujesz do {lokacja_wybrana}...")
        losowe_wydarzenie()  # Losowe wydarzenie podczas eksploracji
        walka(lokacja_wybrana)
    except (ValueError, IndexError):
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        explore()

# Rozpoczęcie gry
def gra():
    """Funkcja główna gry."""
    global life, mana, gold
    print("Witaj w grze RPG!")
    while life > 0:
        explore()
        sklep()
        if life <= 0:
            print("Koniec gry!")
            break

# Rozpoczęcie gry
gra()

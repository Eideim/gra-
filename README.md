import random
import time


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
        print("4 - Atak z łuku (Wymaga umiejętności Obrona)")
        print("5 - Zabójczy cios (Wymaga większej ilości many)")
        print("6 - Magia lodu (Wymaga many)")

        wybor = input("Twój wybór: ")
        
        if wybor == '1':  
            obrażenia = random.randint(5, 15) + skills["Miecz"]
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń atakiem mieczem!")
        
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
        
        elif wybor == '4' and skills["Obrona"] > 0:  
            obrażenia = random.randint(10, 20) + skills["Obrona"]
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń atakiem z łuku!")
        
        elif wybor == '5' and mana >= 10:  
            mana -= 10
            obrażenia = random.randint(25, 35)
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń zabójczym ciosem!")
        
        elif wybor == '6' and mana >= 8:  
            mana -= 8
            obrażenia = random.randint(15, 20) + skills["Magia"]
            przeciwnik[1] -= obrażenia
            print(f"Zadałeś {obrażenia} obrażeń magią lodu!")
            if random.random() < 0.3:  
                print("Przeciwnik został spowolniony!")
                przeciwnik[2] = max(1, przeciwnik[2] - 2)  
        
        else:
            print("Nieznany wybór lub brak wystarczającej many!")
        
        if przeciwnik[1] <= 0:
            print(f"Pokonałeś {przeciwnik[0]}!")
            experience += 10
            gold += 20
            przedmiot()
            break

        
        damage = przeciwnik[2]
        print(f"Przeciwnik atakuje! Zadaje {damage} obrażeń.")
        life -= damage
        time.sleep(1)

    if life <= 0:
        print("Zostałeś pokonany... Gra skończona.")
        return

def przygoda():
    """Funkcja główną obsługującą przygodę."""
    global experience, gold, life, mana
    while True:
        print("\nWybierz lokację do przygody:")
        for idx, lokacja in enumerate(lokacje):
            print(f"{idx + 1}. {lokacja}")
        print("0. Wyjście z gry")
        
        wybor = input("Wybierz lokację: ")
        
        if wybor == '0':
            print("Dziękujemy za grę!")
            break
        
        if wybor.isdigit() and 1 <= int(wybor) <= len(lokacje):
            lokacja = lokacje[int(wybor) - 1]
            print(f"Zaczynasz przygodę w {lokacja}...")
            walka(lokacja)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
        
        rozwój_postaci()  

def menu():
    """Główne menu gry."""
    print("Witaj w grze RPG!")
    while True:
        print("\n1. Przygoda")
        print("2. Sklep")
        print("3. Zakończ grę")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            przygoda()
        elif wybor == '2':
            sklep()
        elif wybor == '3':
            print("Dziękujemy za grę!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


menu()

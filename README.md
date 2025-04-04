books = []
movies = []
phones = []
watches = []  
cars = []     

def add_phone():
    name = input("Podaj nazwę telefonu: ")
    mark = input("Jakiej firmy jest telefon: ")
    year = input("Podaj rok wydania: ")
    ram = input("Podaj ile ma ramu: ")
    storage = input("Podaj ile ma pamięci: ")

    phone = {
        "name": name,
        "mark": mark,
        "ram": int(ram),
        "year": int(year),
        "storage": int(storage)
    }
    phones.append(phone)
    print(f'Telefon "{name}" został dodany.')

def remove_phone():
    name = input("Podaj tytuł telefonu do usunięcia: ")
    global phones
    phones = [phone for phone in phones if phone["name"].lower() != name.lower()]
    print(f'Telefon "{name}" został usunięty.')

def edit_phone():
    name = input("Podaj tytuł telefonu do edycji: ")
    for phone in phones:
        if phone["name"].lower() == name.lower():
            new_name = input(f"Nowa nazwa ({phone['name']}): ") or phone["name"]
            new_mark = input(f"Nowa marka ({phone['mark']}): ") or phone["mark"]
            new_year = input(f"Nowy rok wydania ({phone['year']}): ") or phone["year"]
            new_ram = input(f"Nowy ram ({phone['ram']}): ") or phone["ram"]
            new_storage = input(f"Nowa pamięć ({phone['storage']}): ") or phone["storage"]

            phone["name"] = new_name
            phone["mark"] = new_mark
            phone["year"] = int(new_year)
            phone["ram"] = int(new_ram)
            phone["storage"] = int(new_storage)
            print(f'Telefon "{name}" został zaktualizowany.')
            return
    print(f'Nie znaleziono telefonu "{name}".')

def show_phones():
    if not phones:
        print("Brak telefonów w bibliotece.")
    else:
        print("\nLista telefonów:")
        for phone in phones:
            print(f'{phone["name"]} - {phone["mark"]} ({phone["year"]}) - {phone["ram"]} GB, {phone["storage"]} GB')

def add_book():
    title = input("Podaj tytuł książki: ")
    author = input("Podaj autora książki: ")
    year = input("Podaj rok wydania: ")
    genre = input("Podaj gatunek książki: ")
    pages = input("Podaj liczbę stron: ")

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "pages": int(pages)
    }
    books.append(book)
    print(f'Książka "{title}" została dodana.')

def remove_book():
    title = input("Podaj tytuł książki do usunięcia: ")
    global books
    books = [book for book in books if book["title"].lower() != title.lower()]
    print(f'Książka "{title}" została usunięta.')

def edit_book():
    title = input("Podaj tytuł książki do edycji: ")
    for book in books:
        if book["title"].lower() == title.lower():
            new_title = input(f"Nowy tytuł ({book['title']}): ") or book["title"]
            new_author = input(f"Nowy autor ({book['author']}): ") or book["author"]
            new_year = input(f"Nowy rok wydania ({book['year']}): ") or book["year"]
            new_genre = input(f"Nowy gatunek ({book['genre']}): ") or book["genre"]
            new_pages = input(f"Nowa liczba stron ({book['pages']}): ") or book["pages"]

            book["title"] = new_title
            book["author"] = new_author
            book["year"] = int(new_year)
            book["genre"] = new_genre
            book["pages"] = int(new_pages)
            print(f'Książka "{title}" została zaktualizowana.')
            return
    print(f'Nie znaleziono książki "{title}".')

def show_books():
    if not books:
        print("Brak książek w bibliotece.")
    else:
        print("\nLista książek:")
        for book in books:
            print(f'{book["title"]} - {book["author"]} ({book["year"]}) - {book["genre"]}, {book["pages"]} stron')

def search_book():
    title = input("Podaj tytuł książki do wyszukania: ")
    found_books = [book for book in books if title.lower() in book["title"].lower()]
    if not found_books:
        print(f'Nie znaleziono książki o tytule zawierającym "{title}".')
    else:
        print("\nZnalezione książki:")
        for book in found_books:
            print(f'{book["title"]} - {book["author"]} ({book["year"]})')

def sort_books():
    valid_keys = ["title", "author", "year", "genre", "pages"]
    by = input(f"Sortuj według ({', '.join(valid_keys)}): ")
    if by not in valid_keys:
        print(f'Niepoprawny klucz sortowania. Możesz użyć: {", ".join(valid_keys)}')
        return
    books.sort(key=lambda book: str(book[by]).lower())
    print(f'Książki zostały posortowane według "{by}".')

def filter_books_by_genre():
    genre = input("Podaj gatunek do filtrowania: ")
    filtered_books = [book for book in books if book["genre"].lower() == genre.lower()]
    if not filtered_books:
        print(f'Brak książek w gatunku "{genre}".')
    else:
        print(f'\nLista książek w gatunku "{genre}":')
        for book in filtered_books:
            print(f'{book["title"]} - {book["author"]} ({book["year"]})')

def add_movie():
    title = input("Podaj tytuł filmu: ")
    director = input("Podaj reżysera filmu: ")
    year = input("Podaj rok wydania: ")
    genre = input("Podaj gatunek filmu: ")
    duration = input("Podaj długość filmu w minutach: ")

    movie = {
        "title": title,
        "director": director,
        "year": int(year),
        "genre": genre,
        "duration": int(duration)
    }
    movies.append(movie)
    print(f'Film "{title}" został dodany.')

def remove_movie():
    title = input("Podaj tytuł filmu do usunięcia: ")
    global movies
    movies = [movie for movie in movies if movie["title"].lower() != title.lower()]
    print(f'Film "{title}" został usunięty.')

def edit_movie():
    title = input("Podaj tytuł filmu do edycji: ")
    for movie in movies:
        if movie["title"].lower() == title.lower():
            new_title = input(f"Nowy tytuł ({movie['title']}): ") or movie["title"]
            new_director = input(f"Nowy reżyser ({movie['director']}): ") or movie["director"]
            new_year = input(f"Nowy rok wydania ({movie['year']}): ") or movie["year"]
            new_genre = input(f"Nowy gatunek ({movie['genre']}): ") or movie["genre"]
            new_duration = input(f"Nowa długość filmu ({movie['duration']} min): ") or movie["duration"]

            movie["title"] = new_title
            movie["director"] = new_director
            movie["year"] = int(new_year)
            movie["genre"] = new_genre
            movie["duration"] = int(new_duration)
            print(f'Film "{title}" został zaktualizowany.')
            return
    print(f'Nie znaleziono filmu "{title}".')

def show_movies():
    if not movies:
        print("Brak filmów w bibliotece.")
    else:
        print("\nLista filmów:")
        for movie in movies:
            print(f'{movie["title"]} - {movie["director"]} ({movie["year"]}) - {movie["genre"]}, {movie["duration"]} min')

def add_watch():
    name = input("Podaj nazwę zegarka: ")
    brand = input("Jakiej firmy jest zegarek: ")
    year = input("Podaj rok wydania: ")
    type_ = input("Podaj typ zegarka (np. analogowy, cyfrowy): ")
    price = input("Podaj cenę zegarka: ")

    watch = {
        "name": name,
        "brand": brand,
        "year": int(year),
        "type": type_,
        "price": float(price)
    }
    watches.append(watch)
    print(f'Zegarek "{name}" został dodany.')

def remove_watch():
    name = input("Podaj nazwę zegarka do usunięcia: ")
    global watches
    watches = [watch for watch in watches if watch["name"].lower() != name.lower()]
    print(f'Zegarek "{name}" został usunięty.')

def edit_watch():
    name = input("Podaj nazwę zegarka do edycji: ")
    for watch in watches:
        if watch["name"].lower() == name.lower():
            new_name = input(f"Nowa nazwa ({watch['name']}): ") or watch["name"]
            new_brand = input(f"Nowa marka ({watch['brand']}): ") or watch["brand"]
            new_year = input(f"Nowy rok wydania ({watch['year']}): ") or watch["year"]
            new_type = input(f"Nowy typ ({watch['type']}): ") or watch["type"]
            new_price = input(f"Nowa cena ({watch['price']}): ") or watch["price"]

            watch["name"] = new_name
            watch["brand"] = new_brand
            watch["year"] = int(new_year)
            watch["type"] = new_type
            watch["price"] = float(new_price)
            print(f'Zegarek "{name}" został zaktualizowany.')
            return
    print(f'Nie znaleziono zegarka "{name}".')

def show_watches():
    if not watches:
        print("Brak zegarków w bibliotece.")
    else:
        print("\nLista zegarków:")
        for watch in watches:
            print(f'{watch["name"]} - {watch["brand"]} ({watch["year"]}) - {watch["type"]}, {watch["price"]} PLN')

def add_car():
    make = input("Podaj markę samochodu: ")
    model = input("Podaj model samochodu: ")
    year = input("Podaj rok produkcji: ")
    mileage = input("Podaj przebieg samochodu (km): ")
    price = input("Podaj cenę samochodu: ")

    car = {
        "make": make,
        "model": model,
        "year": int(year),
        "mileage": int(mileage),
        "price": float(price)
    }
    cars.append(car)
    print(f'Samochód "{make} {model}" został dodany.')

def remove_car():
    make = input("Podaj markę samochodu do usunięcia: ")
    model = input("Podaj model samochodu do usunięcia: ")
    global cars
    cars = [car for car in cars if car["make"].lower() != make.lower() or car["model"].lower() != model.lower()]
    print(f'Samochód "{make} {model}" został usunięty.')

def edit_car():
    make = input("Podaj markę samochodu do edycji: ")
    model = input("Podaj model samochodu do edycji: ")
    for car in cars:
        if car["make"].lower() == make.lower() and car["model"].lower() == model.lower():
            new_make = input(f"Nowa marka ({car['make']}): ") or car["make"]
            new_model = input(f"Nowy model ({car['model']}): ") or car["model"]
            new_year = input(f"Nowy rok produkcji ({car['year']}): ") or car["year"]
            new_mileage = input(f"Nowy przebieg ({car['mileage']} km): ") or car["mileage"]
            new_price = input(f"Nowa cena ({car['price']} PLN): ") or car["price"]

            car["make"] = new_make
            car["model"] = new_model
            car["year"] = int(new_year)
            car["mileage"] = int(new_mileage)
            car["price"] = float(new_price)
            print(f'Samochód "{make} {model}" został zaktualizowany.')
            return
    print(f'Nie znaleziono samochodu "{make} {model}".')

def show_cars():
    if not cars:
        print("Brak samochodów w bibliotece.")
    else:
        print("\nLista samochodów:")
        for car in cars:
            print(f'{car["make"]} {car["model"]} ({car["year"]}) - {car["mileage"]} km, {car["price"]} PLN')

def watch_menu():
    while True:
        print("--- MENU BIBLIOTEKI ZEGARKÓW ---")
        print("1. Dodaj zegarek")
        print("2. Usuń zegarek")
        print("3. Edytuj zegarek")
        print("4. Wyświetl wszystkie zegarki")
        print("0. Powrót do głównego menu")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_watch()
        elif choice == "2":
            remove_watch()
        elif choice == "3":
            edit_watch()
        elif choice == "4":
            show_watches()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def car_menu():
    while True:
        print("--- MENU BIBLIOTEKI SAMOCHODÓW ---")
        print("1. Dodaj samochód")
        print("2. Usuń samochód")
        print("3. Edytuj samochód")
        print("4. Wyświetl wszystkie samochody")
        print("0. Powrót do głównego menu")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_car()
        elif choice == "2":
            remove_car()
        elif choice == "3":
            edit_car()
        elif choice == "4":
            show_cars()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def movie_menu():
    while True:
        print("--- MENU BIBLIOTEKI FILMÓW ---")
        print("1. Dodaj film")
        print("2. Usuń film")
        print("3. Edytuj film")
        print("4. Wyświetl wszystkie filmy")
        print("0. Powrót do głównego menu")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            remove_movie()
        elif choice == "3":
            edit_movie()
        elif choice == "4":
            show_movies()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def phone_menu():
    while True:
        print("--- MENU BIBLIOTEKI TELEFONÓW ---")
        print("1. Dodaj telefon")
        print("2. Usuń telefon")
        print("3. Edytuj telefon")
        print("4. Wyświetl wszystkie telefony")
        print("0. Powrót do głównego menu")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_phone()
        elif choice == "2":
            remove_phone()
        elif choice == "3":
            edit_phone()
        elif choice == "4":
            show_phones()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def book_menu():
    while True:
        print("--- MENU BIBLIOTEKI KSIĄŻEK ---")
        print("1. Dodaj książkę")
        print("2. Usuń książkę")
        print("3. Edytuj książkę")
        print("4. Wyświetl wszystkie książki")
        print("5. Wyszukaj książkę")
        print("6. Sortuj książki")
        print("7. Filtruj książki po gatunku")
        print("0. Powrót do głównego menu")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            edit_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            search_book()
        elif choice == "6":
            sort_books()
        elif choice == "7":
            filter_books_by_genre()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def main_menu():
    while True:
        print("=== MENU GŁÓWNE ===")
        print("1. Biblioteka książek")
        print("2. Biblioteka telefonów")
        print("3. Biblioteka filmów")
        print("4. Biblioteka zegarków")
        print("5. Biblioteka samochodów")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            book_menu()
        elif choice == "2":
            phone_menu()
        elif choice == "3":
            movie_menu()
        elif choice == "4":
            watch_menu()
        elif choice == "5":
            car_menu()
        elif choice == "0":
            print("Do widzenia!")
            break

main_menu()


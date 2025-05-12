class Pojazd:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def info(self):
        return f"{self.marka} {self.model}, Rok: {self.rok_produkcji}"

class Samochod(Pojazd):
    def __init__(self, marka, model, rok_produkcji, liczba_drzwi):
        super().__init__(marka, model, rok_produkcji)
        self.liczba_drzwi = liczba_drzwi

    def info(self):
        return f"{super().info()}, Liczba drzwi: {self.liczba_drzwi}"

class Motocykl(Pojazd):
    def __init__(self, marka, model, rok_produkcji, pojemnosc_silnika):
        super().__init__(marka, model, rok_produkcji)
        self.pojemnosc_silnika = pojemnosc_silnika

    def info(self):
        return f"{super().info()}, Pojemność silnika: {self.pojemnosc_silnika} cm³"

class Flota:
    def __init__(self):
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def usun_pojazd(self, pojazd):
        self.pojazdy.remove(pojazd)

    def pokaz_flote(self):
        for pojazd in self.pojazdy:
            print(pojazd.info())

flota = Flota()

samochod1 = Samochod("Toyota", "Corolla", 2020, 4)
motocykl1 = Motocykl("Yamaha", "MT-07", 2019, 689)

flota.dodaj_pojazd(samochod1)
flota.dodaj_pojazd(motocykl1)

flota.pokaz_flote()

samochod2 = Samochod("Ford", "Focus", 2021, 5)
motocykl2 = Motocykl("Kawasaki", "Ninja", 2022, 649)

flota.dodaj_pojazd(samochod2)
flota.dodaj_pojazd(motocykl2)

flota.pokaz_flote()

flota.usun_pojazd(motocykl1)

print("Po usunięciu motocykla:")
flota.pokaz_flote()









class PojazdInfo:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def info(self):
        return f"{self.marka} {self.model}, Rok: {self.rok_produkcji}"

class Samochod:
    def __init__(self, marka, model, rok_produkcji, liczba_drzwi):
        self.pojazd_info = PojazdInfo(marka, model, rok_produkcji)
        self.liczba_drzwi = liczba_drzwi

    def info(self):
        return f"{self.pojazd_info.info()}, Liczba drzwi: {self.liczba_drzwi}"

class Motocykl:
    def __init__(self, marka, model, rok_produkcji, pojemnosc_silnika):
        self.pojazd_info = PojazdInfo(marka, model, rok_produkcji)
        self.pojemnosc_silnika = pojemnosc_silnika

    def info(self):
        return f"{self.pojazd_info.info()}, Pojemność silnika: {self.pojemnosc_silnika} cm³"

class Flota:
    def __init__(self):
        self.pojazdy = []

    def dodaj_pojazd(self, pojazd):
        self.pojazdy.append(pojazd)

    def usun_pojazd(self, pojazd):
        self.pojazdy.remove(pojazd)

    def pokaz_flote(self):
        for pojazd in self.pojazdy:
            print(pojazd.info())

flota = Flota()

samochod1 = Samochod("Toyota", "Corolla", 2020, 

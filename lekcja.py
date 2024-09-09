class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0


    def get_tytul(self):
        return self._tytul


    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł jest za długi. Maksymalna długość to 20 znaków.")


    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen


    def inkrementuj_wypozyczenia(self):
        self._liczba_wypozyczen += 1


if __name__ == "__main__":

    film = Film()
    print("Domyślny tytuł:", film.get_tytul())
    print("Domyślna liczba wypożyczeń:", film.get_liczba_wypozyczen())

    film.set_tytul("Incepcja")
    print("Ustawiony tytuł:", film.get_tytul())

    print("Pobrany tytuł:", film.get_tytul())
    print("Pobrana liczba wypożyczeń:", film.get_liczba_wypozyczen())

    print("Liczba wypożyczeń przed inkrementacją:", film.get_liczba_wypozyczen())
    film.inkrementuj_wypozyczenia()
    print("Liczba wypożyczeń po inkrementacji:", film.get_liczba_wypozyczen())

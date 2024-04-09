# Klasa kontener do zarządzania róznymi typami danych
# W tym przypadku mamy pliki: lisy, krotki, slowniki i liczby, wszystkie zaimplmentowane w projekt
# Na samym dole mamy wywołanie filtór które podają nam takie informacje które zostały wpisane w funkcjach def
class Kontener:
    def __init__(self):
        self.dane = []

    def dodaj(self, element):
        self.dane.append(element)

    def usun(self, element):
        if element in self.dane:
            self.dane.remove(element)

    def wyswietl(self):
        for element in self.dane:
            print(element)

    def wyswietl_liczby_wieksze_niz_10(self): #wyswietlenie liczby wiekszej od 10
        for element in self.dane:
            if isinstance(element, int) and element > 10:
                print(element)

    def wyswietl_krotki_z_a(self): #wyswietlenie danych zawierajachych "a"
        for element in self.dane:
            if isinstance(element, tuple) and any('a' in str(elem) for elem in element):
                print(element)

    def wczytaj_z_pliku(self, sciezka_pliku, typ): #wczytnie plików
        with open(sciezka_pliku, 'r') as plik:
            for linia in plik:
                if typ == 'liczby':
                    try:
                        self.dodaj(int(linia.strip()))
                    except ValueError:
                        pass
                elif typ == 'listy':
                    self.dodaj([int(x) for x in linia.strip().split(',')])
                elif typ == 'krotki':
                    self.dodaj(tuple(linia.strip().split(',')))
                elif typ == 'slowniki':
                    klucz, wartosc = linia.strip().split(',')
                    self.dodaj({klucz: wartosc})

if __name__ == "__main__":
    kontener = Kontener()
    
    kontener.wczytaj_z_pliku('liczby.txt', 'liczby')

    kontener.wczytaj_z_pliku('listy.txt', 'listy')

    kontener.wczytaj_z_pliku('krotki.txt', 'krotki')

    kontener.wczytaj_z_pliku('slowniki.txt', 'slowniki')

    print("Zawartosc kontenera po wczytaniu danych:")
    kontener.wyswietl()

    #wyświetlenie żadanych informacji z filtracja
    print("\nLiczby wieksze niz 10:")
    kontener.wyswietl_liczby_wieksze_niz_10()

    print("\nKrotki zawierajace litere 'a':")
    kontener.wyswietl_krotki_z_a()
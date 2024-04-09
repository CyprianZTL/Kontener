# Kontener Danych 🗂️✨

Klasa `Kontener` służy do zarządzania różnymi typami danych - listami, krotkami, słownikami, i liczbami. 🔄

## Funkcjonalności
- `dodaj(element)`: Dodaje element do kontenera. ➕
- `usun(element)`: Usuwa element z kontenera, jeśli istnieje. ➖
- `wyswietl()`: Wyświetla wszystkie elementy w kontenerze. 👀
- `wyswietl_liczby_wieksze_niz_10()`: Wyświetla wszystkie liczby większe niż 10. 🔢
- `wyswietl_krotki_z_a()`: Wyświetla krotki zawierające literę 'a'. 🔍
- `wczytaj_z_pliku(sciezka_pliku, typ)`: Wczytuje dane z pliku w zależności od typu (liczby, listy, krotki, słowniki). 📁

## Przykład użycia
```python
kontener = Kontener()
kontener.wczytaj_z_pliku('liczby.txt', 'liczby')
kontener.wczytaj_z_pliku('listy.txt', 'listy')
kontener.wczytaj_z_pliku('krotki.txt', 'krotki')
kontener.wczytaj_z_pliku('slowniki.txt', 'slowniki')

print("Zawartość kontenera po wczytaniu danych:")
kontener.wyswietl()

# Wyświetlenie filtracji
print("\nLiczby większe niż 10:")
kontener.wyswietl_liczby_wieksze_niz_10()

print("\nKrotki zawierające literę 'a':")
kontener.wyswietl_krotki_z_a()

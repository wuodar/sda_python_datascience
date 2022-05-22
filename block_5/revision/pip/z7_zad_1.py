# Przed rozpoczęciem pracy z pip'em, pamiętaj swtorzyć środowisko wirtualne, jeszcze jeśli tego nie zrobiłeś (w folderze głównym repo).
# Następnie aktywuj środowisko:
#  - linux: komenda "source nazwa_srodowiska/bin/activate"
#  - windows: komenda "nazwa_srodowiska/Scripts/activate"
"""
Ja przełączyłam się na środowisko przez konsolę pycharma
"""
# Następnie:
# 1. zainstaluj biblioteki w wersjach zawartych w pliku requirements.txt w folderze głównym repo (mozesz to zrobic na dwa sposoby)
"""
pip installl -r requirements.txt
"""
# 2. sprawdz czy nie ma dostepnych nowszych wersji dla zainstalowanych bibliotek
"""
pip freeze #pozwala sprawdzić pakiety
pip list -o #wypisuje moduły,  dla ktorych są dostępne aktualizacje
"""
# 3. jezeli takowe sa, zaktualizuj je
"""
pip install -U
"""
# 4. poszukaj informacji o zainstalowanych bibliotekach, dowiedz sie, co dostarczaja do projektu (polecam szczeg�lnie biblioteke ipython)
"""
pip show
"""
# 5. poszukaj w pip biblioteki pylint
"""
pip search
"""
# 6. zainstaluj biblioteke pylint w wersji wyciagnietej z poprzedniego punktu
"""
pip install pylint
"""
# 7. dowiedz sie, co to takiego googlujac w internecie
"""
ni wim
"""
# 8. wybierz jeden ze swoich uprzednio stworzonych plik�w pythonowych i sprawdz jego poprawnosc z wykorzystaniem pylinta
# (komenda: pylint <sciezka_do_pliku>)
"""
pylint D:\KURS\sda_python_datascience\block_5\exercises\z5_zad_1_print_items_kopia.py
"""
# 9. jezeli wystepuja jakies pylintowe sugestie, dokonaj poprawek; pr�buj do momentu kiedy wynik nie wyniesie 10/10
"""
block_5\exercises\z5_zad_1_print_items_kopia.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
block_5\exercises\z5_zad_1_print_items_kopia.py:32:24: W0621: Redefining name 'first_name' from outer scope (line 19) (redefined-outer-name)
block_5\exercises\z5_zad_1_print_items_kopia.py:32:36: W0621: Redefining name 'last_name' from outer scope (line 20) (redefined-outer-name)
block_5\exercises\z5_zad_1_print_items_kopia.py:32:0: W0621: Redefining name 'pets' from outer scope (line 22) (redefined-outer-name)

"""
# 10. jak sadzisz, gdzie i do czego moze sie przydac taka biblioteka?
"""
pylint - python code static checker

Do sprawdzania czystości i czytelności kodu.
"""

# 11. sprawdz jakie biblioteki sa aktualnie zainstalowane na Twoim komputerze; przekieruj wynik do pliku
# 12. jaka jest r�znica miedzy poleceniami "pip list", a "pip freeze"? czy mozna z powodzeniem wykorzystac formaty generowane przez obydwie komendy (po uprzednim przekierowaniu do pliku) do zainstalowania paczki zaleznosci (bibliotek) w nowym projekcie? sprawdz
# 13. odinstaluj uprzednio zainstalowana biblioteke jedi
# 14. odinstaluj pozostale biblioteki, kt�rych nie bedziesz juz potrzebowal(a) -> opcjonalne
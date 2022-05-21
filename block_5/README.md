W Tworzenie nowego brancha
1. git status
    jeżeli brak zmian (nie ma niczego na czerwono)
# 2. jeżeli są jakieś zmiany, to zapiszmy je za pomocą "git stash" (to ukryje te zmiany przed gitem)
# 3. po stashu powinniśmy mieć czyste repo, czyli bez zmian względem ostatniego pulla/commita (czyli aktualizacji)
#    możemy teraz stworzyć swój branch, wpisując git checkout -b <nazwa_branchu>
# 4. Po stworzeniu brancha, możemy przywrócic zestashe'owane zmiany, komendą "git stash apply"
# 5. Następnie dodajemy zmieniono pliki do stage'a (git add -A, jeżeli w konsoli, można też w pycharm) i commitujemy je
#    (git commit -m "wiadomosc o zmianach")
# 6. Ostatnim krokiem jest wrzucenie zmian na github, czyli push
#    (w przypadku konsoli, piszemy git push --set-upstream origin <nazwa_brancha>, ale można w pucharmie za jednym razem z krokiem 5)

# 1. Przełącz się na branch main (git checkout main)
# 2. Zaktualizuj repo (git pull)
# 3. Przełącz się na swój branch (git checkout <nazwa_brancha>
# 4. Zmergeuj zmiany z maina (git merge main)
# 5. W przypadku konfliktów, rozwiaz je
# 6. Dodaj zmiany do swojego brancha (git add -A, git commit -m "wiadomosc")
# 7. (Opcjonalnie) wrzuć zmiany na github na swój branch (git push)
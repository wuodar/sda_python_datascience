""""
Stwórz klasę Song, przyjmującą w konstruktorzę listę wersów dowolnej piosenki.
Dodatkowo stwórz w klasie Song metodą print_song, wypisująca na ekran wersy utworu, linia po linii.
"""

"""
Działanie metody sing_me_a_song:
    >>> print happy_bday.sing_me_a_song()
    May god bless you,
    Have a sunshine on you,
    Happy Birthday to you !
"""

class Song:
    def __init__(self, text_of_song):
        self.text = text_of_song
        self.sing_me_a_song()

    def sing_me_a_song(self):
        for i in self.text:
            print(i)

tekst = ["Ala ma kota,", "Kot ma Alę,", "Pogoń na mistrza,", "Inaczej się nie bawię."]
piosenka = Song(tekst)

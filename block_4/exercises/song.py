"""
Napisz klasę Song, która będzie przyjmować w konstruktorze listę wersów tekstu piosenki
(wersów piosenki)
i zapiszę ją jako pole obiektu.
Napisz następnie metodę sing_me_a_song, która wyprintuje linia po linii tekst piosenki

Przykładowa lista wersów:
    >>> happy_bday = Song(["May god bless you, ",
    ...                    "Have a sunshine on you,",
    ...                    "Happy Birthday to you !"])

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
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
<<<<<<< HEAD
    def __init__(self, text_of_song):
        self.text = text_of_song
        self.sing_me_a_song()

    def sing_me_a_song(self):
        for i in self.text:
            print(i)

tekst = ["Ala ma kota,", "Kot ma Alę,", "Pogoń na mistrza,", "Inaczej się nie bawię."]
piosenka = Song(tekst)
=======
    def __init__(self, song_lines) -> None:
        self.song_lines = song_lines

    def print_song(self):
        for line in self.song_lines:
            print(line)


if __name__ == "__main__":
    toto_africa = [
        "I hear the drums echoing tonight",
        "But she hears only whispers of some quiet conversation",
        "She is coming in, 12:30 flight",
        "The moonlit wings reflect the stars that guide me towards salvation",
        "I stopped an old man along the way",
        "Hoping to find some old forgotten words or ancient melodies",
        "He turned to me as if to say",
        '"Hurry boy, it iss waiting there for you"',
    ]
    song = Song(toto_africa)
    song.print_song()
>>>>>>> main

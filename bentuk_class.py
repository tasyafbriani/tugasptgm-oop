import random

class Game_tebak_angka:
    def __init__(self):
        self.jawaban = random.randint(1, 10)

    def coba(self):
        tebakan = int(input('Tebak angka dari 1 s.d 10: '))

        if self.coba_tebakan(tebakan):
            print("Jawaban kamu benar!!")
        else:
            print("Jawaban kamu salah!!")

    def coba_tebakan(self, tebakan):
        return tebakan == self.jawaban

if __name__ == "__main__":
    game = Game_tebak_angka()
    game.coba()

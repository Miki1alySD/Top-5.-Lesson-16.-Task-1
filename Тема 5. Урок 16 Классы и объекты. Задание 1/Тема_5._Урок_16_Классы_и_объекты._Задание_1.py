class Cassa:

    summa = 27455 #колличество дененг в кассе
    
    def top_up(self, pokup):

        self.pokupka=pokup
        pokup+=Cassa.summa
        return f"В кассе {pokup}"

    def count_1000(self):
        print(Cassa.summa//1000)

    def take_away(self, x):
        if x <= self.summa:
            self.summa -= x
        else:
            return f"Недостаточно денег"

r=Cassa()
print(r.take_away(28000))
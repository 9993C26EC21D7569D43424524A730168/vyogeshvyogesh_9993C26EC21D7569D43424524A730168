class Player:
    def play(self):
        print("The player is playing cricket.")


class Batsman(Player):
    def play(self):
        print("The Batsman is batting.")


class Bowler(Player):
    def play(self):
        print("The Bowler is bowling.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
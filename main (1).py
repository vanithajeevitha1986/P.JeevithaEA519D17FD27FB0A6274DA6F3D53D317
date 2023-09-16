#Define the base class player 
class player:
  def play(self):
    print("The player is playing cricket.")
#define the Derived class batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")
#Define the Derived class bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")
#Create object of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play method for each object
batsman.play()
bowler.play()
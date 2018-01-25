class Rocket(object):
    """docstring for Rocket. Rocket simulates a rocket ship for a game.
    """
    def __init__(self):
        # Each rocket has an (x,y) position
        self.x = 0
        self.y = 0
    def move_up(self):
        #Increment the y-position of the Rocket
        self.y += 1


    def move_side(self):
        #Increment the x-position of the rocket
        self.x += 1

my_rocket = Rocket()
print("Rocket altitude: ", my_rocket.y)
my_rocket.move_up()
print("Rocket altitude: ", my_rocket.y)
my_rocket.move_up()
print("Rocket altitude: ", my_rocket.y)

class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0,rank=2):
        self.suit = self.suit_names[suit]
        if rank in self.faces: # self.rank handles printed representation
            self.rank = self.faces[rank]
        else:
            self.rank = rank
        self.rank_num = rank # To handle winning comparison

    def __str__(self):
        return "{} of {}".format(self.rank_num,self.suit)

testCard1 = Card(suit=1, rank=4)
print("Test Card suit: ", testCard1.suit)
print("Test Card rank: ", testCard1.rank)

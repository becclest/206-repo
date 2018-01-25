'''
SI 206 W18 Homework03: Classes and Inheritance

Your discussion section:
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

coco = Explore_pet()
brian = Explore_pet("Brian")

coco.boredom = 10
brian.hunger = 15

print (coco)
print (brian)
#your code begins here . . .

'''
Task B
'''
#For task B, add your code inside the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words = ["hello"]

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

    def clock_tick(self):
        current_hunger = self.hunger
        current_hunger += 2
        return current_hunger

        current_boredom = self.boredom
        current_boredom += 2
        return current_boredom

    def say(self):
        vocab = 'I know how to say:  ' + self.words + '\n'
        return vocab

    def teach(self, word):
        if self.boredom_decrement > self.boredom:
            boredom = 0

    def feed(self, word):
        if self.hunger_decrement > self.hunger:
            hunger = 0

bum = Pet("bum")
print (bum.hunger())
print (bum.boredom())
bum.clock_tick()
print (bum)

'''
Task C
'''

def teaching_session(my_pet,new_words):
    pass
  #your code goes here. Replace pass with your code . . .





#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .

'''
Task B: Poodle
'''
#your code begins here . . .

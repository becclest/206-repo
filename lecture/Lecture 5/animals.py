
class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs

  def greeting(self):
    return "cowers"

  def speak(self):
      return "groan"


class Dog(Animal):

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def greeting(self):
    return "wags"

  def speak(self):
    return "bark"

class Cow(Animal):
  
  def greeting(self):
    return "ring ring"

  def speak(self):
    return "moo"

class Bird(Animal):
  legs = 2

  def speak(self):
    return "chirp"

class Snake(Animal):
  legs = 0

  def greeting(self):
    return "slither"

  def speak(self):
    return "hiss"


class Spider(Animal):
  legs = 8


class Labrador(Dog):
  def __init__(self, nm):
    super().__init__(nm, 'Labrador')

  def greeting(self):
    return super().greeting() + " enthusiastically"


d1 = Dog('Fido', 'Australian Shepherd')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')
l1 = Labrador('Air Bud')

animals = [d1, c1, b1, s1, l1]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())

if isinstance(d1, Animal):
  print("A dog is an animal")
else:
  print("A dog is not an animal")

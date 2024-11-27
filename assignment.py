''' === ACTIVITY ONE === '''

#base clase
class Superhero:
  #initializing class
  def __init__(self, strength, rich, isHuman, canFly, villain):
    self.strength = strength
    self.rich = rich
    self.isHuman = isHuman
    self.canFly = canFly
    self.villain = villain
  
  def superProfile(self):
    print(f'\n{self.__class__.__name__} Profile')
    print(f"\nStrength: {self.strength}, Rich: {self.rich}, Human: {self.isHuman}, Can Fly: {self.canFly}, Nemesis: {self.villain}")


#superman class
class Superman(Superhero):
  def __init__(self, strength, rich, isHuman, canFly, villain, costume, location):
    super().__init__(strength, rich, isHuman, canFly, villain)
    self.costume = costume
    self.location = location

  def superMove(self):
    print(f'\n{self.__class__.__name__} fly over {self.location} in {self.costume}')

#batman class
class Batman(Superhero):
  def __init__(self, strength, rich, isHuman, canFly, villain, costume, location):
    super().__init__(strength, rich, isHuman, canFly, villain)
    self.costume = costume
    self.location = location

  def superMove(self):
    print(f'\n{self.__class__.__name__} drives Batmobile through {self.location} in {self.costume}')

#creating instances of Superhero class

superman = Superman('Super', False, False, True, 'Lex Luthor', 'Red cape and blue tight', 'Metropolis')
superman.superProfile()

batman = Batman('Average', True, True, False, 'Joker', 'Bat custume', 'Gotham City')
batman.superProfile()

#creating instances of Superman and Batman classes and calling superMove method

superman.superMove()

batman.superMove()

''' === ACTIVITY TWO === '''
class Car:
  def move(self):
    return 'Car drives very fast'
  

class Plane:
  def move(self):
    return 'Plane flies high'
  
for vehicle in [Car(), Plane()]:
  print(vehicle.move())
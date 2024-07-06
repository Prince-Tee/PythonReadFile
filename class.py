class Dog():
    def __init__ (self,breed,size):
      self.breed= breed
      self.size= size
      print("The dog {} is good for it's {}".format(self.breed,size))
    def eat (self,food):
          print('the {} eats {} in the morning'.format(self.breed, food))
    
dog= Dog('boerbull', '180lbs')
dog.eat('indomie')

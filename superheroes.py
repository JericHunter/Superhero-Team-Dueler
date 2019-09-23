import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
# myAbility = Ability("Goated",random.randint(2,7))
        pass
    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      return random.randint(0,self.max_damage)
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
      pass
if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
        pass
        # TODO: Create instance variables for the values passed in.
    def block(self):
        ''' Return a value between 0 and the value set by self.max_block.'''
  # TODO: Use random.randint(a, b) to select a random attack value.
        return random.randint(0,self.max_block)
        pass
class Hero:
    def __init__(self, name, current_health, starting_health = 100):
        '''Instance properties:
             abilities: List
             armors: List
             name: String
             starting_health: Integer
             current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name =  name
        self.starting_health = starting_health
        self.current_health = current_health
      # TODO: Initialize instance variables values as instance variables
      # (Some of these values are passed in above,
      # others will need to be set at a starting value)
      # abilities and armors are lists that will contain objects that we can use
        pass
    def add_ability(self, ability):
        self.abilities.append(ability)
  # TODO: Add ability object to abilities:List
        pass
    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)

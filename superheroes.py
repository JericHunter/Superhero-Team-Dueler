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
    def attack(self):
        total_damage = 0
        for hero in self.abilities:
            total_damage += hero.attack()
        return total_damage
        pass

    def add_armor(self, armor):
        self.armors.append(armor)
        pass

    def defend(self):
        total_defense = 0
        for hero in self.armors:
            total_defense += hero.block()
        return total_defense
        pass

    def take_damage(self, damage):
        self.current_health -= damage
        pass
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
        pass
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)
            opponent.take_damage(hero_attack)
        if self.is_alive() == False and opponent.is_alive() == False:
            print("Draw!")
        elif opponent.is_alive() == False:
            print(f'{self.name} won')
        elif self.is_alive() == False:
            print(f'{opponent.name} won')
  # TODO: Fight each hero until a victor emerges.
  # Print the victor's name to the screen.
        pass
if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.

            hero1 = Hero("Wonder Woman", 1000)
            hero2 = Hero("Dumbledore", 1000)
            ability1 = Ability("Super Speed", 300)
            ability2 = Ability("Super Eyes", 130)
            ability3 = Ability("Wizard Wand", 80)
            ability4 = Ability("Wizard Beard", 20)
            hero1.add_ability(ability1)
            hero1.add_ability(ability2)
            hero2.add_ability(ability3)
            hero2.add_ability(ability4)
            hero1.fight(hero2)

import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
# myAbility = Ability("Goated",random.randint(2,7))
    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      return random.randint(0,self.max_damage)
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.
        ability = Ability("Debugging Ability", 20)
        print(ability.name)
        print(ability.attack())

        pass
        pass

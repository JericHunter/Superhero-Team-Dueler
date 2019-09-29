from random import randint,choice
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

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)
        pass

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
    def __init__(self, name, starting_health = 100):
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
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
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
            self.add_kill(1)
            opponent.add_deaths(1)
        elif self.is_alive() == False:
            print(f'{opponent.name} won')
            opponent.add_kill(1)
            self.add_deaths(1)
  # TODO: Fight each hero until a victor emerges.
  # Print the victor's name to the screen.

    #TODO: Refactor this method to update the
    # number of kills the hero has when the opponent dies.
    # Also update the number of deaths for whoever dies in the fight
        pass
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
    # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills
    pass
    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
    # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    pass
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
  # TODO: Add the Hero object that is passed in to the list of heroes in
  # self.heroes
        self.heroes.append(hero)
        pass
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
            else:
                pass
        return 0
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        all_heroes = []
        for hero in self.heroes:
            all_heroes.append(hero.name)
        print(all_heroes)

        pass
    # Keep all your current code, but add these methods
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        # attacking = True
        # while attacking:
        #Randomly assigns order for the heroes to battle
        heroA = self.heroes[random.randint(0, (len(self.heroes))-1)]
        heroB = other_team.heroes[random.randint(0, (len(other_team.heroes))-1)]
        heroA.fight(heroB)
        pass

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(f" Hero: {hero.name} Kills: {hero.kills} Deaths: {hero.deaths} KD: {hero.kills/hero.deaths}")
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

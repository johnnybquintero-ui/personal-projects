import random

class Character:
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power
    
    def is_alive(self):
        return self.health > 0
    
    def reduce_health(self, amount):
        if not self.is_alive():
            return
        self.health = max(self.health - amount, 0)

    def random_hit(self):
        hit = random.randint(1, 100)
        return hit >= 30

class Player(Character):

    def take_damage(self, amount):
        if not self.is_alive():
            return
        
        self.reduce_health(amount)
        print(f"You've taken {amount} damage!")

        if not self.is_alive():
            print("GAME OVER!")

    def heal(self, amount):
        if self.health < 100:
            self.health = min(self.health + amount, 100)
            print(f"You healed back to {self.health}")

        elif self.health == 100:
            print("You are already full health!")

    def attack(self, enemy):

        if not self.is_alive():
            print("Player has expired.")
            return

        if not enemy.is_alive():
            print("STOP! It's dead. Jesus!")
            return

        if self.random_hit():
            enemy.take_damage(self.attack_power, self)

        else:
            print("You missed!")   

class Enemy(Character):

    def take_damage(self, amount, player):

        if not self.is_alive():
            return
        
        self.reduce_health(amount)
        print(f"The enemy has taken {amount} damage!")
        
        if not self.is_alive():
            print("ENEMY DEFEATED!")
            player.heal(20)
    
    def attack(self, player):

        if not player.is_alive():
            print("What part of GAME OVER did you not understand?")
            return

        if self.random_hit():
            player.take_damage(self.attack_power)

        else:
            print("Enemy missed!")
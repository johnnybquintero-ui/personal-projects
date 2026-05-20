import random

class Player:

    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, HP):
        if self.health <= 0:
            return
        
        self.health = max(self.health - HP, 0)
        print(f"You've taken {HP} damage!")

        if self.health == 0:
            print("GAME OVER!")

    def health_item(self, HP):
        if self.health < 100:
            self.health = min(self.health + HP, 100)
            print(f"You healed back to {self.health}")

        elif self.health == 100:
            print("You are already full health! Health item not required.")

    def attack(self, enemy):
        hit = random.randint(1, 100)
        if self.health <=0:
            print("Player has expired.")
            return

        if enemy.health <= 0:
            print("STOP! It's dead. Jesus!")

        elif hit >= 30 and enemy.health > 0:
            enemy.take_damage(self.attack_power, self)

        else:
                print("You missed!")   

class Enemy:
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, HP, player):
        if self.health > 0:
            self.health = max(self.health - HP, 0)
            print(f"The enemy has taken {HP} damage!")
        
        if self.health <= 0:
            print("ENEMY DEFEATED!")
            player.health_item(20)
    
    def attack(self, player):
        hit = random.randint(1, 100)
        if player. health <=0:
            print("What part of GAME OVER did you not understand?")
            return

        if hit >= 30 and player.health > 0:
            player.take_damage(self.attack_power)

        else:
            print("Enemy missed!")
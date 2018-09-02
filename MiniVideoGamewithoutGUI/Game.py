# Frederick A. Castaneda Jr.
# July 5, 2018 - July 8, 2018
# Mini-Video Game
# Lets you and your mate fight with each other
# Random damage for every attack
# You can add your own attack (just modify the code)
import random


class PlayerStats:
    def __init__(self, playerName, number):
        self.playerName = playerName
        self.number = number
        self.health = 100
        self.mana = 100
        self.power = 0


class PlayerSkills(PlayerStats):
    def thunderboltAttack(self):
        damage = random.randint(1, 30)
        print("{}: Used Thunderbolt Attack with the damage of {}".format(self.playerName, damage))
        return damage

    def magicAttack(self):
        damage = random.randint(5, 50)
        print("{}: Used Magic Attack with the damage of {}".format(self.playerName, damage))
        return damage

    def specialSkill(self):
        damage = 50
        print("{}: Used the SPECIAL SKILL ATTACK!! with the damage of {}".format(self.playerName, damage))
        return damage


class Player(PlayerSkills):
    def __init__(self, playerName, number):
        super().__init__(playerName, number)

    def __str__(self, playerName, enemyName, health, mana, power):
        print(f"{playerName}: Health: {health} Mana: {mana} Power: {power}")
        print(f"{playerName} lose!")
        print(f"{enemyName} YOU WIN!!!!")

    @staticmethod
    def menu(number, name, health, mana, power):
        print(f"\nPlayer {number}: {name}")
        print(f"{name}: Health: {health} Mana: {mana} Power: {power}\n")
        print(f"{name}: Choose your attack!!")
        print("1.) Thunderbolt Attack (1-30 damage)")
        print("2.) Magic Attack (5-50 damage)")
        print("3.) Special Skill (50 damage)")
        option = str(input("\nYour attack here: "))
        print("-----------------------------------------------------------------------")
        return option


print("Welcome to Fight Game!")
playerOneName = str(input("Player 1: Enter your name: "))
playerTwoName = str(input("Player 2: Enter your name: "))
playerOne = Player(playerOneName, 1)
playerTwo = Player(playerTwoName, 2)

while True:
    if playerOne.health >= 0 and playerTwo.health >= 0:
        while playerOne.health >= 0:
            optionOne = playerOne.menu(playerOne.number, playerOne.playerName, playerOne.health, playerOne.mana, playerOne.power)
            if optionOne == "1":
                playerOne.power += random.randint(1, 15)
                playerTwo.health -= playerOne.thunderboltAttack()
                print("{}: has {} power to use Special Skill".format(playerOne.playerName, playerOne.power))
                print("Player 2 Remaining Health: {} \n".format(playerTwo.health))
                break
            elif optionOne == "2":
                if playerOne.mana >= 0:
                    playerOne.mana -= random.randint(20, 30)
                    playerTwo.health -= playerOne.magicAttack()
                    playerOne.power += random.randint(5, 20)
                    print("Player 2 Remaining Health: {}".format(playerTwo.health))
                    print("{} has gained {} power to use Special Skill".format(playerOne.playerName, playerOne.power))
                    print("Your Remaining Mana: {}\n".format(playerOne.mana))
                    break
                else:
                    print("Sorry you don't have enough mana! Choose another attack!!\n")
            elif optionOne == "3":
                if playerOne.power >= 100:
                    playerTwo.health -= playerOne.specialSkill()
                    print("Player 2 Remaining Health: {} \n".format(playerTwo.health))
                    playerOne.power -= 100
                    break
                else:
                    print("Sorry you don't have power yet!! Choose another attack!!\n")
            else:
                print("Invalid Input!\n")

        while playerTwo.health >= 0:
            optionTwo = playerTwo.menu(playerTwo.number, playerTwo.playerName, playerTwo.health, playerTwo.mana, playerTwo.power)
            if optionTwo == "1":
                playerTwo.power += random.randint(1, 15)
                playerOne.health -= playerTwo.thunderboltAttack()
                print("{}: has {} power to use Special Skill".format(playerTwo.playerName, playerTwo.power))
                print("Player 1 Remaining Health: {} \n".format(playerOne.health))
                break
            elif optionTwo == "2":
                if playerTwo.mana >= 0:
                    playerTwo.mana -= random.randint(20, 30)
                    playerOne.health -= playerTwo.magicAttack()
                    playerTwo.power += random.randint(5, 20)
                    print("Player 1 Remaining Health: {}".format(playerOne.health))
                    print("You has gained {} power to use Special Skill".format(playerTwo.power))
                    print("Your Remaining Mana: {}\n".format(playerTwo.mana))
                    break
                else:
                    print("Sorry you don't have enough mana! Choose another attack!!\n")
            elif optionTwo == "3":
                if playerTwo.power >= 100:
                    playerOne.health -= playerTwo.specialSkill()
                    print("Player 1 Remaining Health: {} \n".format(playerOne.health))
                    playerTwo.power -= 100
                    break
                else:
                    print("Sorry you don't have enough power yet!!! Choose another attack!!\n")
            else:
                print("Invalid Input!\n")
    else:
        if playerOne.health <= 0:
            playerOne.__str__(playerOne.playerName, playerTwo.playerName, playerOne.health, playerOne.mana, playerOne.power)
            break
        else:
            playerTwo.__str__(playerTwo.playerName, playerOne.playerName, playerTwo.health, playerTwo.mana, playerTwo.power)
            break
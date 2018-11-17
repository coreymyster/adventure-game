# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.

from character import Character
from random import *

# Creates the character objects
def getCharacters():
    hero = Character("Daltor", 200, 20)
    sendor = Character("Sendor", 100, 35)
    ghost = Character("Ghost", 50, 7)
    zombifiedBat = Character("Zombified Bat", 50, 12)
    liveRock = Character("Live Rock", 40, 22)
    
    return hero, sendor, ghost, zombifiedBat, liveRock

# Generates a random enemy encounter for each turn if an enemy battle occurs
def enemyEncounter(sendor, ghost, zombifiedBat, liveRock):
    randomEncounter = random()
    
    if randomEncounter > .7:
        return ghost
    elif randomEncounter > .5 and randomEncounter <= .7:
        return liveRock
    elif randomEncounter > .1 and randomEncounter <= .5:
        return zombifiedBat
    elif randomEncounter <= .1:
        return sendor

# The game logic, determines what happens for each turn
def gameProgress(hero, sendor, ghost, zombifiedBat, liveRock):
    stepsRemaining = 10
    totalCoins = 0
    while stepsRemaining > 0:
        step = input("Only {} steps remaining. Step forward? (y/n) ".format(stepsRemaining))
        enemy = enemyEncounter(sendor, ghost, zombifiedBat, liveRock)    

        # Determines if the turn will result in coins or an enemy encounter
        coinsOrEnemy = random()
        
        if step == 'y':
            stepsRemaining -= 1
            
            # Generates coins
            if coinsOrEnemy > .6:
                randCoins = randrange(10, 100)
                totalCoins = totalCoins + randCoins
                print("You found {} coins!".format(randCoins))
            
            # Generates an enemy to fight if coins are not generated
            else:
                print("You've encountered {}! Time to fight!".format(enemy.name))
                print("")
                while enemy.getHealth() > 0 and hero.getHealth() > 0:
                    # Calculates enemy attacks on hero health and hero health on enemy attacks
                    hero.attack(hero.getHealth(), enemy.getAttackPower())
                    enemy.attack(enemy.getHealth(), hero.getAttackPower())
                    print("You attack {0} and caused {1} damage. {0} has {2} health left.".format(enemy.name, hero.getAttackPower(), enemy.getHealth()))
                    if enemy.getHealth() > 0:
                        print("{} attacks and caused {} damage. You have {} health left.".format(enemy.name, enemy.attackPower, hero.getHealth()))
                    elif enemy.getHealth() <= 0 and hero.getHealth() > 0:
                        print("")
                        print("Great job, you defeated {}! You have {} health left, so tread lightly.".format(enemy.name, hero.getHealth() + enemy.getAttackPower()))
                
                # Resets the health of the enemy incase there is another encounter
                enemy.resetEnemy(enemy.health)
                
            if hero.getHealth() >= 1 and stepsRemaining == 0:
                print("")
                print("Congratulations, you have deafeated Sendor and his army!")
                print("The Chest of Light you have opened will restore order to the kingdom")
                print("In addition to the chest, you also found {} coins along the way".format(totalCoins))
                print("Great job on battling your way through!")
            elif hero.getHealth() < 1:
                print("")
                print("Oh no! You have fallen to Sendor and his group of enemies.")
                print("You weren't strong enough to take back the Chest of Light and")
                print("restore order to the kingdom. Better luck next time.")
                break
        elif step == 'n':
            print("The only way to finish is to move forward")
    

def main():
    hero, sendor, ghost, zombifiedBat, liveRock = getCharacters()
    
    print("Welcome {}".format(hero.name))
    print("Sendor has found the black crystal sword and the only way")
    print("To defeat his presence is to open the chest of light at the")
    print("end of this dark cave. Try to make it through without encountering Sendor")
    
    gameProgress(hero, sendor, ghost, zombifiedBat, liveRock)
    
main()
class Character:
    def __init__(self, name, health, attackPower):
        self.name = name
        self.originalHealth = health
        self.health = health
        self.attackPower = attackPower
    
    def getHealth(self):
        if self.health < 1:
            self.health = 0
            return self.health
        else:
            return self.health
    
    def resetEnemy(self, enemyHealth):
        self.health = self.originalHealth
        return self.health
        
    def getAttackPower(self):
        return self.attackPower
    
    def attack(self, hero, enemy):
        self.health = hero - enemy
        return self.health
        
import pygame,random

class EnemySpaceShip():

    movementChange = 0.3
    imgList = ['./img/ufo-type-one.png', './img/ufo-type-two.png']

    def __init__(self):
        self.playerImg = pygame.image.load(random.choice(self.imgList))
        self.locationY = 0
        self.locationX = random.randint(0,770)
        self.movementChange = 0.5

    def move(self):
        self.locationX = self.locationX + self.movementChange
        # border limitation for the enemy
        if self.locationX >= 770 or self.locationX <= 0:
            self.movementChange = self.movementChange * (-1)
            self.locationY = self.locationY + 30


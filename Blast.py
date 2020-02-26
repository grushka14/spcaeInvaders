import pygame, random


class Blast():
    imgList = ['./img/explosion_four.png', './img/explosion_two.png', './img/explosion_three.png',
               './img/explosion_one.png']

    def __init__(self, locationX, locationY, img=random.choice(imgList)):
        self.img = pygame.image.load(img)
        self.locationY = locationY
        self.locationX = locationX
        self.timeToLive = 20

    def tick(self):
            self.timeToLive = self.timeToLive -1

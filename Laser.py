import pygame


class Laser():
    def __init__(self, locationX, locationY=480, img='./img/laser.png'):
        self.locationX = locationX
        self.locationY = locationY
        self.laserImg = pygame.image.load(img)

    # handling the movement of the laser
    def move(self):
        self.locationY = self.locationY - 0.5

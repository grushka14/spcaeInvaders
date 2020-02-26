import pygame


# player space ship class
class PlayerSpaceShip():

    def __init__(self, playerName='player1', img='./img/player-ship.png'):
        self.playerName = playerName
        self.playerImg = pygame.image.load(img)
        self.locationY = 480
        self.locationX = 370

    # handling the change of values for player movement
    def move(self, number):
        self.locationX = self.locationX + number
        # border limits for the player movement
        if self.locationX > 770:
            self.locationX = 770
        if self.locationX < 0:
            self.locationX = 0

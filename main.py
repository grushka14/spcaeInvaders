import pygame, time, schedule
import PlayerSpaceShipe, Laser, Enemy, Blast

running = True
screen_size = (800, 600)

# pygame initialization
pygame.init()

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

startTime = time.time()

def showScore():
    onScreenScore = font.render(f"Score: {score}", True, (255, 255, 255))
    addToScreen(onScreenScore, 10, 550)

def showTime():
    onScreenTime = font.render(f"Time: {round((time.time() - startTime),1)}", True, (255, 255, 255))
    addToScreen(onScreenTime, 600, 550)

# window settings
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('./img/alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('./img/background.jpg')

# player
player = PlayerSpaceShipe.PlayerSpaceShip()

# enemy
enemyList = [Enemy.EnemySpaceShip()]

def job():
    enemyList.append(Enemy.EnemySpaceShip())


schedule.every(2).seconds.do(job)
# laser
laserList = []

# explosion
explosionList = []


def addToScreen(img, x, y):
    screen.blit(img, (x, y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player controls
        playerMovementChange = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerMovementChange = - 0.3
            if event.key == pygame.K_RIGHT:
                playerMovementChange = 0.3
            if event.key == pygame.K_SPACE:
                laserList.append(Laser.Laser(player.locationX))

    screen.fill((0, 255, 255))
    screen.blit(background, (0, 0))
    player.move(playerMovementChange)

    # enemy
    schedule.run_pending()

    for ship in enemyList:
        if ship.locationY >= 480:
            print('x')
            running = False
        ship.move()
        addToScreen(ship.playerImg, ship.locationX, ship.locationY)

    # laser logic
    for beam in laserList:
        if beam.locationY <= 0:
            laserList.remove(beam)
        # laser/enemy collision logic
        for ship in enemyList:
            if ship.locationY <= beam.locationY <= ship.locationY + 30 and ship.locationX <= beam.locationX <= ship.locationX + 50:
                score = score + 1
                laserList.remove(beam)
                enemyList.remove(ship)
                explosionList.append(Blast.Blast(ship.locationX, ship.locationY))
        beam.move()
        addToScreen(beam.laserImg, beam.locationX, beam.locationY)

    # adding blasts to screen
    for blast in explosionList:
        if blast.timeToLive == 0:
            explosionList.remove(blast)
        blast.tick()

        addToScreen(blast.img, blast.locationX, blast.locationY)

    # adding score and time to screen
    showScore()
    showTime()
    # add player to screen
    addToScreen(player.playerImg, player.locationX, player.locationY)

    pygame.display.update()

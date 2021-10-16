import pygame
import time
import math
from utils import scale_image, blit_rotate_center

# Loading Images
GRASS = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/track1.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/track-border1.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/finish.png"), 0.8)
FINISH_POSITION = (90, 220)
FINISH_MASK = pygame.mask.from_surface(FINISH)

RED_CAR = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/red-car.png"), 0.4)
GREEN_CAR = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/green-car.png"), 0.4)
GREY_CAR = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/grey-car.png"), 0.4)
PURPLE_CAR = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/purple-car.png"), 0.4)
WHITE_CAR = scale_image(pygame.image.load("SmallProjects/PyGame/Car Game/assets/white-car.png"), 0.4)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

FPS = 60

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def boost(self):
        self.vel = max(self.vel - self.acceleration / 5, 0)
        self.move()

    def slow_mo(self):
        self.vel -= 1
        self.vel = 0.5
        self.move()

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi



class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (130, 180)

    def bounce(self):
        self.vel = -self.vel
        self.move()

    def reset(self):
        self.x,self.y = self.START_POS
        self.angle = 0
        self.vel = 0


def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()
    if keys[pygame.K_LSHIFT]:
        moved = True
        player_car.boost()
    if keys[pygame.K_LCTRL]:
        moved = True
        player_car.slow_mo()

    if not moved:
        player_car.reduce_speed()

run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(8, 8)


while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)

    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide != None:
        if finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            print("Finish")






pygame.quit()

import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((1200, 900))
color = (255, 87, 87)
pygame.display.set_caption("GAME")
a = False
d = False
initPoints = 10
Points = 0
continue_list = []


class Obstacles:
    def __init__(self, y):
        self.x = randint(0, 1175)
        self.y = y
        self.color_2 = (0, 0, 0)
        self.dimenx = 28
        self.dimeny = 28
        self.destroyable = False
        self.centerx = self.x + self.dimenx/2
        self.centery = self.y + self.dimeny/2

    def draw(self):
        pygame.draw.rect(window, self.color_2, (self.x, self.y, self.dimenx, self.dimeny))
        if 744 <= self.y <= 800 and (player.x - 28) <= self.x <= (player.x + 28):
            continue_list.append("FINISH GAME")
        else:
            self.move()
        if self.destroyable:
            if self.y <= bullet.yShoot <= self.y + 28 and self.x-20 <= bullet.myX <= self.x+30:
                self.y = -50
                randint(15, 1175)

    def move(self):
        self.y += 1
        self.check()

    def check(self):
        if self.y > 772:
            self.edit_positions()

    def edit_positions(self):
        self.y = 0
        self.x = randint(0, 1175)


class DestroyableObstacles(Obstacles):
    def __init__(self, y):
        super(). __init__(y)
        self.color_2 = (0, 255, 255)
        self.destroyable = True


class Coins(Obstacles):
    def __init__(self, y):
        super().__init__(y)
        self.x = randint(15, 1175)
        self.color_2 = (255, 255, 0)
        self.dimeny = 15
        self.y += 15
        self.points = 0

    def draw(self):
        pygame.draw.circle(window, self.color_2, (self.x, self.y), self.dimeny)
        if 744 <= self.y <= 800 and (player.x - 28) <= self.x <= (player.x + 28):
            self.points += 1
            self.y = -50
            self.x = randint(15, 1175)
        else:
            self.move()

    def edit_positions(self):
        super(). edit_positions()
        self.x = randint(15, 1175)


class Player:
    def __init__(self):
        self.x = 600
        self.y = 772
        self.color_2 = (255, 255, 255)
        self.dimenx = 28
        self.dimeny = 28
        self.ifShoot = False
        self.yShoot = 772
        self.myX = 0

    def draw(self):
        pygame.draw.rect(window, self.color_2, (self.x, self.y, self.dimenx, self.dimeny))
        if self.ifShoot:
            bullet.draw(self.myX, self.yShoot, self.dimenx, self.dimeny)
            self.yShoot -= 1
            if self.yShoot <= -10:
                self.ifShoot = False
                self.yShoot = 772

    def shoot(self):
        if not self.ifShoot:
            self.myX = self.x
        self.ifShoot = True


class Looser:
    def __init__(self):
        self.color_2 = (155, 155, 155)
        pygame.draw.rect(window, self.color_2, (60, 60, 1075, 200))
        text = pygame.font.Font(None, 120)
        text_looser = text.render("HAHA LOOOOOSER!!", 0, (0, 0, 0))
        window.blit(text_looser, (130, 130))


class Bullet:
    def __init__(self):
        self.myX = 0
        self.yShoot = 0
        self.dimenx = 0
        self.dimeny = 0
        self.centerx = self.myX + self.dimenx/2
        self.centery = self.yShoot + self.dimeny/2

    def draw(self, myX, yShoot, dimenx, dimeny):
        self.myX = myX
        self.yShoot = yShoot
        self.dimenx = dimenx
        self.dimeny = dimeny
        pygame.draw.rect(window, (0, 150, 0), (self.myX + 10, self.yShoot, self.dimenx - 15, self.dimeny))


player = Player()
bullet = Bullet()

ob1_1 = DestroyableObstacles(0)
ob1_2 = Obstacles(0)
ob1_3 = Obstacles(0)
ob1_4 = Obstacles(0)
ob1_5 = Obstacles(0)
ob1_6 = Obstacles(0)

ob2_1 = DestroyableObstacles(-100)  # Different
ob2_2 = Obstacles(-100)
ob2_3 = Obstacles(-100)
ob2_4 = Obstacles(-100)
ob2_5 = Obstacles(-100)
ob2_6 = Obstacles(-100)

ob3_1 = DestroyableObstacles(-200)
ob3_2 = Coins(-200)
ob3_3 = Obstacles(-200)
ob3_4 = Obstacles(-200)
ob3_5 = Obstacles(-200)
ob3_6 = Obstacles(-200)

ob4_1 = DestroyableObstacles(-300)
ob4_2 = Obstacles(-300)
ob4_3 = Obstacles(-300)
ob4_4 = Obstacles(-300)
ob4_5 = Obstacles(-300)
ob4_6 = Obstacles(-300)

ob5_1 = DestroyableObstacles(-400)
ob5_2 = Obstacles(-400)
ob5_3 = Obstacles(-400)
ob5_4 = Obstacles(-400)
ob5_5 = Obstacles(-400)
ob5_6 = Obstacles(-400)

ob6_1 = DestroyableObstacles(-500)
ob6_2 = Obstacles(-500)
ob6_3 = Obstacles(-500)
ob6_4 = Obstacles(-500)
ob6_5 = Obstacles(-500)
ob6_6 = Obstacles(-500)

ob7_1 = Coins(-600)  # Different
ob7_2 = DestroyableObstacles(-600)
ob7_3 = Obstacles(-600)
ob7_4 = Obstacles(-600)
ob7_5 = Obstacles(-600)
ob7_6 = Obstacles(-600)

ob8_1 = DestroyableObstacles(-700)
ob8_2 = Obstacles(-700)
ob8_3 = Obstacles(-700)
ob8_4 = Obstacles(-700)
ob8_5 = Obstacles(-700)
ob8_6 = Obstacles(-700)

ob9_1 = DestroyableObstacles(-800)
ob9_2 = Obstacles(-800)
ob9_3 = Obstacles(-800)
ob9_4 = Obstacles(-800)
ob9_5 = Obstacles(-800)
ob9_6 = Obstacles(-800)

while True:
    window.fill(color, (0, 0, 1200, 800))
    if len(continue_list) == 0:
        player.draw()

        ob1_1.draw()
        ob1_2.draw()
        ob1_3.draw()
        ob1_4.draw()
        ob1_5.draw()
        ob1_6.draw()

        ob2_1.draw()
        ob2_2.draw()
        ob2_3.draw()
        ob2_4.draw()
        ob2_5.draw()
        ob2_6.draw()

        ob3_1.draw()
        ob3_2.draw()
        ob3_3.draw()
        ob3_4.draw()
        ob3_5.draw()
        ob3_6.draw()

        ob4_1.draw()
        ob4_2.draw()
        ob4_3.draw()
        ob4_4.draw()
        ob4_5.draw()
        ob4_6.draw()

        ob5_1.draw()
        ob5_2.draw()
        ob5_3.draw()
        ob5_4.draw()
        ob5_5.draw()
        ob5_6.draw()

        ob6_1.draw()
        ob6_2.draw()
        ob6_3.draw()
        ob6_4.draw()
        ob6_5.draw()
        ob6_6.draw()

        ob7_1.draw()
        ob7_2.draw()
        ob7_3.draw()
        ob7_4.draw()
        ob7_5.draw()
        ob7_6.draw()

        ob8_1.draw()
        ob8_2.draw()
        ob8_3.draw()
        ob8_4.draw()
        ob8_5.draw()
        ob8_6.draw()

        ob9_1.draw()
        ob9_2.draw()
        ob9_3.draw()
        ob9_4.draw()
        ob9_5.draw()
        ob9_6.draw()

        Points = ob7_1.points + ob3_2.points
        if initPoints != Points:
            window.fill((50, 50, 50), (0, 800, 1200, 900))
            text = pygame.font.Font(None, 120)
            text_points = text.render(f"Points: {Points}", 0, (255, 255, 255))
            window.blit(text_points, (10, 810))
            initPoints = Points

    if len(continue_list) == 1:
        looser = Looser()
        ob7_1.points = 0
        ob3_2.points = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                a = True
            if event.key == K_d:
                d = True
            if event.key == K_SPACE:
                player.shoot()
            if event.key == K_r:
                continue_list.clear()
                ob1_1.y = 0
                ob1_2.y = 0
                ob1_3.y = 0
                ob1_4.y = 0
                ob1_5.y = 0
                ob1_6.y = 0

                ob2_1.y = -100
                ob2_2.y = -100
                ob2_3.y = -100
                ob2_4.y = -100
                ob2_5.y = -100
                ob2_6.y = -100

                ob3_1.y = -200
                ob3_2.y = -200
                ob3_3.y = -200
                ob3_4.y = -200
                ob3_5.y = -200
                ob3_6.y = -200

                ob4_1.y = -300
                ob4_2.y = -300
                ob4_3.y = -300
                ob4_4.y = -300
                ob4_5.y = -300
                ob4_6.y = -300

                ob5_1.y = -400
                ob5_2.y = -400
                ob5_3.y = -400
                ob5_4.y = -400
                ob5_5.y = -400
                ob5_6.y = -400

                ob6_1.y = -500
                ob6_2.y = -500
                ob6_3.y = -500
                ob6_4.y = -500
                ob6_5.y = -500
                ob6_6.y = -500

                ob7_1.y = -600
                ob7_2.y = -600
                ob7_3.y = -600
                ob7_4.y = -600
                ob7_5.y = -600
                ob7_6.y = -600

                ob8_1.y = -700
                ob8_2.y = -700
                ob8_3.y = -700
                ob8_4.y = -700
                ob8_5.y = -700
                ob8_6.y = -700

                ob9_1.y = -800
                ob9_2.y = -800
                ob9_3.y = -800
                ob9_4.y = -800
                ob9_5.y = -800
                ob9_6.y = -800

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                a = False
            if event.key == K_d:
                d = False
    if a:
        if player.x == 0:
            a = False
        else:
            player.x -= 1
    if d:
        if player.x == 1172:
            a = False
        else:
            player.x += 1

    pygame.display.update()

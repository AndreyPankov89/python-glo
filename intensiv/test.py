import pygame
import random
import time
import sys

class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30

        self.vx = 2
        self.vy = 2

    def show(self):
        pygame.draw.circle(self.display, self.color, (self.center_x, self.center_y), self.radius)

    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy

    def clear(self):
        pygame.draw.circle(self.display, pygame.Color('white'), (self.center_x, self.center_y), self.radius)

    def move(self):
        self.clear()
        self.go()
        self.show()

    def stop(self):
        self.vx = 0
        self.vy = 0

    def check_balls(self, width, height):
        if (self.center_x <= (width - self.radius) and self.center_x >= self.radius) and (
                self.center_y <= (height - self.radius) and self.center_y >= self.radius):
            return True

    def check_coords(self, width, height):
        x, y = pygame.mouse.get_pos()
        if ball.check_balls(width, height) and (x - self.center_x) ** 2 + (y - self.center_y) ** 2 < self.radius ** 2:
            return True

class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('green')
        width, height = display.get_size()

        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)

class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)
        self.color = pygame.Color('yellow')

        self.center_x = x
        self.center_y = y

class RandomPointMovableBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)

        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)
        while self.vx == 0 and self.vy == 0:
            self.vx = random.randint(-3, 3)
            self.vy = random.randint(-3, 3)

class BilliardBall(RandomPointMovableBall):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('blue')

    def go(self):
        super().go()

        width, height = self.display.get_size()
        if self.center_x <= self.radius or self.center_x >= width - self.radius:
            self.vx = -self.vx
        if self.center_y <= self.radius or self.center_y >= height - self.radius:
            self.vy = -self.vy
pygame.init()

width = 700
height = 400
color_bg = 255, 255, 255

display = pygame.display.set_mode((width, height))

display.fill(color_bg)

balls = []
for i in range(3):

    ball = BilliardBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
count = 0
count_left = 0
count_right = 0
count_top = 0
count_down = 0
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.check_coords(width, height):
                    ball.stop()
                    count += 1
                string = (f'Шаров поймано {count}')
                display.fill('white')
                font = pygame.font.SysFont('couriernew', 40)
                text = font.render(str(string), True, 'red')
                display.blit(text, (50, 50))
    display.fill('white')
    for ball in balls:
        ball.move()
        if ball.radius >= ball.center_x:
            count_left += 1
        if ball.radius >= ball.center_y:
            count_top += 1
        if width - ball.radius <= ball.center_x:
            count_right += 1
        if height - ball.radius <= ball.center_y:
            count_down += 1
    string_left = (f'Стукнулось о левую стенку {count_left}')
    string_top = (f'Стукнулось о верхнюю стенку {count_top}')
    string_right = (f'Стукнулось о правую стенку {count_right}')
    string_down = (f'Стукнулось о нижнюю стенку {count_down}')
    font = pygame.font.SysFont('couriernew', 20)
    text_left = font.render(str(string_left), True, 'red')
    display.blit(text_left, (50, 50))
    text_top = font.render(str(string_top), True, 'red')
    display.blit(text_top, (50, 100))
    text_right = font.render(str(string_right), True, 'red')
    display.blit(text_right, (50, 150))
    text_down = font.render(str(string_down), True, 'red')
    display.blit(text_down, (50, 200))

    pygame.display.flip()
    clock.tick(60)
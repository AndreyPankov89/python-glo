import pygame
import random
import time

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

pygame.init()

width = 700
height = 400
color_bg = 255, 255, 255

display = pygame.display.set_mode((width, height))

display.fill(color_bg)

balls = []
for i in range(10):
    ball = RandomPointMovableBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
count = 0
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == pygame.MOUSEBUTTONDOWN:

            for ball in balls:

                x, y = pygame.mouse.get_pos()
                if ball.check_balls(width, height) and (x - ball.center_x)**2 + (y - ball.center_y)**2 < ball.radius**2:
                    ball.stop()
                    count += 1
                string = (f'Шаров поймано {count}')
                screen = pygame.display.set_mode([700, 300])
                screen.fill('Red')
                font = pygame.font.SysFont('couriernew', 40)
                text = font.render(str(string), True, 'white')
                screen.blit(text, (50, 50))
    for ball in balls:
        ball.move()

    pygame.display.flip()
    clock.tick(60)

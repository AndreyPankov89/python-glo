import pygame as pg
import sys
import random
pg.init()

height = 768
width = 1024
BGCOLOR = pg.Color('white')
display = pg.display.set_mode((width, height))
display.fill(BGCOLOR)
class Ball():
    def __init__(self,display):
        self._display = display
        self._x = 100
        self._y = 100
        self._r = 30
        self._vx = 3
        self._vy = 3
        self._color = pg.Color('green')

    def draw(self):
        pg.draw.circle(self._display,self._color, (self._x, self._y), self._r)
    
    def clear(self):
        pg.draw.circle(self._display,BGCOLOR, (self._x, self._y), self._r)  
    
    def go(self):
        self._x += self._vx
        self._y += self._vy

    def move(self):
        self.clear()
        self.go()
        self.draw()

    def stop(self):
        self._vx = 0
        self._vy = 0

    def is_on_display(self):
        width, height = display.get_size()
        if (self._r < self._x < width - self._r) and (self._r < self._y < height - self._r):
            return True
        return False
    
    def is_catch(self, x, y):
        if ((x - self._x)**2 + (y - self._y)**2 <= self._r**2):
            return True
        return False

    def touch(self):
        if (self._x <= self._r):
            return 'left'
        if (self._x >= width - self._r):
            return 'right'
        if (self._y <= self._r):
            return 'up' 
        if (self._y >= height - self._r):
            return 'down'
        return ''

class RandomPountBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        width, height = display.get_size()
        a = self._r 
        bx = width - self._r
        by = height - self._r
        self._x = random.randint(a, bx)
        self._y = random.randint(a, by)
        print(self._x, self._y)

class RandomPountMoveableBall(RandomPountBall):
    def __init__(self, display):
        super().__init__(display)
        while True:
            vx = random.randint(-3, 3)
            vy = random.randint(-3, 3)
            if (vx != 0 or vy != 0):
                self._vx = vx
                self._vy = vy
                break
       
        print(self._vx, self._vy)

class BillyardBall(RandomPountMoveableBall):
    def __init__(self, display):
        super().__init__(display)

    def go(self):
        super().go()
        width, height = self._display.get_size()
        if (self._x <= self._r or self._x >= width - self._r):
            self._vx = - self._vx
        if (self._y <= self._r or self._y >= height - self._r):
            self._vy = - self._vy
class Text():
    def __init__(self, display):
        self._display = display
        self._font = pg.font.SysFont('couriernew',28)
        self._color = pg.Color('red');
        self._place = (10, 10)

    def set_place(self, x, y):
        self._place = (x, y)
    def print(self, text):
        text = self._font.render(str(text), True, self._color)
        self._display.blit(text, self._place)

balls = []

for i in range(3):
    ball = BillyardBall(display)
    ball.draw()
    balls.append(ball)


clock =pg.time.Clock()
left_text = Text(display)
left_text.set_place(10, 420)

right_text = Text(display)
right_text.set_place(980, 420)

up_text = Text(display)
up_text.set_place(500, 10)

down_text = Text(display)
down_text.set_place(500, 740)


counters = {'up': 0, 'down': 0, 'left': 0, 'right':0}
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        

    display.fill(BGCOLOR)
    
    for ball in balls:
        ball.move()
        touch = ball.touch()
        if (touch != ''):
            counters[touch] +=1

    left_text.print(counters['left'])
    right_text.print(counters['right'])
    up_text.print(counters['up'])
    down_text.print(counters['down'])
    pg.display.flip()
    clock.tick(54)
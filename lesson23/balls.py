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
            if (vx != 0):
                self._vx = vx
                break
        while True:
            vy = random.randint(-3, 3)
            if (vy != 0):
                self._vy = vy
                break
        print(self._vx, self._vy)

class Text():
    def __init__(self, display):
        self._display = display
        self._font = pg.font.SysFont('couriernew',12)
        self._color = pg.Color('red');
        self._place = (10, 10)

    def set_place(self, x, y):
        self._place = (x, y)
    def print(self, text : str):
        text = self._font.render(text, True, self._color)
        self._display.blit(text, self._place)

balls = []

for i in range(10):
    ball = RandomPountMoveableBall(display)
    ball.draw()
    balls.append(ball)


clock =pg.time.Clock()
counter_text = Text(display)
total_text = Text(display)
total_text.set_place(800, 10)
stop_counter = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                counter = 0
                for ball in balls:
                    ball.stop()
                    counter += 1 if ball.is_on_display() else 0
                counter_text.print(f'На экране {counter} мячей')
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            for ball in balls:
                if ball.is_on_display() and ball.is_catch(x, y):
                    ball.stop()
                    stop_counter += 1 
                
            display.fill(BGCOLOR)
            total_text.print(f'Поймано {stop_counter} мячей')

    
    for ball in balls:
        ball.move()
    pg.display.flip()
    clock.tick(24)
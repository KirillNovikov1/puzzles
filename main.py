import sys
import pygame
import os

FPS = 50

WHITE = (255, 255, 255)
pygame.init()
n = 8
width = 80
height = 80

start_size = (1600, 900)

margin = 1

window = pygame.display.set_mode(((width + margin) * n + margin, (height + margin) * n + margin))

screen = pygame.Surface(((width + margin) * n + margin, (height + margin) * n + margin))
koo = []
all_s = []
koor = []
grid = []
for row in range(n):
    grid.append([])
    for column in range(n):
        grid[row].append(0)

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        all_s.append(self)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.action = False
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[self.row][self.column] = 1


    def bum(self):
        if self.x < mp[0] < self.x + self.w and self.y < mp[1] < self.y + self.h:
            a = mp[0] - self.x
            b = mp[1] - self.y
            koor.append(a)
            koor.append(b)
            self.action = True
            c = self.x
            d = self.y
            koo.append(c)
            koo.append(d)

    def funtion(self):
        mp = pygame.mouse.get_pos()
        self.x = (mp[0] // (width + margin)) * (width + margin) + margin
        self.y = (mp[1] // (height + margin)) * (height + margin) + margin
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[koo[1] // (height + margin)][koo[0] // (width + margin)] = 0
        if grid[self.row][self.column] == 1:
            self.x = koo[0]
            self.y = koo[1]

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def mouv(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0] - koor[0]
        self.y = pos[1] - koor[1]
        if self.x < -10:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.x + width > ((margin + width) * n + 10 + margin):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y < -10:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y + height > ((margin + height) * n + 10 + margin):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False

    def mesto(self):
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[self.row][self.column] = 1

def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["  Добро пожаловать в игру Puzzles", '',
                  "  Собери Картинку и пройди игру", '',
                  "Нажмите любую кнопку, чтобы начать"]
    fon = pygame.transform.scale(load_image('fon.jpg'), start_size)
    window.blit((fon), (0, 0))
    font = pygame.font.Font(None, 45)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 45
        text_coord += intro_rect.height
        window.blit(string_rendered, intro_rect)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                terminate()
            elif e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


hero1 = Sprite((width + margin) * (0) + margin, margin + (height + margin) * (0), ('data/fores_01.gif'))
hero2 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (1), ('data/fores_02.gif'))
hero3 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (2), ('data/fores_05.gif'))
hero4 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (3), ('data/fores_03.gif'))
hero5 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (4), ('data/fores_04.gif'))
hero6 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (5), ('data/fores_06.gif'))
hero17 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (6), ('data/fores_17.gif'))
hero18 = Sprite(margin + (width + margin) * (n - 8), margin + (height + margin) * (7), ('data/fores_18.gif'))

hero7 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (0), ('data/fores_07.gif'))
hero8 = Sprite((width + margin) * (2) + margin, margin + (height + margin) * (n - 8), ('data/fores_08.gif'))
hero9 = Sprite((width + margin) * (3) + margin, margin + (height + margin) * (n - 8), ('data/fores_09.gif'))
hero10 = Sprite((width + margin) * (4) + margin, margin + (height + margin) * (n - 8), ('data/fores_10.gif'))
hero11 = Sprite((width + margin) * (5) + margin, margin + (height + margin) * (n - 8), ('data/fores_11.gif'))
hero12 = Sprite((width + margin) * (6) + margin, margin + (height + margin) * (n - 8), ('data/fores_12.gif'))
hero13 = Sprite((width + margin) * (4) + margin, margin + (height + margin) * (4), ('data/fores_13.gif'))

hero14 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (0), ('data/fores_14.gif'))
hero15 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (1), ('data/fores_15.gif'))
hero16 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (2), ('data/fores_16.gif'))
hero19 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (3), ('data/fores_19.gif'))
hero20 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (4), ('data/fores_20.gif'))
hero21 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (5), ('data/fores_21.gif'))
hero22 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (6), ('data/fores_22.gif'))
hero23 = Sprite((width + margin) * (7) + margin, margin + (height + margin) * (7), ('data/fores_23.gif'))

hero24 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (7), ('data/fores_24.gif'))
hero25 = Sprite((width + margin) * (n - 6) + margin, margin + (height + margin) * (7), ('data/fores_25.gif'))
hero26 = Sprite((width + margin) * (n - 5) + margin, margin + (height + margin) * (7), ('data/fores_26.gif'))
hero27 = Sprite((width + margin) * (n - 4) + margin, margin + (height + margin) * (7), ('data/fores_27.gif'))
hero28 = Sprite((width + margin) * (n - 3) + margin, margin + (height + margin) * (7), ('data/fores_28.gif'))
hero29 = Sprite((width + margin) * (6) + margin, margin + (height + margin) * (7), ('data/fores_29.gif'))

hero30 = Sprite((width + margin) * (3) + margin, margin + (height + margin) * (4), ('data/fores_30.gif'))
hero31 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (1), ('data/fores_31.gif'))
hero32 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (2), ('data/fores_32.gif'))
hero33 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (3), ('data/fores_33.gif'))
hero34 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (4), ('data/fores_34.gif'))
hero35 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (5), ('data/fores_35.gif'))
hero36 = Sprite((width + margin) * (1) + margin, margin + (height + margin) * (6), ('data/fores_36.gif'))
dum = True

start_screen()
clock = pygame.time.Clock()

while dum:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:

            mp = pygame.mouse.get_pos()
            for i in all_s:
                i.bum()

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:

            for i in all_s:
                if i.action:
                    i.funtion()
            for i in all_s:
                i.action = False

            for i in all_s:
                i.mesto()
            koor = []
            koo = []
        for i in all_s:
            if i.action:
                i.mouv()

    for i in all_s:
        i.render()

    window.blit(screen, (0, 0))

    pygame.display.flip()

    clock.tick(FPS)
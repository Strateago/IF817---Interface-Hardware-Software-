import pygame
from pygame.locals import *
from sys import exit
import random
import os, sys
from fcntl import ioctl

pygame.init()

RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

fd = os.open(sys.argv[1], os.O_RDWR)
button = 0
k = 0.79
i = 0
mult = 1
score = 0
counter = 0
hearts = 3
width = 700
height = 466
i_sugar = random.randint(0,3)
i_mug = 0
positions_sugar = 63, 238, 415, 605
v_sugar = 10
X_sugar = positions_sugar[i_sugar]
Y_sugar = 40
positions_mug = 38, 213, 390, 585
X_mug = positions_mug[i_mug]
Y_splash = 338
MOVE_MUG = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

Font = pygame.font.SysFont('franklingothicmedium', 25, False, False)
Font1 = pygame.font.SysFont('franklingothicmedium', 25, True, False)
Font2 = pygame.font.SysFont('franklingothicmedium', 25, False, True)
Font3 = pygame.font.SysFont('franklingothicmedium', 50, False, True)
screen = pygame.display.set_mode((width, height))
sugar = pygame.image.load('sugar.png')
sugar = pygame.transform.scale(sugar, (50, 50))
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (700, 466))
menu_background = pygame.image.load('menu_background.jpeg').convert()
menu_background = pygame.transform.scale(menu_background, (700, 466))
mug = pygame.image.load('mug.png')
heart = pygame.image.load(('heart.png'))
heart = pygame.transform.scale(heart, (50, 50))
dead_heart = pygame.image.load('dead_heart.png')
dead_heart = pygame.transform.scale(dead_heart, (50, 50))
mug = pygame.transform.scale(mug, (100, 100))

class Splash(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Splash0.png'))
        self.sprites.append(pygame.image.load('Splash1.png'))
        self.sprites.append(pygame.image.load('Splash2.png'))
        self.sprites.append(pygame.image.load('Splash3.png'))
        self.sprites.append(pygame.image.load('Splash4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()

        self.animate = False

    def splash(self):
        self.animate = True

    def update(self, X_mug):
        self.rect.topleft = X_mug, Y_splash
        if self.animate == True:
            if self.atual == 0:
                self.atual = self.atual + 1
            else:
                self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animate = False
            self.image = self.sprites[int(self.atual)]

def draw_text(text, font, color, x, y): # Funcao para facilitar a escrita de texto
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

Game_Sprites = pygame.sprite.Group()
Splash_ = Splash()
Game_Sprites.add(Splash_)
clock = pygame.time.Clock()

screen.fill(BLACK)

parte_jogo = 0

while True:
    clock.tick(30)
    screen.fill(BLACK)

    if parte_jogo == 0: #MENU
        score = 0
        hearts = 3

        data_red = 0x00000000
        ioctl(fd, WR_RED_LEDS)
        os.write(fd, data_red.to_bytes(4, 'little'))

        data_green = 0x00000000
        ioctl(fd, WR_GREEN_LEDS)
        os.write(fd, data_green.to_bytes(4, 'little'))

        data_R = 0xFFFFFFFF
        ioctl(fd, WR_R_DISPLAY)
        os.write(fd, data_R.to_bytes(4, 'little'))

        screen.blit(menu_background, (0, 0))
        counter += 1
        # Faz o texto "START GAME" piscar
        draw_text('Sweeten The Coffee', Font3, WHITE, 180, 90)
        draw_text('Press Any Button to Start', Font2, WHITE, 240, 340)
        draw_text('Press ESC to Quit', Font2, WHITE, 265, 365)

        # Nomes dos autores no canto inferior direito
        draw_text('Thiago Costa @tjgc', Font2, WHITE, width - 190, height - 75)
        draw_text('Amanda Lima @acfml', Font2, WHITE, width - 190, height - 60)
        draw_text('Pedro César @pcgr', Font2, WHITE, width - 190, height - 45)
        draw_text('Lígia Ferro @lfblcp', Font2, WHITE, width - 190, height - 30)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ioctl(fd, RD_PBUTTONS)
        button = os.read(fd, 4)
        if int.from_bytes(button, 'little') != 15:
            parte_jogo = 1

        ioctl(fd, RD_SWITCHES)
        switches = os.read(fd, 4)
        num = int.from_bytes(switches, 'little')

        binario = bin(num)
        mult = 0
        for a in range(len(binario)):
            if binario[a] == '1':
                mult += 1
        v_sugar = 10 + mult*k

        dezena = mult//10
        unidade = mult%10
        if dezena == 0:
            data_L = 0x40000000
        elif dezena == 1:
            data_L = 0x79000000
        if unidade == 0:
            data_L += 0x40FFFF
        elif unidade == 1:
            data_L += 0x79FFFF
        elif unidade == 2:
            data_L += 0x24FFFF
        elif unidade == 3:
            data_L += 0x30FFFF
        elif unidade == 4:
            data_L += 0x19FFFF
        elif unidade == 5:
            data_L += 0x12FFFF
        elif unidade == 6:
            data_L += 0x02FFFF
        elif unidade == 7:
            data_L += 0x78FFFF
        elif unidade == 8:
            data_L += 0x00FFFF
        elif unidade == 9:
            data_L += 0x10FFFF
        ioctl(fd, WR_L_DISPLAY)
        os.write(fd, data_L.to_bytes(4, 'little'))

    elif parte_jogo == 1: #JOGO

        dezena = mult//10
        unidade = mult%10
        if dezena == 0:
            data_L = 0x40000000
        elif dezena == 1:
            data_L = 0x79000000
        if unidade == 0:
            data_L += 0x400000
        elif unidade == 1:
            data_L += 0x790000
        elif unidade == 2:
            data_L += 0x240000
        elif unidade == 3:
            data_L += 0x300000
        elif unidade == 4:
            data_L += 0x190000
        elif unidade == 5:
            data_L += 0x120000
        elif unidade == 6:
            data_L += 0x020000
        elif unidade == 7:
            data_L += 0x780000
        elif unidade == 8:
            data_L += 0x000000
        elif unidade == 9:
            data_L += 0x100000

        screen.blit(background, (0, 0))
        screen.blit(sugar, (X_sugar, Y_sugar))
        screen.blit(mug, (X_mug, 380))
        if hearts == 1:
            screen.blit(dead_heart, (550, 20))
            screen.blit(dead_heart, (600, 20))
            screen.blit(heart, (650, 20))
        if hearts == 2:
            screen.blit(dead_heart, (550, 20))
            screen.blit(heart, (600, 20))
            screen.blit(heart, (650, 20))
        if hearts == 3:
            screen.blit(heart, (550, 20))
            screen.blit(heart, (600, 20))
            screen.blit(heart, (650, 20))

        ioctl(fd, RD_PBUTTONS)
        button = os.read(fd, 4) 
        if int.from_bytes(button, 'little') == 7:
            i_mug = 0
        elif int.from_bytes(button, 'little') == 11:
            i_mug = 1
        elif int.from_bytes(button, 'little') == 13:
            i_mug = 2
        elif int.from_bytes(button, 'little') == 14:
            i_mug = 3
            
        X_mug = positions_mug[i_mug]

        Y_sugar = Y_sugar + v_sugar
        if 350 <= Y_sugar <= 380 and i_mug == i_sugar:
            score = score + 1
            Splash_.splash()
            Game_Sprites.draw(screen)
            Game_Sprites.update(X_mug)
            Y_sugar = 40
            i_sugar = random.randint(0, 3)
            X_sugar = positions_sugar[i_sugar]
        elif Y_sugar >= 380:
            Y_sugar = 40
            i_sugar = random.randint(0, 3)
            hearts = hearts - 1
            screen.blit(dead_heart, (600, 20))
            X_sugar = positions_sugar[i_sugar]
        
        if hearts == 0:
            data_L += 0x4040
        elif hearts == 1:
            data_L += 0x4079
        elif hearts == 2:
            data_L += 0x4024
        elif hearts == 3:
            data_L += 0x4030
        ioctl(fd, WR_L_DISPLAY)
        os.write(fd, data_L.to_bytes(4, 'little'))

        dezena = score//10
        unidade = score%10
        if dezena == 0:
            data_R = 0x40404000
        elif dezena == 1:
            data_R = 0x40407900
        if unidade == 0:
            data_R += 0x40
        elif unidade == 1:
            data_R += 0x79
        elif unidade == 2:
            data_R += 0x24
        elif unidade == 3:
            data_R += 0x30
        elif unidade == 4:
            data_R += 0x19
        elif unidade == 5:
            data_R += 0x12
        elif unidade == 6:
            data_R += 0x02
        elif unidade == 7:
            data_R += 0x78
        elif unidade == 8:
            data_R += 0x00
        elif unidade == 9:
            data_R += 0x10
        ioctl(fd, WR_R_DISPLAY)
        os.write(fd, data_R.to_bytes(4, 'little'))

        if hearts == 0 :
            counter = 0
            parte_jogo = 2
            data_red = 0xFFFFFFFF
            ioctl(fd, WR_RED_LEDS)
            os.write(fd, data_red.to_bytes(4, 'little'))
            pygame.time.delay(500)

        if score == 15:
            counter = 0   
            parte_jogo = 2
            data_green = 0xFFFFFFFF
            ioctl(fd, WR_GREEN_LEDS)
            os.write(fd, data_green.to_bytes(4, 'little'))
            pygame.time.delay(500)

        Game_Sprites.draw(screen)
        Game_Sprites.update(X_mug)
        pygame.display.flip()

    elif parte_jogo == 2: #TELA FINAL

        screen.blit(background, (0, 0))

        counter += 1

        # Faz o texto "GAME OVER" piscar
        if counter // 180 % 2 == 0:
            draw_text('GAME OVER', Font3, RED, 20, 20)

        draw_text('Press Any Button to Return to Menu', Font2, WHITE, 20, 70)
        draw_text('Press ESC to Quit', Font2, WHITE, 20, 110)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ioctl(fd, RD_PBUTTONS)
        button = os.read(fd, 4)
        if int.from_bytes(button, 'little') != 15:
            parte_jogo = 0
            pygame.time.delay(500)
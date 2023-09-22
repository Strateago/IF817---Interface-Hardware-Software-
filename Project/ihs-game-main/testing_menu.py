import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 700, 466
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Over Menu Test')

# Fonts and Background
Font3 = pygame.font.SysFont('franklingothicmedium', 50, False, True)
Font2 = pygame.font.SysFont('franklingothicmedium', 30, False, True)
Font1 = pygame.font.SysFont('franklingothicmedium', 20, False, True)
background = pygame.image.load('menu_background.jpeg').convert()
background_inicial = pygame.image.load('background_inicial.jpeg').convert()

background = pygame.transform.scale(background, (700, 466))
background_inicial = pygame.transform.scale(background_inicial, (700, 466))

# Global variable to control game over state
END_GAME = True  # Simulating that the game has ended

def draw_text(text, font, color, x, y): # Funcao para facilitar a escrita de texto
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

# Função para o Menu de game over
def game_over_menu():
    global END_GAME
    counter = 0

    while END_GAME:
        screen.blit(background, (0, 0))

        counter += 1

        # Faz o texto "GAME OVER" piscar
        if counter // 180 % 2 == 0:
            draw_text('GAME OVER', Font3, RED, 20, 20)

        draw_text('Press R to Restart', Font2, WHITE, 20, 70)
        draw_text('Press Q to Quit', Font2, WHITE, 20, 110)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    END_GAME = False

# Função do menu inicial
def start_menu():
    counter = 0

    while True:
        screen.blit(background_inicial, (0, 0))

        counter += 1

        # Faz o texto "START GAME" piscar
        if counter // 330 % 2 == 0:
            draw_text('Sweeten The Coffee', Font3, BLACK, 190, 155)
            draw_text('Press S to Start', Font2, WHITE, 270, 290)
            draw_text('Press Q to Quit', Font2, WHITE, 270, 320)

        # Nomes dos autores no canto inferior direito
        draw_text('Thiago Costa @ tjgc', Font1, BLACK, width - 180, height - 70)
        draw_text('Amanda Lima @ ', Font1, BLACK, width - 180, height - 55)
        draw_text('Pedro César @pcgr', Font1, BLACK, width - 180, height - 40)
        draw_text('Lígia Ferro @ lfblcp', Font1, BLACK, width - 180, height - 25)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_s:
                    return  # Retorna para o jogo principal

# Run the function to display the start menu
start_menu()

# Run the function to display the game over menu
game_over_menu()
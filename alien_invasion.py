#Classes do python
import pygame
from pygame.sprite import Group

#Minhas classes
from settings import Settings
from ship import Ship

#Meus módulos
import game_functions as gf


def run_game(): #Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_setting = Settings() #Instância das configurações
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height)) 
    ship = Ship(ai_setting, screen)
    #Dimensões da janela em pixels
    bullets = Group()
    pygame.display.set_caption('Alien Invasion') #Título da janela
    """ bg_color = (230, 230, 230) #Cor para janela é uma tupla em RGB """
    while True: #Laço para deixa a janela aberta
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        
        gf.update_screen(ai_setting, screen, ship, bullets)
        """ 
        Refatoração de código
        screen.fill(ai_setting.bg_color) #Método que aceita o argumento em forma de tupla para definir uma cor
        ship.blitme()
        pygame.display.flip() #Sempre atualiza a janela 
        """

run_game()

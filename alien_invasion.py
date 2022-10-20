#Classes do python
import pygame

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
    pygame.display.set_caption('Alien Invasion') #Título da janela
    """ bg_color = (230, 230, 230) #Cor para janela é uma tupla em RGB """
    while True: #Laço para deixa a janela aberta
        gf.Check_events(ship)
        ship.update()
        gf.Update_screen(ai_setting, screen, ship)
        """ 
        Refatoração de código
        screen.fill(ai_setting.bg_color) #Método que aceita o argumento em forma de tupla para definir uma cor
        ship.blitme()
        pygame.display.flip() #Sempre atualiza a janela 
        """

run_game()

import sys
import pygame

def Check_events(): #Responde a eventos de presionamento de teclas e de mouse.
    for event in pygame.event.get(): #O método pygame.event.get() recebe os movimento de teclado e mouse
        if event.type == pygame.QUIT: #Caso o evento seja que QUIT a janela fecha
            sys.exit()


def Update_screen(ai_settings, screen, ship): #Atualiza as imagens na tela e alterna para nova tela
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
import sys
import pygame


def Check_events(ship): #Responde a eventos de presionamento de teclas e de mouse.
    for event in pygame.event.get(): #O método pygame.event.get() recebe os movimento de teclado e mouse
        if event.type == pygame.QUIT: #Caso o evento seja que QUIT a janela fecha
            sys.exit()
        elif(event.type == pygame.KEYDOWN): #KEYDOW acontece quando eu preciono uma tecla
            if(event.key == pygame.K_RIGHT):
                ship.moving_right = True
            elif(event.key == pygame.K_LEFT):
                ship.moving_left = True
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_RIGHT): #KEYUP acontece quando eu solto uma tecla
                ship.moving_right = False
            if(event.key == pygame.K_LEFT):
                ship.moving_left = False
            


def Update_screen(ai_settings, screen, ship): #Atualiza as imagens na tela e alterna para nova tela
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
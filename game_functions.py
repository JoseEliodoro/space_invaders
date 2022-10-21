from pygame.sprite import Group
import sys
import pygame

from bullet import Bullet


def check_events(ai_setting, screen, ship, bullets): #Responde a eventos de presionamento de teclas e de mouse.
    for event in pygame.event.get(): #O método pygame.event.get() recebe os movimento de teclado e mouse
        if event.type == pygame.QUIT: #Caso o evento seja que QUIT a janela fecha
            sys.exit()
        elif(event.type == pygame.KEYDOWN): #KEYDOW acontece quando eu pressiono uma tecla
            check_keydown_events(event,ai_setting, screen, ship, bullets)
        if(event.type == pygame.KEYUP): #KEYUP acontece quando eu solto uma tecla
           check_keyup_events(event, ship)
            

def check_keydown_events(event, ai_setting, screen, ship, bullets): #Responde a prissionamentos de teclas.
    if(event.key == pygame.K_RIGHT):
        ship.moving_right = True
    elif(event.key == pygame.K_LEFT):
        ship.moving_left = True
    elif(event.key == pygame.K_SPACE):
        fire_bullet(ai_setting, screen, ship, bullets)
        


def check_keyup_events(event, ship): #Responde a solturas de tecla.
    if(event.key == pygame.K_RIGHT): 
        ship.moving_right = False
    elif(event.key == pygame.K_LEFT):
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets): #Atualiza as imagens na tela e alterna para nova tela
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    
    
def update_bullets(bullets): #Atualiza as posições dos projéteis e se livra dos antigos
    bullets.update() #Executa especificamento o método update para todos os elementod do grupo
    for bullet in bullets.copy(): 
        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet)
            

def fire_bullet(ai_setting, screen, ship, bullets): #Dispara um projétil se o limite não foi alcançado.
    if(len(bullets) < ai_setting.bullets_allowed):
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)
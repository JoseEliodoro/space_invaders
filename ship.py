import pygame

class Ship():
    def __init__(self, ai_settings, screen): #Inicializa a espaçonave e define sua posição inicial.
        self.ai_settings = ai_settings
        self.screen = screen #Carrega a imagem da espaçonave o obtém seu rect
        self.image = pygame.image.load('images/ship.bmp') #Obtém o caminho da imagem
        
        self.moving_right = False #Flag de movimento
        self.moving_left = False #Flag de movimento
        
        """ 
        rect é o posicinamento do elemento 
        posicinamento em retangulo
        """
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx 
        #Atributos do rect center, centerx, centery, top, bottom, left, right, x ou y
        self.rect.bottom = self.screen_rect.bottom
        #Inicia cada nova espaçonave na parte inferior central da janela

        self.center = float(self.rect.centerx)
    
    def update(self): #Atualiza a posição da espaçonave de acordo com a flag de movimento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    
    
    def blitme(self): #Desenha a espaçonave em sua posição atual.
        self.screen.blit(self.image, self.rect)
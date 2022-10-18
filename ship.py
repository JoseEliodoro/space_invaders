import pygame

class Ship():
    def __init__(self, screen): #Inicializa a espaçonave e define sua posição inicial.
        self.screen = screen #Carrega a imagem da espaçonave o obtém seu rect
        self.image = pygame.image.load('images/ship.bmp') #Obtém o caminho da imagem
        
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
        
    def blitme(self): #Desenha a espaçonave em sua posição atual.
        self.screen.blit(self.image, self.rect)
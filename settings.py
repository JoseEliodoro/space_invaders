class Settings(): #Classe que armazena as configurações do jogo.
    def __init__(self): #Inicializa as configurações do jogo.
        self.screen_width = 1200 #Largura da janela
        self.screen_height = 800 #Altura da janela
        self.bg_color = (230, 230, 230) #Cor da janela
        self.ship_speed_factor = 1.5
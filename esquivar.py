import pygame
import sys
import random

class Jugador(pygame.Rect):
    def __init__(self, velocity, right_key, left_key, *args, **kwargs):
        self.velocity = velocity
        self.right_key = right_key
        self.left_key = left_key
        super().__init__(*args, **kwargs)
    def mover_jugador(self, board_width):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.right_key]:
            if self.x + self.velocity < board_width - self.width:
                self.x += self.velocity

        if keys_pressed[self.left_key]:
            if self.x - self.velocity > 0:
                self.x -= self.velocity

class Obstaculo (pygame.Rect):
    def __init__(self, velocity,  *args, **kwargs):
        self.velocity = velocity
        super().__init__(*args, **kwargs)
    def mover_obstaculo(self):
        self.y += self.velocity
      
class Juego:
    ALTO = 600
    ANCHO = 800
    COLOR_OBSTACULO = (255,0,0)
    COLOR_JUGADOR = (0,0,255)
    VELOCIDAD_OBSTACULO = 10
    ANCHO_OBSTACULO = 20	
    ALTO_OBSTACULO = 20
    DIFICULTAD = 1

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.ANCHO,self.ALTO))
        self.clock = pygame.time.Clock()
        self.obstaculos = []
        self.jugador = Jugador(self.VELOCIDAD_OBSTACULO,
        pygame.K_RIGHT,
        pygame.K_LEFT,
        self.ALTO / 2,
        self.ANCHO / 2,
        self.ANCHO_OBSTACULO * 1.3,
        self.ALTO_OBSTACULO * 1.3)


    def crear_obstaculos(self):
        self.obstaculos.append(Obstaculo(
                self.VELOCIDAD_OBSTACULO,
                random.randrange(self.ANCHO_OBSTACULO,self.ANCHO - self.ANCHO_OBSTACULO, self.ANCHO_OBSTACULO),
                random.randrange(self.ALTO_OBSTACULO,self.ALTO / 2), 
                self.ANCHO_OBSTACULO,
                self.ALTO_OBSTACULO
            ))
    # ~ def choque(self):
        # ~ for obstaculo in self.obstaculos:
            # ~ if obstaculo.colliderect(jugador):
                # ~ self.screen.fill((255,255,255))
                # ~ sys.exit()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            self.screen.fill((0,0,0,))
            self.jugador.mover_jugador(self.ANCHO)
            pygame.draw.rect(self.screen, self.COLOR_JUGADOR, self.jugador)
            for obstaculo in self.obstaculos:
                pygame.draw.rect(self.screen, self.COLOR_OBSTACULO, obstaculo)
                obstaculo.mover_obstaculo()
                if obstaculo.colliderect(self.jugador):
                    sys.exit()
                if obstaculo.y >= juego.ALTO - juego.ALTO_OBSTACULO :
                    self.obstaculos.remove(obstaculo)
                    del obstaculo
                
            if len(self.obstaculos) < 20:
                juego.crear_obstaculos()
            # ~ juego.choque()
            pygame.display.flip()
            self.clock.tick(20)
                    
if __name__== '__main__':
    juego = Juego()
    juego.game_loop()


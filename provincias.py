# Pygame template - skeleton for a new pygame project
import pygame
import random
import os


WIDTH = 900
HEIGHT = 900
FPS = 24
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imagenes')
    
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#classes
class BuenosAires:
    img = 'ba.png'
    destx = 100
    desty = 100

class SantaCruz:
    img = 'sc.png'
    destx = 600
    desty = 400
    
class Ficha(pygame.sprite.Sprite):
    def __init__(self, icono, destx, desty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, icono)).convert()  
        self.image.set_colorkey(WHITE)
        self.rect =  self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.drag = False
        self.destx = destx
        self.desty = desty
        self.encaje = False
    
    def update(self):
        # self.rect.x +=5
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                mouse_x, mouse_y = event.pos
                self.drag = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.drag = False
        if event.type == pygame.MOUSEMOTION and self.drag :
            mouse_x, mouse_y = event.pos
            self.rect.x = mouse_x 
            self.rect.y = mouse_y 
            if self.rect.right >= WIDTH:
                self.rect.right = WIDTH 
            elif self.rect.bottom > HEIGHT:
                self.rect.top = HEIGHT - self.rect.height
            elif self.rect.collidepoint(self.destx, self.desty):
                self.encaje = True
        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
piezas = [BuenosAires, SantaCruz]
cnt = 0
ficha = Ficha(piezas[cnt].img,piezas[cnt].destx, piezas[cnt].desty)
all_sprites = pygame.sprite.Group()
all_sprites.add(ficha)
imag = pygame.image.load("imagenes\\AR-B.png")

# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Update
    
    if ficha.encaje :
        cnt += 1
        all_sprites.remove(ficha)
        if cnt == len(piezas):
            running = False
        else:
            ficha = Ficha(piezas[cnt].img,piezas[cnt].destx, piezas[cnt].desty)
            all_sprites.add(ficha)
 
    # Draw / render
    screen.fill(WHITE)
    screen.blit(imag, (ficha.destx,ficha.desty))
    all_sprites.draw(screen)

    all_sprites.update()
   # *after* drawing everything, flip the display
    pygame.display.flip()
    # keep loop running at the right speed
    clock.tick(FPS)

pygame.quit()
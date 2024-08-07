import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (Frames Per Second)
FPS = 60
clock = pygame.time.Clock()

# Clase para la canasta
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Mantener dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Clase para la bola
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0
        self.speedy = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speedy
        # Si la bola llega al fondo de la pantalla, reiniciar posición
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = 0
            self.speedy = random.randint(3, 8)

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()

# Crear la canasta y agregarla al grupo de sprites
basket = Basket()
all_sprites.add(basket)

# Crear bolas y agregarlas al grupo de sprites
for i in range(5):
    ball = Ball()
    all_sprites.add(ball)
    balls.add(ball)

# Bucle principal del juego
running = True
while running:
    clock.tick(FPS)

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Detectar colisiones
    if pygame.sprite.spritecollide(basket, balls, True):
        ball = Ball()
        all_sprites.add(ball)
        balls.add(ball)

    # Dibujar / Renderizar
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Después de dibujar todo, actualizar la pantalla
    pygame.display.flip()

pygame.quit()

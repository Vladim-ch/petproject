import pygame        

# параметры экрана
WIDTH = 360
HEIGHT = 480
FPS = 30

# заготовки цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

def main():
    # стандартный шаблон 
    pygame.init()
    # pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME for your ASS")
    clock = pygame.time.Clock()

    running = True

    # Параметры объектов на экране
    all_sprites = pygame.sprite.Group()
    player = Block(50, 50, GREEN)

    all_sprites.add(player)
    while running:
        clock.tick(FPS) # указываем ограничение FPS
        
        # Выход из окна игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Рендер цвета фона 
        screen.fill(BLACK)
        all_sprites.draw(screen)        
        pygame.display.flip()


if __name__ == '__main__':
    main()


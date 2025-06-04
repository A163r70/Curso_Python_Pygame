from pygame.sprite import Sprite
from Configuration import Configuration
import pygame

class Soldier(Sprite):
    def __init__(self, screen):
        super().__init__()
        soldier_image_path = Configuration.get_soldier_image_path()
        self.image = pygame.image.load(soldier_image_path)
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()


        screen_rect = screen.get_rect()
        self.rect.centery=screen_rect.centery
        self.rect.right = screen_rect.right

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)


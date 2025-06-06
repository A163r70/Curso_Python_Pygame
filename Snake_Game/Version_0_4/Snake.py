import pygame
from pygame.sprite import Sprite
from Configuration import Configuration
from random import randint

class SnakeBlock(Sprite):

    def __init__(self, is_head: bool=False):
        """
        Constructor de la clase.
        """
        #se llama al constructor de la clase padre.
        super().__init__()

        if is_head:
            color = Configuration.get_sanke_head_color()
        else:
            color = Configuration.get_snake_body_color()

        snake_block_size = Configuration.get_snake_block_size()
        self.image = pygame.Surface((snake_block_size, snake_block_size))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar el bloque de la rspiente.
        :param screen: Pantalla en donde se dibuja.
        """

        screen.blit(self.image, self.rect)

    def snake_head_init(self)->None:
        screen_width = Configuration.get_screen_size()[0]
        screen_height = Configuration.get_screen_size()[1]
        snake_block_size = Configuration.get_snake_block_size()

        self.rect.x = snake_block_size * randint(0,(screen_width // snake_block_size))
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size))

import pygame
from pygame.sprite import Sprite
from Configuration import Configuration
from random import randint

class Apple(Sprite):

    #Atributo de clase para la puntuacion
    _no_apples = 0

    def __init__(self):
        super().__init__()

        Apple._no_apples += 1 #contador de manzanas

        self.image = pygame.Surface((Configuration.get_apple_block_size(), Configuration.get_apple_block_size()))
        self.image.fill((Configuration.get_apple_color()))

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibujaa
        """
        screen.blit(self.image, self.rect)

    def random_position(self, snake_body: pygame.sprite.Group)->None:
        """
        Se utiliza para inicializar una posicion aleatoria de la manzana y verifica
        no se sobreponga sobre el cuerpo de la serpiente.
        """
        repeat = True
        while repeat:
            #Se genera la posicion aleatoria.
            screen_width = Configuration.get_screen_size()[0]
            screen_height = Configuration.get_screen_size()[1]
            apple_block_size = Configuration.get_apple_block_size()

            self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size))
            self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size))

            #Se verifica que no se encuentre sobre el cuerpo de la serpiente.
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False

    @classmethod
    def get_no_apples(cls)->int:
        """
        Getter de _no_apples
        """
        return cls._no_apples
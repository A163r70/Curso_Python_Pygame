from Configuration import Configuration
import pygame

class Background:

    def __init__(self):
        background_image_path = Configuration.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        # Escalamos la imagen para que coincida con el tamaño de la pantalla.
        screen_size = Configuration.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)  # Dibujamos la imagen del fondo en la superficie de la pantalla.

import pygame
from Configuration import Configuration

class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path = Configuration.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size = Configuration.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image, self.rect)

class Audio:

    def __init__(self):
        #Se carga la musica del juego
        pygame.mixer.music.load(Configuration.get_music_path())

        #Se cargan los sonidos
        self._start_sound = pygame.mixer.Sound(Configuration.get_start_sound_path())
        self._eats_apple_sound = pygame.mixer.Sound(Configuration.get_eats_apple_sound_path())
        self._game_over_sound = pygame.mixer.Sound(Configuration.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume)->None:
        """Se utiliza para reproducir la musica en bucle"""
        pygame.mixer.music.play(loops = -1) #El -1 indica que se reproduce en bucle
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time)->None:
        """
        Se utilza para realizar un desvanecimiento de la musica del juego hasta que pare.
        :param time: Tiempo de desvanecimiento de la musica (en ms)
        """
        pygame.mixer.music.fadeout(time)

    def play_start_sound(self)->None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._start_sound.play()

    def play_eats_apple_sound(self)->None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana
        """
        self._eats_apple_sound.play()

    def play_game_over_sound(self)->None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()
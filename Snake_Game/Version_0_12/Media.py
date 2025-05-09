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

class Scoreboard:
    def __init__(self):
        self._typeface = "Kimono"
        self._font_size = 40
        self._font_color = (171, 250, 10)

        #Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("Puntos: 0", True, self._font_color)

        #Se obtiene el rectangulo
        self.rect = self.image.get_rect()
        #Se ajusta la posicion del marcador
        self.rect.x = Configuration.get_screen_size()[0] * 0.05
        self.rect.y = Configuration.get_screen_size()[1] * 0.05

    def update(self, new_score: int)->None:
        text = "Puntos: " + str(new_score)
        self.image = self._font.render(text, True, self._font_color)

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el scoreboard de cantidades de manzanas que va comiendo
        :param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)

class GameOverImage:
    def __init__(self):
        self.image = pygame.image.load("../Media/game_over_image.png")
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """

        :param screen:
        :return:
        """
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom-Configuration.get_snake_block_size()
        screen.blit(self.image, self.rect)


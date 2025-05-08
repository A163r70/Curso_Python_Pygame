class Configuration:
    """
    Clase que contiene todas la configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)           #Resolución de la pantalla (ancho, alto)
    _game_title = "Sanke game en Pygame" #Título del juego.
    _background = (20, 30, 50)           # Fonfo de la pantalla en formato RGB.
    _fps = 8 #fps del juego.
    _game_over_screen_time = 4


    #Configuraciones de la serpiente
    _snake_block_size = 80 #Tamaño del bloque de la serpiente.
    _snake_head_color = (255, 255, 255) #Color de la cabeza
    _snake_body_color = (0, 255, 0)#Color del cuerpo

    #Configuraciones de la manzana
    # Configuraciones de la manzana.
    _apple_block_size = _snake_block_size  # Tamaño del bloque (igual que la el de la serpiente).
    _apple_color = (255, 0, 0)  # Color de la manzana.
    _time_to_refresh = 200

    #La rutas de los archivos multimedia
    _background_image_path = "../Media/background_image.jpg"
    _apple_image_path = ["../Media/apple1.png",
                         "../Media/apple2.png",
                         "../Media/apple3.png",
                         "../Media/apple4.png"]
    _snake_head_image_path = ["../Media/head1.png",
                              "../Media/head2.png",
                              "../Media/head3.png",
                              "../Media/head4.png",
                              "../Media/head5.png",
                              "../Media/head6.png",
                              "../Media/head7.png",
                              "../Media/head8.png"]
    _snake_body_image_path =  ["../Media/body1.png",
                                "../Media/body2.png",
                                "../Media/body3.png"]

    #Configuracion de la musica del juego
    _music_volume = 0.25 #Volumen de la musica de fondo (valor entre 0 y 1)
    _music_fadeout_time = _game_over_screen_time * 100 #Duracion del desvanecimiento de la musica en ms.

    #Rutas de los audios utilizados en la clase Audio
    _music_path = "../Media/music.mp3"
    _start_sound_path = "../Media/start_sound.wav"
    _eats_apple_sound_path = "../Media/eats_apple_sound.wav"
    _game_over_sound_path = "../Media/game_over_sound.wav"

    @classmethod
    def get_screen_size(cls)->tuple[int, int]:
        """
        Getter para un _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        """
        return cls._game_title

    @classmethod
    def getter_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def gette_game_over_screen_time(cls) -> int:
        """
        Getter para _over_screen_time
        """
        return cls._game_over_screen_time

    @classmethod
    def get_snake_block_size(cls)->int:
        """
        Getter para snake_block_size
        """
        return cls._snake_block_size
    @classmethod
    def get_sanke_head_color(cls)->tuple[int, int, int]:
        """
        Geter para snake_head_color
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls)->tuple[int, int, int]:
        """
        Getter para snake_dody_color
        """
        return cls._snake_body_color

    @classmethod
    def get_apple_block_size(cls) -> int:
        """
        Getter para _apple_block_size.
        """
        return cls._apple_block_size

    @classmethod
    def get_time_to_refresh(cls) -> int:
        """
        Getter para _time_to_refresh.
        """
        return cls._time_to_refresh

    @classmethod
    def get_background_image_path(cls) ->str:
        """
        Getter para _background_image_path
        """
        return cls._background_image_path

    @classmethod
    def get_apple_image_path(cls) -> list:
        """
        Getter para _background_apple_path
        """
        return cls._apple_image_path

    @classmethod
    def get_snake_head_image_path(cls) -> list:
        """
        Getter para _background_apple_path
        """
        return cls._snake_head_image_path

    @classmethod
    def get_snake_body_image_path(cls) -> list:
        """
        Getter para _background_apple_path
        """
        return cls._snake_body_image_path

    @classmethod
    def get_music_volume(cls)->float:
        """
        Getter para _music_volume
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path
        """
        return cls._music_path

    @classmethod
    def get_start_sound_path(cls) -> str:
        """
        Getter para _start_sound_path
        """
        return cls._start_sound_path

    @classmethod
    def get_eats_apple_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path
        """
        return cls._eats_apple_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path
        """
        return cls._game_over_sound_path
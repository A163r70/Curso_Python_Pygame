class Configuration:
    """
    Clase que contiene todas la configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)           #Resolución de la pantalla (ancho, alto)
    _game_title = "Sanke game en Pygame" #Título del juego.
    _background = (20, 30, 50)           # Fonfo de la pantalla en formato RGB.
    _fps = 8 #fps del juego.

    #Configuraciones de la serpiente
    _snake_block_size = 80 #Tamaño del bloque de la serpiente.
    _snake_head_color = (255, 255, 255) #Color de la cabeza
    _snake_body_color = (0, 255, 0)#Color del cuerpo

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
    def getter_background(cls)->tuple[int, int, int]:
        """
        Getter para _background.
        """
        return cls._background

    @classmethod
    def getter_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

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
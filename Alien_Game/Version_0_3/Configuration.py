class Configuration:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1000, 500)           #Resolución de la pantalla (ancho, alto)
    _game_title = "Soldiers vs Alien" #Título del juego.
    _background = (20, 30, 50)           # Fondo de la pantalla en formato RGB.
    _fps = 8  # fps del juego.

    _background_image_path = "../Media/neon.jpg"
    _soldier_image_path = "../Media/soldado.png"

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
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls)->str:
        return cls._background_image_path

    @classmethod
    def get_soldier_image_path(cls)->str:
        return cls._soldier_image_path
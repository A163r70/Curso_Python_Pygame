class Configuration:
    """
    Clase que contiene todas la configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1000, 500)           #Resolución de la pantalla (ancho, alto)
    _game_title = "Sanke game en Pygame" #Título del juego.
    _background = (20, 30, 50)           # Fonfo de la pantalla en formato RGB.

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


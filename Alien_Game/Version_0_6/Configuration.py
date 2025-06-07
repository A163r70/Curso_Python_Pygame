class Configuration:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1000, 500)           #Resolución de la pantalla (ancho, alto)
    _game_title = "Soldiers vs Alien" #Título del juego.
    _background = (20, 30, 50)           # Fondo de la pantalla en formato RGB.
    _fps = 60  # fps del juego.

    # Configuraciones del soldado.
    _soldier_size = (142, 76)
    _soldier_frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frames_per_column = 2
    _soldier_shooting_frame_delay = 30
    _soldier_frame_delay = 300  # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5  # Velocidad (en píxeles) del personaje.

    _background_image_path = "../Media/game.jpg"
    _soldier_sheet_path = "../Media/soldier-idle_shooting_sheet.png"

    _shot_sheet_path = "../Media/shot-sheet.png"
    _shot_frames_per_row = 4
    _shot_size = (30, 30)
    _shot_speed = 30.5
    _shot_frame_delay = 100

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
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size

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
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_soldier_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._soldier_frames_per_row

    @classmethod
    def get_soldier_frames_per_column(cls)->int:
        return cls._soldier_frames_per_column

    @classmethod
    def get_soldier_shooting_frame_delay(cls) -> int:
        """
        Getter para _soldier_shooting_frame_delay.
        """
        return cls._soldier_shooting_frame_delay

    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""

    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_shot_sheet_path(cls)->str:
        return cls._shot_sheet_path

    @classmethod
    def get_shot_size(cls)->tuple[int, int]:
        return cls._shot_size

    @classmethod
    def get_shot_speed(cls)->float:
        return cls._shot_speed

    @classmethod
    def get_shot_frame_delay(cls)->int:
        return cls._shot_frame_delay

    @classmethod
    def get_shot_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._shot_frames_per_row
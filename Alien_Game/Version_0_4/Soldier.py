from pygame.sprite import Sprite
from Configuration import Configuration
import pygame

class Soldier(Sprite):
    def __init__(self, screen):
        super().__init__()

        self._is_moving_up = False
        self._is_moving_down = False

        # Lista que almacena los frames del soldado.
        self._frames = []

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configuration.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configuration.get_frames_per_row()
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height

        """NUEVO."""
        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configuration.get_soldier_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = soldier_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, soldier_frame_size)

            self._frames.append(frame)

        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        """NUEVO."""
        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        self._speed = Configuration.get_soldier_speed()
        self._rect_y = float(self.rect.y)

    def update_position(self, screen):
        screen_rect = screen.get_rect()

        if (self._is_moving_up): #si se mueve hacia arriba
            self._rect_y -= self._speed     #lo movemos en y

        if(self._is_moving_down):
            self._rect_y += self._speed     #lo movemos hacia abajo en y

        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.top)
        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        self.rect.y = int(self._rect_y)

    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configuration.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)

    @property
    def is_moving_up(self)->bool:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool)->None:
        self._is_moving_up = value

    @property
    def is_moving_down(self)->bool:
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool)->None:
        self._is_moving_down = value


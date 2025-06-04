import pygame
from pygame.sprite import Sprite
from Configuration import Configuration
from Soldier import Soldier


class Shot(Sprite):
    def __init__(self, screen, soldier):
        super().__init__()

        self._is_moving_left = False
        self._is_moving_right = False

        self._frames_shot = []

        sheet_shot_path = Configuration.get_shot_sheet_path()
        shot_sheet = pygame.image.load(sheet_shot_path)

        sheet_frames_per_row = Configuration.get_frames_per_row()
        sheet_width = shot_sheet.get_width()
        sheet_height = shot_sheet.get_height()
        shot_frame_width = sheet_width // sheet_frames_per_row
        shot_frame_height = sheet_height

        shot_frame_size = Configuration.get_shot_size()

        for i in range(sheet_frames_per_row):
            x = i * shot_frame_width
            y = 0
            subsurface_rect = (x, y, shot_frame_width, shot_frame_height)
            frame = shot_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, shot_frame_size)

            self._frames_shot.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames_shot[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        soldier_rect = soldier.rect
        self.rect.right = soldier_rect.right - 130
        self.rect.centery = soldier_rect.centery - 10

        self._speed = Configuration.get_shot_speed()
        self._rect_x = float(self.rect.x)

    def shot_animation(self)->None:
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configuration.get_shot_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames_shot[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames_shot):
                self._frame_index = 0

    def update_position(self, screen):
        screen_rect = screen.get_rect()

        if (self._is_moving_left): #si se mueve hacia arriba
            self._rect_x -= self._speed     #lo movemos en y

        if(self._is_moving_right):
            self._rect_x += self._speed     #lo movemos hacia abajo en y

        if self._rect_x < float(screen_rect.top):
            self._rect_x = float(screen_rect.top)
        elif self._rect_x > (screen_rect.bottom - self.image.get_height()):
            self._rect_x = float(screen_rect.bottom - self.image.get_height())

        self.rect.x = int(self._rect_x)

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)

    @property
    def is_moving_left(self) -> bool:
        return self._is_moving_left

    @is_moving_left.setter
    def is_moving_left(self, value: bool) -> None:
        self._is_moving_left = value

    @property
    def is_moving_right(self) -> bool:
        return self._is_moving_right

    @is_moving_right.setter
    def is_moving_down(self, value: bool) -> None:
        self._is_moving_right = value
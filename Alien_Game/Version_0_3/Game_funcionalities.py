import pygame
from Configuration import Configuration
from Media import Background
from Soldier import Soldier


def game_events()->bool:
    """
    Función que administra los eventos de juego.
    :return: La bandera del fin del juego.
    """
    #Se declara la bandera del fin del juego
    game_over = False

    # Verificar los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock, background: Background, soldier: Soldier)->None:
    """
    Función que administra los elementos visuales del juego.
    """

    # Dibujamos la imagen de fondo en la pantalla.
    background.blit(screen)
    soldier.blit(screen)

    pygame.display.flip()  # Actualizamos el contenido de la ventana.

    clock.tick(Configuration.get_fps())
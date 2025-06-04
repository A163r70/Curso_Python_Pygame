import pygame
from Configuration import Configuration

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

def screen_refresh(screen: pygame.surface.Surface)->None:
    """
    Función que administra los elementos visuales del juego.
    """

    screen.fill(Configuration.getter_background())

    # Se actualiza la pantalla.
    pygame.display.flip()
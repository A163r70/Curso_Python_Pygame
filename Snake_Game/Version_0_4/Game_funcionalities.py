import pygame
from Configuration import Configuration
from Snake import SnakeBlock

def game_events()->bool:
    """
    Función que administra los eventos del juegos.
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

def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_body: pygame.sprite.Group)->None:
    """
    Función que adminisrra los elementos visuales del juego.
    """

    screen.fill(Configuration.getter_background())

    #Se dibuja el cuerpo de la serpiente.
    for snake_block in snake_body.sprites():
        snake_block.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    #Se controla le velocidad de fps del juego
    clock.tick(Configuration.getter_fps())
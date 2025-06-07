import pygame
from Configuration import Configuration
from Media import Background
from Soldier import Soldier
from Shot import Shot


def game_events(soldier: Soldier, shots: pygame.sprite.Group)->bool:
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            if event.key == pygame.K_SPACE:
                new_shot = Shot(soldier)
                shots.add(new_shot)
                soldier.shoots()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False


    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,
                   background: Background, soldier: Soldier, shots: pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego.
    """

    # Dibujamos la imagen de fondo en la pantalla.
    background.blit(screen)
    soldier.update_animation()
    soldier.update_position(screen)
    soldier.blit(screen)
    for shot in shots.sprites():
        shot.update_position()
        shot.shot_animation()
        shot.blit(screen)

    pygame.display.flip()  # Actualizamos el contenido de la ventana.

    clock.tick(Configuration.get_fps())
import time
import pygame
from Configuration import Configuration
from Snake import SnakeBlock
from Apple import Apple
from Media import Background, Audio, Scoreboard, GameOverImage


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

        #Verificamos si el evento es que se oprima una tecal, y verificamos hacia que lado nos movemos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)

    #Se regresa la bandera
    return game_over

def snake_movement(snake_body: pygame.sprite.Group)->None:
    """
    Función que gestiona el movimiento de la serpiente.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    """

    body_size = len(snake_body.sprites())-1

    for i in range(body_size, 0, -1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i-1].rect.y

    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configuration.get_snake_block_size()
    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configuration.get_snake_block_size()
    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configuration.get_snake_block_size()
    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configuration.get_snake_block_size()

def check_collision(screen: pygame.surface.Surface, snake_body: pygame.sprite.Group, apples: pygame.sprite.Group,
                    audio: Audio, scoreboard: Scoreboard)->bool:
    """
    Funcion que revisa las coliciones del juego
    * Cabeza de la serpiente con el cuerpo
    * Cabeza de la serpiente con el bosrde de la pantalla.
    * Cabeza de la serpiente con la manzana.
    :param screen: Pantalla.
    :param snake_body: Cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :return: La bandera del fin del juego.
    """
    #Se declara la bandera del fin del juego.
    game_over = False

    #Se obtiene la cabeza de la serpiente
    head = snake_body.sprites()[0]

    #Se revisa la conlicion de cabeza de la serpiente con el borde la pantalla
    screen_rect = screen.get_rect()

    if head.rect.right > screen_rect.right:
        game_over = True
    elif head.rect.left < screen_rect.left:
        game_over = True
    elif head.rect.top < screen_rect.top:
        game_over = True
    elif head.rect.bottom > screen_rect.bottom:
        game_over = True

    #Se revisa la condición de la cabeza de las serpiente con el cuerpo de la serpiente.
    head_body_collisions = pygame.sprite.spritecollide(head, snake_body, dokill=False)

    if len(head_body_collisions) > 1:
        game_over = True

    #Se revisa la ondición de la cabeza de la serpiente con la manzana.
    head_apples_collisions = pygame.sprite.spritecollide(head, apples, dokill=True)

    if len(head_apples_collisions) > 0:
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple = Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

        scoreboard.update(Apple.get_no_apples()-1)

        #Se reproduce el sonido de que la serpiente ha comido la manzana
        audio.play_eats_apple_sound()

    return game_over

def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_body: pygame.sprite.Group,
                   apples: pygame.sprite.Group, background: Background, scoreboard: Scoreboard)->None:
    """
    Función que adminisrra los elementos visuales del juego.
    """

    #Se dibuja el fondo de la pantalla
    background.blit(screen)

    scoreboard.blit(screen)



    #Fondo de la pantalla en formato RGB
    #screen.fill(Configuration.getter_background())

    snake_body.sprites()[0].animate_head()

    # Se dibuja el cuerpo de la serpiente.
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    #Se anima el movimiento de la manzana
    apples.sprites()[0].animate_apple()

    # Se dibuja la manzana
    apples.draw(screen)

    #Se controla le velocidad de fps del juego
    clock.tick(Configuration.getter_fps())

    # Se actualiza la pantalla.
    pygame.display.flip()

def game_over_screen(audio: Audio, screen: pygame.surface.Surface)->None:
    """
    Función con la parte del fin del juego
    """
    #Se realiza el desvanecimiento de la musica y se reproduce el sonido de fin de juego
    audio.music_fadeout(time=Configuration.get_music_fadeout_time())
    audio.play_game_over_sound()

    game_over_image = GameOverImage()
    game_over_image.blit(screen)

    pygame.display.flip()

    time.sleep(Configuration.gette_game_over_screen_time())
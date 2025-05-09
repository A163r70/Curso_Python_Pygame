"""
Nombre:
Fecha:
Versión 0.8:
- Se agregan las colisiones del juego.
"""
#Se importan los módulos para el videojuego.
import pygame
from Configuration import Configuration
from Game_funcionalities import game_events, screen_refresh, snake_movement, check_collision, game_over_screen
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple
from Media import Background, Audio, Scoreboard


def run_game()->None:
    """
    Función principal del videojuego.
    """

    #Se incializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    screen = pygame.display.set_mode(Configuration.get_screen_size())

    #Se configura el título del juego.
    pygame.display.set_caption(Configuration.get_game_title())

    # Se configura el reloj del juego
    clock = pygame.time.Clock()# Se configura el reloj del juego

    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo dela serpiente.
    snake_body = Group()
    snake_body.add(snake_head)

    #Se crea el bloque inical de la manzana
    apple = Apple()
    apple.random_position(snake_body)

    #Se crea un grupo con las manzanas
    apples = Group()
    apples.add(apple)

    #Se crea el objeto con el fondo de pantalla
    background = Background()

    #Se crea el objeto con el sonido del juego y se reproduce la musica y el sonido inicial del juego
    audio = Audio()
    audio.play_music(volume=Configuration.get_music_volume())
    audio.play_start_sound()

    #Se crea el objeto del marcador
    scoreboard = Scoreboard()


    #Ciclo principal del videojuego
    game_over = False
    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        game_over = game_events()

        #Condición de que cerro la ventana
        if game_over:
            break

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)

        #Se revisan las condiciones en el juego
        game_over = check_collision(screen, snake_body, apples, audio, scoreboard)

        # Se dibujan los elementos gráficos en la pantalla.
        screen_refresh(screen, clock, snake_body, apples, background, scoreboard)

        # Si a perdido el jugador se llama a la pantalla de fin del juego
        if game_over:
            game_over_screen(audio, screen)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()
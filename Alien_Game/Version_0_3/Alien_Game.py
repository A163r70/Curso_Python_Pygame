"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21-05-25
Versión 0.2:
- Se agregó la clase Configuration en el módulo Configuration.py que va a incluir todas las
configuraciones del juego.
- Se agrega el módulo Game_funcionalities.
"""

import pygame
from Configuration import Configuration
from Game_funcionalities import game_events,screen_refresh
from Media import Background
from Soldier import Soldier


def run_game()->None:
    """
    Función principal del videojuego.
    """

    #Se inicializa el módulo de pygame
    pygame.init()

    clock = pygame.time.Clock()


    #Se inicializa la pantalla
    screen = pygame.display.set_mode(Configuration.get_screen_size())

    #Se configura el título del juego
    pygame.display.set_caption(Configuration.get_game_title())

    #Ciclo principal del videojuego
    game_over = False
    background = Background()
    soldier= Soldier(screen)

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        game_over = game_events()

        # Se dibujan los elementos gráficos en la pantalla.
        screen_refresh(screen, clock, background, soldier)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()
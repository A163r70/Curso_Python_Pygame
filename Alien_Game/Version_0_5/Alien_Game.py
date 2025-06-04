"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21-05-25
Versión 0.4:

"""

import pygame
from pygame.sprite import Group
from Configuration import Configuration
from Game_funcionalities import game_events,screen_refresh
from Media import Background
from Soldier import Soldier
from Shot import Shot


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

    shot_group = Group()


    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        game_over = game_events(soldier, shot_group, screen)

        # Se dibujan los elementos gráficos en la pantalla.
        screen_refresh(screen, clock, background, soldier, shot_group)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()
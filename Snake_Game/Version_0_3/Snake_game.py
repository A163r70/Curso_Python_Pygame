"""
Nombre:
Fecha:
Versión 0.3:
- Se agrego la calse Configuration en el módulo Configuration.py que va a incluir todas las
configuraciones del juego.
- Se agrega el módulo Game_funcionalitis
"""
#Se importan los módulos para el videojuego.
import pygame
from Configuration import Configuration
from Game_funcionalities import game_events, screen_refresh
from Snake import SnakeBlock

def run_game()->None:
    """
    Función principal del videojuego.
    """

    #Se incializa el módulo de pygame
    pygame.init()

    #Se configura el reloj del juego
    clock = pygame.time.Clock()

    #Se inicializa la pantalla
    screen = pygame.display.set_mode(Configuration.get_screen_size())

    #Se configura el título del juego.
    pygame.display.set_caption(Configuration.get_game_title())

    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()


    #Ciclo principal del videojuego
    game_over = False
    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        game_over = game_events()

        # Se dibujan los elementos gráficos en la pantalla.
        screen_refresh(screen, clock, snake_head)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()
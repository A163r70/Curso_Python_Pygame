"""
Nombre:
Fecha:
Versión 0.1:
- Se crea la pantalla de inicio
- Se confirgura el título de la pantalla
"""
#Se importan los módulos para el videojuego.
import pygame


def run_game()->None:
    """
    Función principal del videojuego.
    """

    #Se incializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    screen_size = (1000, 500)
    screen = pygame.display.set_mode(screen_size)

    #Se configra el título del juego
    game_title = "Sanke game en Pygame"
    pygame.display.set_caption(game_title)

    #Ciclo principal del videojuego
    game_over = False

    while not game_over:
        #Verificar los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            #Un clic en cerrar el juego.
            if event.type == pygame.QUIT:
                game_over = True

        # Se dibujn los elementos gráficos en la pantalla.
        background = (20, 30, 50)   # Fonfo de la pantalla en formato RGB.
        screen.fill(background)

        #Se actualiza la pantalla.
        pygame.display.flip()

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()
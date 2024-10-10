import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# FPS
FPS = 60
reloj = pygame.time.Clock()

# Dimensiones del jugador
tamaño_jugador = 50
velocidad_jugador = 5

# Dimensiones del enemigo
tamaño_enemigo = 50
velocidad_enemigo_inicial = 5

# Función para dibujar al jugador
def dibujar_jugador(jugador_x, jugador_y):
    pygame.draw.circle(PANTALLA, AZUL, (jugador_x + tamaño_jugador // 2, jugador_y + tamaño_jugador //2), tamaño_jugador //2)

# Función para dibujar enemigos
def dibujar_enemigo(enemigo_x, enemigo_y):
    pygame.draw.rect(PANTALLA, ROJO, (enemigo_x, enemigo_y, tamaño_enemigo, tamaño_enemigo))

# Verificar colisión
def verificar_colision(jugador_x, jugador_y, enemigo_x, enemigo_y):
    if (jugador_x < enemigo_x + tamaño_enemigo and
        jugador_x + tamaño_jugador > enemigo_x and
        jugador_y < enemigo_y + tamaño_enemigo and
        jugador_y + tamaño_jugador > enemigo_y):
        return True
    return False

# Menú principal
def mostrar_menu():
    while True:
        PANTALLA.fill(NEGRO)
        fuente = pygame.font.Font(None, 74)
        texto_titulo = fuente.render("Dodge Game", True, BLANCO)
        PANTALLA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        fuente_menu = pygame.font.Font(None, 50)
        texto_inicio = fuente_menu.render("1. Iniciar", True, BLANCO)
        texto_instrucciones = fuente_menu.render("2. Instrucciones", True, BLANCO)
        texto_salir = fuente_menu.render("3. Salir", True, BLANCO)

        PANTALLA.blit(texto_inicio, (ANCHO // 2 - texto_inicio.get_width() // 2, ALTO // 2))
        PANTALLA.blit(texto_instrucciones, (ANCHO // 2 - texto_instrucciones.get_width() // 2, ALTO // 2 + 60))
        PANTALLA.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, ALTO // 2 + 120))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return
                if evento.key == pygame.K_2:
                    mostrar_instrucciones()
                if evento.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

# Menú de instrucciones
def mostrar_instrucciones():
    while True:
        PANTALLA.fill(NEGRO)
        fuente = pygame.font.Font(None, 50)
        texto_instrucciones1 = fuente.render("Usa las flechas para moverte", True, BLANCO)
        texto_instrucciones2 = fuente.render("y esquiva los enemigos.", True, BLANCO)
        texto_regresar = fuente.render("Presiona ESC para regresar.", True, BLANCO)

        PANTALLA.blit(texto_instrucciones1, (ANCHO // 2 - texto_instrucciones1.get_width() // 2, ALTO // 2 - 30))
        PANTALLA.blit(texto_instrucciones2, (ANCHO // 2 - texto_instrucciones2.get_width() // 2, ALTO // 2 + 10))
        PANTALLA.blit(texto_regresar, (ANCHO // 2 - texto_regresar.get_width() // 2, ALTO // 2 + 60))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

# Juego principal
def juego():
    jugador_x = ANCHO // 2 - tamaño_jugador // 2
    jugador_y = ALTO - tamaño_jugador - 10
    enemigo_x = random.randint(0, ANCHO - tamaño_enemigo)
    enemigo_y = -tamaño_enemigo
    velocidad_enemigo = velocidad_enemigo_inicial

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= velocidad_jugador
        if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - tamaño_jugador:
            jugador_x += velocidad_jugador
        if teclas[pygame.K_UP] and jugador_y > 0:
            jugador_y -= velocidad_jugador
        if teclas[pygame.K_DOWN] and jugador_y < ALTO - tamaño_jugador:
            jugador_y += velocidad_jugador

        # Movimiento del enemigo
        enemigo_y += velocidad_enemigo
        if enemigo_y > ALTO:
            enemigo_y = -tamaño_enemigo
            enemigo_x = random.randint(0, ANCHO - tamaño_enemigo)
            velocidad_enemigo += 0.5  # Aumentar velocidad de los enemigos

        # Verificar colisión
        if verificar_colision(jugador_x, jugador_y, enemigo_x, enemigo_y):
            corriendo = False  # Termina el juego al colisionar

        # Dibujar en pantalla
        PANTALLA.fill(NEGRO)
        dibujar_jugador(jugador_x, jugador_y)
        dibujar_enemigo(enemigo_x, enemigo_y)
        pygame.display.flip()

        reloj.tick(FPS)

# Ejecutar juego
def main():
    mostrar_menu()
    juego()

if __name__ == "__main__":
    main()

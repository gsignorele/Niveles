import pygame

import constantes
from jugador import Player
from nivel import Nivel

""" Clase principal en el que se debe ejecutar el juego. """
pygame.init()

# Configuramos el alto y largo de la pantalla
size = [constantes.ANCHO_PANTALLA, constantes.ALTURA_PANTALLA]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Proyecto Video-Juegos")

# Creamos al jugador con la imagen p1_walk.png
jugador_principal = Player("imagenes/p1_walk.png")
jugador_principal.rect.x = 0
jugador_principal.rect.y = constantes.ALTURA_PANTALLA - jugador_principal.rect.height

# Creamos el nivel 1
nivel_1 = Nivel("imagenes/background_01.png", jugador_principal, screen)
# le decimos al jugador en que nivel va a estar
jugador_principal.nivel = nivel_1

lista_sprites_activos = pygame.sprite.Group()
lista_sprites_activos.add(jugador_principal)

#Variable booleana que nos avisa cuando el usuario aprieta el botOn salir.
salir = False
clock = pygame.time.Clock()
# -------- Loop Princiapl -----------
while not salir:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            salir = True 

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_principal.retroceder()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.avanzar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.bajar()
            if evento.key == pygame.K_UP:
                jugador_principal.subir()

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador_principal.parar()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.parar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.parar()
            if evento.key == pygame.K_UP:
                jugador_principal.parar()    
   
    nivel_1.update()
    lista_sprites_activos.update()

    # Si el jugador se acarca hacia el lado derecho mueve el mundo hacia la izquierda (-x)    
    if jugador_principal.rect.x >= 500:
        diff = jugador_principal.rect.x - 500
        jugador_principal.rect.x = 500        
        nivel_1.avance_nivel(-diff)
    
    # Si el jugador se acarca hacia el lado izquierda mueve el mundo hacia la derecha (x)    
    if jugador_principal.rect.x <= 120:
        diff = 120 - jugador_principal.rect.x
        jugador_principal.rect.x = 120
        nivel_1.avance_nivel(diff)           
    
    if jugador_principal.rect.y <= 0:        
        jugador_principal.rect.y = 0
    
    nivel_1.draw(screen)
    lista_sprites_activos.draw(screen)    
            
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

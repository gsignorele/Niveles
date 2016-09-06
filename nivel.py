import pygame
from enemigo import Enemy
from pared import Pared
from plataforma import Plataforma
from plataforma_movimiento import PlataformaConMovimiento
import constantes


class Nivel():
    
    # Valor numerico que expresa que tan lejos avanza nuestro jugador en el nivel
    posicion_jugador_nivel = 0    
    
    def __init__(self, ruta, jugador_principal, screen):
        self.ruta = ruta
        self.screen = screen
        # se carga el fondo 1 vez sola
        self.fondo = pygame.image.load(self.ruta).convert()        
         
        #listas de sprites        
        self.lista_sprites_enemigos = pygame.sprite.Group()
        
        # agregamos al jugador principal
        self.jugador_principal = jugador_principal        
        
        #Creamos un enemigo        
        enemigo_principal = Enemy("imagenes/pajaro.png")
        enemigo_principal.rect.x = 300
        enemigo_principal.rect.y = 200        
        self.lista_sprites_enemigos.add(enemigo_principal)
        
        enemigo_secundario = Enemy("imagenes/pajaro.png")
        enemigo_secundario.rect.x = 420
        enemigo_secundario.rect.y = 400        
        self.lista_sprites_enemigos.add(enemigo_secundario)
        
        #paredes
        pared = Pared(250,0,10,450)        
        self.lista_sprites_enemigos.add(pared)
        pared_limite_izquierdo = Pared(-150,0,0,constantes.ALTURA_PANTALLA)
        self.lista_sprites_enemigos.add(pared_limite_izquierdo)      
        pared_limite_derecho = Pared(constantes.LARGO_FONDO_NIVEL_1,0,0,constantes.ALTURA_PANTALLA)
        self.lista_sprites_enemigos.add(pared_limite_derecho)
       
        #plataformas        
        GRASS_MIDDLE = (648, 648, 70, 40)
        plataforma = Plataforma(GRASS_MIDDLE)
        plataforma.rect.x = 100 
        plataforma.rect.y = 100        
        self.lista_sprites_enemigos.add(plataforma)
                
        STONE_MIDDLE = (576, 576, 70, 70)
        bloque = PlataformaConMovimiento(STONE_MIDDLE)
        bloque.rect.x = 100 
        bloque.rect.y = 500        
        self.lista_sprites_enemigos.add(bloque)
        bloque.limite_inferior = 600
        bloque.limite_superior = 450
        bloque.jugador = self.jugador_principal
        bloque.nivel = self
        # velocidad         
        bloque.mover_y = -1                      
        
        # Se agrega una plataforma en movimiento.                      
        bloque = PlataformaConMovimiento(GRASS_MIDDLE)
        bloque.rect.x = 350
        bloque.rect.y = 280
        bloque.limite_izquierdo = 350
        bloque.limite_derecho = 600
        bloque.mover_x = 1
        bloque.jugador = self.jugador_principal
        bloque.nivel = self
        self.lista_sprites_enemigos.add(bloque)                
        
    
    def draw(self, screen):
        # Se dibuja el fondo en cada actualizacion de posiciones                
        self.screen.blit(self.fondo,(self.posicion_jugador_nivel // 3,0))
        
        # Se dibujan todos los sprite que se cargaron.        
        self.lista_sprites_enemigos.draw(screen)
    
    
    def update(self):
        self.lista_sprites_enemigos.update()

    
    def avance_nivel(self, avance_x):
        """ Cuando el usuario se mueve de izquierda/derecha se debe mover el nivel """
        self.posicion_jugador_nivel += avance_x
        
        for enemigo in self.lista_sprites_enemigos:            
            enemigo.rect.x += avance_x         


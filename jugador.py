import pygame


import constantes


from plataforma_movimiento import PlataformaConMovimiento
from funciones_spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    """Clase utilizada para desarrollar los jugadores del juego. """
    
    # -- Atributos
    mover_x = 0
    mover_y = 0   
    

    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []

    # Direccion en la que va el jugador.
    direccion = "R"
    
    nivel = None    

    
    def __init__(self, ruta):                
        pygame.sprite.Sprite.__init__(self)

        self.stop = False        
        
        sprite_sheet = SpriteSheet(ruta)
        
        # Carga de todos los sprite de la imagen hacia la derecha
        #1
        imagen = sprite_sheet.obtener_imagen(0, 0, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #2
        imagen = sprite_sheet.obtener_imagen(66, 0, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #3
        imagen = sprite_sheet.obtener_imagen(132, 0, 67, 90)
        self.jugador_frame_der.append(imagen)
        
        #7
        imagen = sprite_sheet.obtener_imagen(0, 93, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #8
        imagen = sprite_sheet.obtener_imagen(66, 93, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #9
        imagen = sprite_sheet.obtener_imagen(132, 93, 72, 90)
        self.jugador_frame_der.append(imagen)
        
        #10
        imagen = sprite_sheet.obtener_imagen(0, 186, 70, 90)
        self.jugador_frame_der.append(imagen)

        # # Carga de todos los sprite de la imagen hacia la derecha y la rotamos.
        imagen = sprite_sheet.obtener_imagen(0, 0, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(66, 0, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(132, 0, 67, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(0, 93, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(66, 93, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(132, 93, 72, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(0, 186, 70, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)

        # Seteamos con que sprite comenzar
        self.image = self.jugador_frame_der[0]
        self.rect = self.image.get_rect()
        

    def update(self):
        """ Metodo que actualiza la posicion del jugador. """
        
        # Gravedad        
        self.calc_grav()                

        # Movimientos Izquierda/Derecha
        self.rect.x += self.mover_x                 
        pos = self.rect.x + self.nivel.posicion_jugador_nivel
        if self.direccion == "R":            
            index = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[index]
        else:
            index = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[index]
      
        # Verficamos si colisionamos con algo mientras avanzamos        
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_sprites_enemigos , False)
        for block in lista_de_bloques_colisionados:
            # si me estoy moviendo a la derecha
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            # si me estoy moviendo a la izquierda
            elif self.mover_x < 0:
                self.rect.left = block.rect.right                

        self.rect.y += self.mover_y
        
        # Verficamos si colisionamos con algo si saltamos        
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_sprites_enemigos , False)
        for block in lista_de_bloques_colisionados:

            if self.mover_y > 0:
                self.rect.bottom = block.rect.top                
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, PlataformaConMovimiento):
                self.rect.x += block.mover_x        
        

    def retroceder(self):
        """ Se llama cuando movemos hacia la izq. """   
        self.direccion = "L" 
        self.mover_x = -6      
        
        
    def avanzar(self):
        """ Se llama cuando movemos hacia la der. """        
        self.mover_x = 6        
        self.direccion = "R"      
        
    def bajar(self):
        """ Se llama cuando movemos hacia la izq. """       
        self.mover_y = 8        

    def subir(self):                
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.nivel.lista_sprites_enemigos, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constantes.ALTURA_PANTALLA:
            self.mover_y = -10
        
        
    def parar(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0
        self.mover_y = 0

        
    def calc_grav(self):
        """ Calcula el efecto de la gravedad. """
        
        if self.mover_y == 0:
            # si el numero es muy grande baja de golpe desde el punto maximo del salto
            self.mover_y = 1
        else:
            # la velocidad con la que sube, mu chico sube mas
            self.mover_y += .1

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.ALTURA_PANTALLA - self.rect.height and self.mover_y >= 0:
            self.mover_y = 0
            self.rect.y = constantes.ALTURA_PANTALLA - self.rect.height


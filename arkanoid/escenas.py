# standar( los que vienen con una instalación  standar de python)
import  os
# libreria de terceros
import pygame as pg

#mis dependencias
from . import ALTO, ANCHO, FPS

from . entidades import Ladrillo, Raqueta



class Escena:
    def __init__(self, pantalla ):
       self.pantalla = pantalla 
       self.reloj = pg.time.Clock()
      


    def bucle_principal(self):
        """ 
         Este metodo debe ser implementado por todas y cada una de las escenas,
         en función de lo que esten esperando hasta la condicion de salida del bucle de la escena.
        """
        print( 'métod vacio bucle principal de ESCENA')


class Portada(Escena):
    def __init__(self, pantalla):
       super().__init__(pantalla)
       ruta = os.path.join('arkanoid','resources','images','arkanoid_name.png')
       self.logo = pg.image.load(ruta)

       ruta_letra = os.path.join('arkanoid', 'resources','fonts','CabinSketch-Bold.ttf')
       self.tipo_letra = pg.font.Font(ruta_letra, 25)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                 # salir = True
                  return True
                
                if evento.type == pg.KEYDOWN  and evento.key == pg.K_SPACE:
                   salir = True

            self.pantalla.fill((99,0,0))

            self.pintar_logo()
            self.pintar_mensaje()

            pg.display.flip() 
        return False
    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho ) / 2
        pos_y = (ALTO - alto)  / 2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = 'Pulsa <ESPACIO> para comennzar la partida'
        img_texto = self.tipo_letra.render(mensaje,True, (255,255,255))
        pos_x = (ANCHO - img_texto.get_width()) /2
        pos_y = 5/6 * ALTO
        self.pantalla.blit(img_texto ,( pos_x, pos_y))
       
        
      
class Partida(Escena):
    def __init__(self, pantalla):        
       super().__init__(pantalla)
       ruta_fondo = os.path.join( 'arkanoid','resources', 'images', 'background.jpg')
       self.fondo = pg.image.load(ruta_fondo)
       self.jugador = Raqueta()
       self.muro = []

    def bucle_principal(self):
        super().bucle_principal()
        salir = False

        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
               if pg.QUIT == evento.type:
                  return True

            
            self.pintar_fondo()
            self.pintar_muro()

            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            pg.display.flip() 

    def pintar_fondo(self) :
        # TODO  mejorar como rellenar toda la pantalla con el fondo sin usar copio/pego
        self.pantalla.fill((0,0,99))
        self.pantalla.blit(self.fondo , (0,0))
        self.pantalla.blit(self.fondo , (600,0))
        self.pantalla.blit(self.fondo , (0,800))
        self.pantalla.blit(self.fondo , (600,800))
     
    def pintar_rmuro(self):
        # Num filas
        # num cols
        # bucle filas
        # bucle cols
        # xxxx <----- trabajar con un solo ladrillo

        filas = 4
        columnas = 6

        for fila in range(filas):
            for col in range(columnas):
              ladrillo = Ladrillo()
              self.muro.append(ladrillo)


class MejoresJugadores(Escena):
    def __init__(self, pantalla) :
      super().__init__(pantalla)
   
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        
        while not salir:
            for evento in pg.event.get():
               if pg.QUIT == evento.type:
                   return True

            self.pantalla.fill((0,0,99))
            pg.display.flip() 
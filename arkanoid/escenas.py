import pygame as pg

class Escena:
    def __init__(self, pantalla ):
       self.pantalla = pantalla 
      


    def bucle_principal(self):
        """ 
         Este metodo debe ser implementado por todas y cada una de las escenas,
         en función de lo que esten esperando hasta la condicion de salida del bucle de la escena.
        """

        print( 'métod vacio bucle principal de ESCENA')


class Portada(Escena):
    def __init__(self, pantalla):
       super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                  salir = True

            self.pantalla.fill((99,0,0))
            pg.display.flip() 
        
      
class Partida(Escena):
    def __init__(self, pantalla):        
       super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False

        while not salir:
            for evento in pg.event.get():
               if pg.QUIT == evento.type:
                 salir = True

            self.pantalla.fill((0,99,0))
            pg.display.flip() 

     
  
class MejoresJugadores(Escena):
    def __init__(self, pantalla) :
      super().__init__(pantalla)
   
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        
        while not salir:
            for evento in pg.event.get():
               if pg.QUIT == evento.type:
                salir = True

            self.pantalla.fill((0,0,99))
            pg.display.flip() 

import os

import pygame as pg

from . import ANCHO, ALTO


class Raqueta(pg.sprite.Sprite):  
   velocidad = 10
   """ 
    1.Es un tipo de strite(usar herencia)
    2. se puede mover de un lado a otro (método)
    3.Pintar la pantalla  (método)
    4. volver a la podición inicial
    5. ... 
       """
   def __init__(self):
      super().__init__()     


      self.imagenes = []
      for i in range(3):
          ruta_img = os.path.join('arkanoid','resources', 'images', f'electric0{i}.png' )
          img = pg.image.load(ruta_img)
          self.imagenes.append(img)

      self.contador = 0
      self.image = self.imagenes[self.contador]
      self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))  

   def update(self):
      self.contador += 1
      if self.contador > 2:
         self.contador = 0
       

      teclas_pulsadas = pg.key.get_pressed()
      if teclas_pulsadas[pg.K_LEFT]:
           self.rect.x -= self.velocidad
           if self.rect.left< 0:
               self.rect.left = 0
      if teclas_pulsadas[pg.K_RIGHT]:
           self.rect.x += self.velocidad
           if self.rect.right > ANCHO:
               self.rect.right = ANCHO 

class Ladrillo(pg.sprite.Sprite):
   def __init__(self):
       super.__init__()
       ruta_verde = os.path.join('arkanoid','resources', 'images', 'greenTile.png')
       self.image = pg.image.load(ruta_verde)
       self.rect = self.image.get_rect() 

   def update():
    pass

    
    
      
          
       
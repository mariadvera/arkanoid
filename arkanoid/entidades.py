
import os

import pygame as pg

from . import ANCHO, ALTO


class Raqueta(pg.sprite.Sprite):  

    """ 
    1.Es un tipo de strite(usar herencia)
    2. se puede mover de un lado a otro (método)
    3.Pintar la pantalla  (método)
    4. volver a la podición inicial
    5. ... 
       """
    def __init__(self):
      super().__init__()
      ruta_img = os.path.join('arkanoid','resources', 'images', 'electric00.png')
      self.image = pg.image.load(ruta_img)
      self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))

    def pintar(self):
     pass
import os, sys

def calc_media( n1, n2, n3):
   if n1 < 0 or n2 < 0 or n3 < 0:
      print('Erro: Números negativos não são permitidos.')
      return None
   media=(n1+n2+n3)/3
   return media

x = 10; y = 20; z = 30
resultado = calc_media(x,y,z)

if resultado is not None:
    print ( "A media é:",resultado)
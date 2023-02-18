"""Evento: cualquier cosa que suceda en la pantalla"""

import pygame

#--> Inicia el juego
pygame.init()

#--> Crea la pantalla
pantalla=pygame.display.set_mode((800,600)) # Tamaño de la ventana

#--> Titulo e icono
pygame.display.set_caption("Invasión espacial",)
icono=pygame.image.load('imagenes/ovni.png')    # 'flaticon' en 32px
pygame.display.set_icon(icono)

#--> Jugador
img_jugador=pygame.image.load('imagenes/cohete.png')
jugador_x=384   # (800/2)-mitad de imagen
jugador_y=568   # (600-tamaño de imagen)
jugador_x_cambio=0

def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#--> Mantiene la pantalla activa hasta el evento 'quit'
se_ejecuta=True
while se_ejecuta:                    
    #--> Color de pantalla
    pantalla.fill((205,144,228))

    #--> Capturar evento
    for evento in pygame.event.get():       # Obtiene el evento ocurrido
        if evento.type == pygame.QUIT:      # La 'x' de la ventana
            se_ejecuta=False                # Termina la ejecucion del codigo

        #--> Se pulsa una tecla
        if evento.type==pygame.KEYDOWN:     # Presiono cualquier tecla
            if evento.key==pygame.K_LEFT:
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.1

        #--> Se levanta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #--> Modificar ubicacion
    jugador_x += jugador_x_cambio

    #--> Mantener dentro de los bordes
    if jugador_x<=0:
        jugador_x=0
    elif jugador_x>768:
        jugador_x=768

    jugador(jugador_x,jugador_y)
    #--> Actualizacion de la pantalla
    pygame.display.update()
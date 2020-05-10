from pygame.locals import *
import pygame
# En este documento de aqui se cambian las teclas de movimiento del jugador
# el pygame.locals es un modulo con un conjunto de variables preestablecidas

DERECHA = K_RIGHT
IZQUIERDA = K_LEFT
SALTO = K_z

def obtener_evento(new_interface = False):
    if not new_interfaz:
        return pygame.key.get_pressed()
    else:
        pass
                                                            # TO DO
                                                            # Aqui se configura la nueva intefaz
                                                            # Ejemplo:
                                                            # if (actividad):
                                                            #     key = pygame.key.get_pressed()
                                                            #     key[DERECHA] = 1
                                                            #     return key


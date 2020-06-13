from pygame.locals import *
import pygame
import joblib
import numpy as np
import sklearn as sk
import data

model_dir = "./models/"
model = joblib.load(model_dir+"RandomForest.pkl")
Xdata = np.loadtxt(model_dir+"Xdata.csv", delimiter=",")

DERECHA = K_RIGHT
IZQUIERDA = K_LEFT
SALTO = K_z



cuenta = [0]        # Lo voli una lista para que la variable no se
                    # vuelva a resetear al usarla en la función

def obtener_evento(new_interface = True, model=model, data=Xdata,\
                    cuenta=cuenta):
    if not new_interface:
        return pygame.key.get_pressed()
    else:
        key = pygame.key.get_pressed()
        KEY = list(key) 
        if KEY[K_t]:
            predict = model.predict(Xdata[cuenta[0]].reshape(1,-1))
            if predict == 1: 
                KEY[DERECHA] = 1
                cuenta[0] += 1
            if predict == 2:
                KEY[IZQUIERDA] = 1                                               # Aqui se configura la nueva intefaz
                cuenta[0] += 1 
        if cuenta[0] > len(Xdata) - 1:
            cuenta[0] = 0
        return KEY
                                                            # Ejemplo:
                                                            # if (actividad):
                                                            #     key = pygame.key.get_pressed()
                                                            #     key[DERECHA] = 1
                                                            #     return key


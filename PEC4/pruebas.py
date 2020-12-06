import numpy as np
import os
import scipy.spatial as sp
from scipy.spatial import distance_matrix


def lee_coordenadas_atomo(linea):
    """Interpreta las coordenadas de una línea de un fichero PDB que empiece por 
    ATOM (es un átomo)"""
    if linea.startswith('ATOM  '):
        x = float(linea[30:38])
        y = float(linea[38:46])
        z = float(linea[46:54])
        return [x, y, z]

    
def obtiene_coordenadas(estructura):
    """Lee una estructura (fichero PDB) y obtiene las coordenadas de los 
    átomos que contiene"""
    coordenadas = []
    with open(estructura) as input:
        lineas = [linea.rstrip(os.linesep) for linea in input.readlines()]
        for linea in lineas:
            atomo = lee_coordenadas_atomo(linea)
            if atomo:
                coordenadas.append(atomo)
    return np.array(coordenadas)


# Coordenadas_1 tiene las coordenadas de la proteína A en formato numpy
coordenadas_1 = obtiene_coordenadas('es_data_1PPE_rec.pdb')
print(len(coordenadas_1))

# Coordenadas_2 tiene las coordenadas de la proteína B en formato numpy
coordenadas_2 = obtiene_coordenadas('es_data_1PPE_lig.pdb')
print(len(coordenadas_2))


#SABEMOS CUANTOS ATOMOS TIENE CADA MOLECULA, LA COSA ES, QUE CUANDO CALCULO A_B Y B_A OBTENGO LA MISMA CANTIDAD DE FILAS Y COLUMNAS, ESTO
#SERA PORQUE TENGO LOS MISMOS ELEMENTOS QUE SATISFACEN MI CONDICIÓN. POR LO QUE TENDRE QUE VER EN dA_B Y dB_A CUALES CUMPLEN CON MI 
#CONDICION DE INDICES. CON UN LOOP LO HE INTENDADO PERO NO ME DEJA, POR LO QUE TENGO QUE PENSAR EN ALGO.

#Vamos a calcular las distancias
def distancia(a,b,n):
    dA_B = sp.distance.cdist(a, b)
    dB_A = sp.distance.cdist(b, a)
    A_B = np.where(dA_B < n)
    B_A = np.where(dB_A < n)


    '''print(len(dA_B))
    print(len(dB_A))
    print(len(A_B[0]))
    print(len(A_B[1]))
    print(len(B_A[0]))
    print(len(B_A[1]))'''

    
        #return { "Answer 1": ans1, "Answer 2": ans2, "Answer 3": ans3}
print("************************** OUR BADASS FUNCTION **********************************")

print(distancia(coordenadas_1,coordenadas_2, 4))
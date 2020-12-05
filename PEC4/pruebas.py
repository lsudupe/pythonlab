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
print(coordenadas_1)

# Coordenadas_2 tiene las coordenadas de la proteína B en formato numpy
coordenadas_2 = obtiene_coordenadas('es_data_1PPE_lig.pdb')
print(coordenadas_2)



#Vamos a calcular las distancias
def distancia(a,b,n):
    #d = distance_matrix(a,b)
    dA_B = sp.distance.cdist(a, b)
    dB_A = sp.distance.cdist(b, a)
    print(len(dB_A))
    print(len(dA_B))
    A_B = np.where(d < n)
    B_A = np.where(d < n)
    Aa = len(A_B[0])
    B = len(A_B[1])
    elem = list((int(j) for i in A_B for j in i))
    
    return

print("************************** OUR BADASS FUNCTION **********************************")

print(distancia(coordenadas_1,coordenadas_2, 4))
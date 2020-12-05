import numpy as np
import os
import scipy.spatial


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
coordenadas_1 = obtiene_coordenadas('data/1PPE_rec.pdb')

# Coordenadas_2 tiene las coordenadas de la proteína B en formato numpy
coordenadas_2 = obtiene_coordenadas('data/1PPE_lig.pdb')

# Código a completar:
atomos_A_B = 0
print("Número de átomos de A en contacto con B: ", atomos_A_B)

atomos_B_A = 0
print("Número de átomos de B en contacto con A: ", atomos_B_A)

# Finalmente, el número de átomos total será la suma de ambos:
print("Número total de átomos en contacto: ", atomos_A_B + atomos_B_A)
import numpy as np
import os
from MDAnalysis.analysis import rms


# Estructura atómica en formato PDB
estructura_1 = """
HETATM    1  C4  AIN A 141      20.988  20.013   8.918  1.00 32.08           C
HETATM    2  C3  AIN A 141      19.732  19.385   8.857  1.00 32.34           C
HETATM    3  C2  AIN A 141      19.527  18.104   9.636  1.00 33.22           C
HETATM    4  C5  AIN A 141      21.977  19.496   9.752  1.00 31.39           C
HETATM    5  H4  AIN A 141      21.183  20.890   8.320  1.00  0.00           H
HETATM    6  C6  AIN A 141      21.761  18.347  10.492  1.00 31.52           C
HETATM    7  H5  AIN A 141      22.932  19.991   9.830  1.00  0.00           H
HETATM    8  C1  AIN A 141      20.570  17.658  10.434  1.00 32.96           C
HETATM    9  H6  AIN A 141      22.537  17.967  11.139  1.00  0.00           H
HETATM   10  H1  AIN A 141      20.440  16.756  11.015  1.00  0.00           H
HETATM   11  C7  AIN A 141      18.679  19.893   7.921  1.00 32.12           C
HETATM   12  O1  AIN A 141      18.856  21.012   7.231  1.00 28.52           O
HETATM   13  O2  AIN A 141      17.582  19.373   7.818  1.00 32.90           O
HETATM   14  O3  AIN A 141      18.290  17.505   9.519  1.00 35.01           O
HETATM   15  C8  AIN A 141      17.117  17.595  10.410  1.00 35.75           C
HETATM   16  O4  AIN A 141      16.308  16.678  10.381  1.00 37.46           O
HETATM   17  C9  AIN A 141      16.879  18.753  11.344  1.00 36.44           C
HETATM   18  H91 AIN A 141      15.952  18.591  11.895  1.00  0.00           H
HETATM   19  H92 AIN A 141      17.709  18.830  12.046  1.00  0.00           H
HETATM   20  H93 AIN A 141      16.803  19.676  10.769  1.00  0.00           H
"""

estructura_2 = """
HETATM    1  C4  AIN A 141      20.909  19.934   8.896  1.00 32.08           C
HETATM    2  C3  AIN A 141      19.652  19.312   8.766  1.00 32.34           C
HETATM    3  C2  AIN A 141      19.387  18.158   9.565  1.00 33.22           C
HETATM    4  C5  AIN A 141      21.860  19.487   9.821  1.00 31.39           C
HETATM    5  H4  AIN A 141      21.131  20.820   8.331  1.00  0.00           H
HETATM    6  C6  AIN A 141      21.586  18.379  10.634  1.00 31.52           C
HETATM    7  H5  AIN A 141      22.771  20.048   9.926  1.00  0.00           H
HETATM    8  C1  AIN A 141      20.364  17.703  10.480  1.00 32.96           C
HETATM    9  H6  AIN A 141      22.314  18.043  11.358  1.00  0.00           H
HETATM   10  H1  AIN A 141      20.171  16.825  11.079  1.00  0.00           H
HETATM   11  C7  AIN A 141      18.638  19.970   7.867  1.00 32.12           C
HETATM   12  O1  AIN A 141      18.979  20.954   7.165  1.00 28.52           O
HETATM   13  O2  AIN A 141      17.431  19.667   7.937  1.00 32.90           O
HETATM   14  O3  AIN A 141      18.249  17.398   9.458  1.00 35.01           O
HETATM   15  C8  AIN A 141      17.235  17.488  10.335  1.00 35.75           C
HETATM   16  O4  AIN A 141      16.343  16.644  10.397  1.00 37.46           O
HETATM   17  C9  AIN A 141      17.211  18.698  11.261  1.00 36.44           C
HETATM   18  H91 AIN A 141      16.416  18.581  11.994  1.00  0.00           H
HETATM   19  H92 AIN A 141      18.154  18.814  11.795  1.00  0.00           H
HETATM   20  H93 AIN A 141      17.020  19.587  10.663  1.00  0.00           H
"""

def lee_coordenadas_atomo(linea):
    """Obtiene de una línea de texto en formato PDB las coordenadas en f
    ormato numérico"""
    if linea.startswith('HETATM'):
        x = float(linea[30:38])    # Coordenada x
        y = float(linea[38:46])    # Coordenada y
        z = float(linea[46:54])    # Coordenada z
        return [x, y, z]

    
def obtiene_coordenadas(estructura):
    """Transforma las coordenadas de cada átomo en un array numpy"""
    coordenadas = []
    for linea in estructura.split(os.linesep):
        atomo = lee_coordenadas_atomo(linea)
        if atomo:
            coordenadas.append(atomo)
    return np.array(coordenadas)


def calcula_rmsd_numpy(coordenadas_1, coordenadas_2):
    """Calcula la RMSD entre dos conjuntos de coordenadas atómicas"""
    # Aquí es dónde tenéis que completar el código. La solución puede ser 
    # una sola línea gracias a la capacidad de NumPy de hacer cálculos con 
    # matrices mediante "broadcast".
    # Si no dais con una solución en una línea no hay problema :)
    rmsd = rms.rmsd(coordenadas_1, coordenadas_2, center= True)
    #rmsd = 0.0 # Esta es la línea a modificar con vuestra solución
    return rmsd


coordenadas_1 = obtiene_coordenadas(estructura_1)
coordenadas_2 = obtiene_coordenadas(estructura_2)

rmsd = calcula_rmsd_numpy(coordenadas_1, coordenadas_2)

print(rmsd)
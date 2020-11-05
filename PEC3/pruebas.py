import string

def cifrado_cesar(mensaje, desplazamiento):
    alfabeto = string.ascii_lowercase
    alfab_desplazado = alfabeto[desplazamiento:] + alfabeto[:desplazamiento]
    tabla = str.maketrans(alfabeto, alfab_desplazado)
    return mensaje.lower().translate(tabla)




# Aqui podeis añadir mas ejemplos
print(cifrado_cesar("PROGRAMACION PARA LA BIOINFORMATICA", 0))
print(cifrado_cesar("PROGRAMACION PARA LA BIOINFORMATICA", 1))
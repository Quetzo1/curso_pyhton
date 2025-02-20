'''
Programa principal del juego del ahorcado
'''
import string
import unicodedata
from random import choice
import funciones as fn
import argparse

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal del juego del ahorcado
    '''
    # Cargamos las plantillas
    plantillas = fn.carga_plantillas
    (nombre_plantilla)
    # Cargamos las oraciones
    oraciones = fn.carga_archivo_texto
    (archivo_texto)
    # Obtenemos las palabras
    palabras = fn.obten_palabras
    (oraciones)
    o = 5 # 5 Oportunidades de fallar
    p = choice(palabras) # elegimos una palabra al azar
    abcdarios = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o>0:
        fn.despliega_plantilla
        (plantillas, o)
        o = fn.adivina_letra(abcdarios, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra!')
            break
        print(f"La palabra era: {p}")

if __name__=='__main__':
    parser = argparse.ArgumentParser (description='juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras a adivinar', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False: print(f'El archivo{archivo} no existe')
    else:
    #archivo ='./datos/pg15532.txt'
        main(archivo)
#!/usr/bin/env python3

import argparse
import os

#Descripcion de la funcionalidad del script
parser = argparse.ArgumentParser(description='Este script sirve para copiar el contenido de un archivo existente a otro. Si el archivo destino no existe, se crea')
#Se definen los argumentos a pedir
parser.add_argument('-i', '--input', type=str, help='Nombre del archivo a copiar')
parser.add_argument('-o', '--output', type=str, help='Nombre del archivo destino')
#Se define una variable que contiene a los argumentos en el objeto parser
args = parser.parse_args()

#Si el archivo de origen no existe, devuelve error
if not os.path.exists(args.input):
    print(f"Error: {args.input} no existe")
    exit(1)


if os.path.exists(args.output):
    overwrite = input(f"Precaucion: {args.output} existe, sobreescribir? (y/n)")
    if overwrite.lower() == 'y' or overwrite.lower() == 'yes':
        with open(args.input, 'r') as src_file, open(args.output, 'w') as dest_file:
            dest_file.write(src_file.read())
            print(f"{args.input} fue copiado a {args.output}")

    else:
        print("Operacion abortada")
        exit()

elif not os.path.exists(args.output):
    overwrite = input(f"Precaucion: {args.output} existe, sobreescribir? (y/n)")
    if overwrite.lower() == 'y' or overwrite.lower() == 'yes':
        with open(args.input, 'r') as src_file, open(args.output, 'x') as dest_file:
            dest_file.write(src_file.read())
            print(f"{args.input} fue copiado a {args.output}")

    else:
        print("Operacion abortada")
        exit()

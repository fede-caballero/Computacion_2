import subprocess
import argparse
import datetime

def ejecutar_comando(comando, archivo_salida, archivo_log):
    #Variable para fecha y hora de ejecucion
    fecha_hora_ejec = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #Se escribe en el archivo de log la fecha y hora de ejecucion del comando
    with open(archivo_log, "a") as archivo:
        archivo.write("Fecha y hora de ejecucion de comando: {}\n".format(fecha_hora_ejec))
    
    #Se escribe dentro del archivo "file" la salida del comando
    with open(archivo_salida, "x") as archivo:
        proceso = subprocess.Popen(comando, shell=True, stdout=archivo, stderr=subprocess.PIPE)

    proceso.wait()

    #Si el proceso devuelve el codigo 0, significa que el comando se ejecuto correctamente
    if proceso.returncode == 0:
        print("El comando se ejecuto correctamente")
    else:
        msj_error = proceso.stderr.read().decode("utf-8")

        with open(archivo_log, "a") as archivo:
            archivo.write("Error al ejecutar el comando: {}\n".format(msj_error))

        print("Ocurrio un error al ejecutar el comando. Consultar archivo Log")

parser = argparse.ArgumentParser(description='Se ejecuta un comando y se guarda la salida en otro archivo')
parser.add_argument("-c", "--command", required=True, help='Comando a ejecutar')
parser.add_argument("-f", "--file", required=True, help='Archivo de salida')
parser.add_argument("-l", "--log", required=True, help='Archivo de registro')
args = parser.parse_args()

ejecutar_comando(args.command, args.file, args.log)
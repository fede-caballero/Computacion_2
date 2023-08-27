import argparse
import os

def calcular_suma_pares(pid, verbose):
    inicio_mensaje = f"Proceso {pid} iniciado"
    fin_mensaje = f"Proceso hijo {pid} finalizado"

    if verbose:
        print(inicio_mensaje)

    suma_pares = sum(x for x in range(0, pid + 1) if x % 2 == 0)

    if verbose:
        print(fin_mensaje)

    return suma_pares

def main():
    parser = argparse.ArgumentParser(description="Suma de pares procesos separados por fork")

    #Argumentos:
    parser.add_argument("-n", type=int, required=True, help="Numero de procesos hijos")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verboso")
    args = parser.parse_args()

    print("Proceso padre iniciado")

    for i in range(args.n):
        pid = os.fork()
        
        if pid == 0:  # Proceso hijo
            suma = calcular_suma_pares(os.getpid(), args.verbose)
            print(f"{os.getpid()} - {os.getppid()} : {suma}")
            os._exit(0)
        elif pid > 0:
            _, status = os.wait()  # Esperar a que el proceso hijo termine
            print(f"Proceso hijo {pid} terminado con estado {status}")
        else:
            print("Error al crear el proceso hijo.")
    
    print("Proceso padre finalizado.")

if __name__ == "__main__":
    main()

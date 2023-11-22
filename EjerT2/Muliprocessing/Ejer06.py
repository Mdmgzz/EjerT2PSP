import multiprocessing

def suma(val1, val2):

    ini = min(val1, val2)
    fin = max(val1, val2)

    resultado = sum(range(ini, fin + 1))

    print(f"La suma de los números entre {ini} y {fin} es: {resultado}")


def main():

    # lista de valores introducidos 
    valores = [(1, 5), (10, 15), (20, 10)] 
    numProcesos = len(valores)

    with multiprocessing.Pool(processes=numProcesos) as pool:
        pool.starmap(suma, valores)
        main()

    print("Procesos Procesados")

if __name__ == "__main__":
    main()
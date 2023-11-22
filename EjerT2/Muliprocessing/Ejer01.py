import multiprocessing

# suma los numeros desde 1 hasta lo pasado por parametro
def suma(numeros):
    resultado = sum(range(1, numeros + 1))
    print(f"La suma de los números hasta {numeros} es: {resultado}")

def main():
    # son los numeros que se pasaran por parametros
    valores = [5, 10, 15]  

#lista vacia en la que posterior mente utilizaremos para llamar a la funcion suma con cada valor
    procesos = []

#for each para ir cogiendo un valor de la lista valores e ir iniciando su proceso de suma
    for valor in valores:
        proceso = multiprocessing.Process(target=suma, args=(valor,))
        procesos.append(proceso)
        proceso.start()

#vamos a iniciar todos los procesos
    for proceso in procesos:
        proceso.join()

# una vez que todos los procesos hayan finalizado se muestra un mensaje de que todo ha terminado
    print("Procesos procesados :).")

# esto se asegura que el codigo se esta ejecutando como programa independiente
if __name__ == "__main__":
    main()
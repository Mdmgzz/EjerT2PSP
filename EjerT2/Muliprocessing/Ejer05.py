import multiprocessing

def suma(ini, fin):
    # comprobacion de rango de los argumentos, si el primer numero es mayor que el primero
    # se cambiaran los puestos
    if ini > fin:
        ini, fin = fin, ini 
    resultado = sum(range(ini, fin + 1))
    print(f"La suma de los números entre {ini} y {fin} es: {resultado}")

def main():
    valores = [(5, 1), (10, 15), (20, 10)]  
    procesos = []

#for each para recorer los valores a procesar
# se utiliza la lista procesos para guardar los argumentos de inicio y fin y llamar a la funcion de suma
# en la cual se guardaran todas los valores de la lista valores y se añadiran al proceso
    for ini, fin in valores:
        proceso = multiprocessing.Process(target=suma, args=(ini, fin))
        procesos.append(proceso)
        proceso.start()

#una vez los valores esten añadidos a la lista proceso , este se iniciará
#una vez que todo haya terminado mostrara mensaje de todo correcto
    for proceso in procesos:
        proceso.join()

    print("Procesos Procesados")

if __name__ == "__main__":
    main()
import multiprocessing

# suma los numeros desde 1 hasta lo pasado por parametro
def suma(n):
    res = sum(range(1, n + 1))
    print(f"La suma de los números hasta {n} es: {res}")

def main():
    valores = [5, 10, 15]

    #numero de procesos que se van a utilizar   
    numProcesos = 2  


# .pool sirve para asignar tareas de manera eficiente a los procesos que hay disponibles
    with multiprocessing.Pool(processes=numProcesos) as pool:
        # pool.map se utiliza para asignar cada la funcion de suma a cada valor de valores
        # y esto hace que se distrubuyan las tareas en los porcesos del pool 
        pool.map(suma, valores)

    print("Procesos Procesados.")

if __name__ == "__main__":
    main()
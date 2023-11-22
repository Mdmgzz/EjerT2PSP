from multiprocessing import Process,Queue


#funcion que lee los numeros de un fichero creado anteriormente
def lecturafichero():
    with open ("ficherosnum.txt","r") as fichero:
        numero = int(fichero.readline().strip())
    return numero


# suma los numeros desde 1 hasta lo pasado por parametro
def suma(queue):
    item=queue.get()

    while item is not None :

        res = sum(range(int(num + 1)))
        suma=0
        for valor in res:
            suma += valor
        print(f"La suma de los números hasta {queue} es: {suma}")

        num=queue.get()


if __name__ == "__main__":
    queue=Queue()

    proceso1=Process(target=lecturafichero,args=(queue,))
    proceso2=Process(target=suma,args=(queue,))

    #iniciamos el primer proceso
    proceso1.start()
    proceso2.start()
    
    proceso1.join()
    #ponemos en el valor de la cola none para que el programa sepa cuando parar
    
    queue.put(None)

    print("Procesos Procesados.")
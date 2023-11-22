from multiprocessing import *

fichero = "Multiprocessing/ficheronum.txt"

def suma(conn):
    primerVal = conn.recv()
    while primerVal is not None: 
        rango = range(int(primerVal+1)) 
        res = 0 

        #for each para recorrer el rango de num
        for numero in rango:
            res+=numero
        print (res) 

        #siguiente valor 
        primerVal = conn.recv() 
        

   

def lecturaFichero(nombreArchivo, conn):
    archivo = open(nombreArchivo, "r")
    for numero in archivo: 

        #strip no coge los espacios blancos
        conn.send(int(numero.strip())) 
    archivo.close()
    conn.send(None)


if __name__ == '__main__':
    left, right = Pipe()
    p1 = Process(target=suma, args=(left,))
    p2 = Process(target=lecturaFichero, args=(fichero, right,))

    p1.start()
    p2.start()

    p2.join()
    p1.join()

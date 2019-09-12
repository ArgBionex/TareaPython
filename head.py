#head: imprime el número indicado de lineas o de bytes

#  C:\Users\Marilina\Desktop\manejable.txt

def head():
    Namefile= input('Por favor ingrese el nombre del archivo: ')
    while True:
        modo= input ('indique si quiere abrir el archivo en modo texto (r) o en modo bytes (rb) \n r/rb: ')
        modo=modo.lower()
        if modo == 'r' or modo == 'rb':
            break
    try:
        archivo = open (Namefile, modo)
    except FileNotFoundError:
        print('El archivo no existe')
        return
    try:
        numero=int(input ('Ingresa la cantidad de lineas o bytes para mostrar: '))
    except ValueError:
        print('No ingresaste un entero')
        return

    if modo == 'r':
        for linea in range(numero):
            print(archivo.readline())
        
    else:
        contenido=archivo.read(numero)
        print(contenido)
    archivo.close()

head()
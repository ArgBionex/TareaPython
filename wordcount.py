# Contador de palabras en un archivo.



# C:\Users\Marilina\Desktop\manejable.txt
def wc():
    filename= input('Por favor ingrese el nombre del archivo: ')
    try:
        archivo = open(filename)
    except FileNotFoundError or OSError:
        print('El archivo no existe')
        return
    
    contenido = archivo.read()

    contenido.replace('\n', ' ')
    contenido = str.split(contenido)
    print(len(contenido))

wc()







# Pega el archivo en un directorio, si ya existe sobreescribe solo si damos el OK

def paste (filename2, archivo):
    try:
        archivo2= open (filename2, 'w')
    except:
        print('La ruta destino no es correcta')
        return
    cadena= ''
    contenido = archivo.read()
    archivo2.write(contenido)
    archivo2.close()

def pasteex(filename2, archivo):
    try:
        open (filename2, 'r')
    except FileNotFoundError: 
        paste(filename2, archivo)
        archivo.close()
        return
    while True: 
        rta= input('El archivo ya existe \n ¿Quieres sobre escribirlo? \n Y/N: ') 
        rta = rta.lower()
        if rta == 'y' or rta == 'n':
            break
    if rta == 'y':
        paste(filename2, archivo)
        archivo.close()


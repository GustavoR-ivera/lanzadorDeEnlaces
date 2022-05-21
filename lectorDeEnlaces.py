import re

#abre el acta
def lecturaArchivo(ruta):
    archivo = open(ruta, 'r')
    return archivo

#crea un .txt donde iran los soportes del acta
def crearArchivo():
    archivo = open('C:\Users\sebas\OneDrive\Escritorio\Ejercicio\soportes.txt', 'w')
    return archivo

#escribe en el archivo soportes cada url encontrada en el acta
def escribir(urls, soportes):
    for i in urls:
        soportes.write(i)
        soportes.write('\n')

#apertura de acta
acta = lecturaArchivo("C:\Users\sebas\OneDrive\Escritorio\Ejercicio\Acta5.txt")

#crear archivo con soportes
soportes = crearArchivo()

#exp. regular
patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

#busqueda del patron linea por linea en el acta
for linea in acta.readlines():
    urls = re.findall(patron, linea)
    escribir(urls,soportes) 

acta.close()









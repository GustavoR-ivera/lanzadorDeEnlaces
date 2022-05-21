import re

#abre el acta
def lecturaArchivo(ruta):
    archivo = open(ruta, 'r')
    return archivo

#crea un .txt donde iran los soportes del acta
def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    return archivo

#obtiene los soportes de cada acta que se le suministre
def procesarActa(acta, soportes):
    #exp. regular
    patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #busqueda del patron linea por linea en el acta
    for linea in acta.readlines():
        urls = re.findall(patron, linea)
        escribir(urls,soportes) 

    acta.close()

#escribe en el archivo soportes cada url encontrada en el acta
def escribir(urls, soportes):
    for i in urls:
        soportes.write(i)
        soportes.write('\n')


def leerActasIndustrial(actaInicial, actaFinal):
    # numero de acta inicial
    m = actaInicial   
    n = m
    #el ciclo se repite tantas veces como la cantidad de actas
    for i in range(actaFinal-actaInicial+1):
        try:
            #apertura de acta (se debe cambiar cada que se quiera procesar una nueva acta)
            nombreActa = '.\Actas_industrial_2021\Acta'
            rutaActa = nombreActa + str(m) + '.txt'
            acta = lecturaArchivo(rutaActa)
   
             #crear archivo con soportes
            nombreSoporte = '.\soportes_industrial_2021\soportesActa'
            rutaSoporte = nombreSoporte + str(n) + '.txt'
            soportes = crearArchivo(rutaSoporte)

            #actualizacion de indices
            m=m+1
            n = m
            procesarActa(acta, soportes) 
        except:
            #actualizacion de indices
            m=m+1
            n = m
            continue

def leerActasSistemas(actaInicial, actaFinal):
    # numero de acta inicial
    m = actaInicial   
    n = m
    #el ciclo se repite tantas veces como la cantidad de actas
    for i in range(actaFinal-actaInicial+1):
        try:
            #apertura de acta (se debe cambiar cada que se quiera procesar una nueva acta)
            nombreActa = '.\Actas_sistemas_2021\Acta'
            rutaActa = nombreActa + str(m) + '.txt'
            acta = lecturaArchivo(rutaActa)
   
             #crear archivo con soportes
            nombreSoporte = '.\soportes_sistemas_2021\soportesActa'
            rutaSoporte = nombreSoporte + str(n) + '.txt'
            soportes = crearArchivo(rutaSoporte)

            #actualizacion de indices
            m=m+1
            n = m
            procesarActa(acta, soportes) 
        except:
            #actualizacion de indices
            m=m+1
            n = m
            continue

def main(): 
    #especificar numero de acta inicial y final
    leerActasIndustrial(8,26)
    #especificar numero de acta inicial y final
    leerActasSistemas(8,17)

main()
    













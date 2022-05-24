# -*- coding: utf-8 -*-
import sys 
from time  import sleep
from selenium  import webdriver

#abre el acta
def lecturaArchivo(ruta):
    archivo = open(ruta, 'r')
    return archivo

# usamos chrome con selenium
driver = webdriver.Chrome('./chromedriver.exe')
#ventana principal para iniciar sesion en el correo
driver.get('https://smartkey.xertica.com/cloudkey/a/unal.edu.co/user/login')
# save main_window
main_window = driver.current_window_handle

#tiempo de demora de erika 5 minutos y después empiezan las descargas
sleep(300)

#----------------------------------------------------------------------------------------#
# numero de soporte inicial
m = 8
# numero de soporte final
n = 26
#----------------------------------------------------------------------------------------#

#el ciclo se repite tantas veces como la cantidad de archivos con soportes
for i in range(n-m+1):
    try:
        #apertura de archivo con soportes 
        nombreSoporte = '.\soportes_industrial_2021\soportesActa'
        rutaSoporte = nombreSoporte + str(m) + '.txt'
        soporte = lecturaArchivo(rutaSoporte)

        #descarga de soportes
        for i in soporte.readlines():
            try:
                driver.execute_script("window.open();")
                # switch to the new window which is second in window_handles array
                driver.switch_to_window(driver.window_handles[1])
                # open successfully and close
                driver.get(i)
                sleep(3)
                boton = driver.find_element_by_xpath('//div[@data-tooltip="Download"]')
                boton.click()
                sleep(3)
                driver.quite()   
                driver.switch_to_window(main_window)  
            except:
                continue

        driver.quite()
        soporte.close()

        #actualizacion de indices
        m=m+1
        
    except:
        #actualizacion de indices
        m=m+1
        continue


quit()
sys.exit(0)
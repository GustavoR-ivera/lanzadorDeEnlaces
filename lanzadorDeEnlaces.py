# -*- coding: utf-8 -*-
import webbrowser

#navegador edge
edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))

#navegador chrome
chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

#navegador brave
bravePath = "C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(bravePath))

#leer archivo
def lecturaArchivo(ruta):
    archivo = open(ruta, 'r')
    return archivo

#apertura de soportes
soportes = lecturaArchivo('.\soportes_industrial_2021\soportesActa8.txt')

for i in soportes.readlines():
    webbrowser.get('chrome').open_new_tab(i)
    



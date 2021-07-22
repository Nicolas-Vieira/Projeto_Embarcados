import serial
import time
import pyautogui

ser = serial.Serial('COM3', 9600)
time.sleep(1)
while 1:
    dados = str(ser.readline().decode().strip('\r\n'))
    lista_dados = dados.split(' ')
    #Direita
    if (int(lista_dados[0]) >= 980):
        pyautogui.move(50, 0)

    #Esquerda
    if (int(lista_dados[0]) <= 23):
        pyautogui.move(-50, 0)

    #Pra baixo
    if (int(lista_dados[1]) >= 980):
        pyautogui.move(0, 50)
    
    #Pra cima
    if (int(lista_dados[1]) <= 23):
        pyautogui.move(0, -50)

    #Click esquerdo
    if (int(lista_dados[2]) == 0):
        pyautogui.click()
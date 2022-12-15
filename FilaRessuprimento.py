import pyautogui
import time

pyautogui.PAUSE = 0.5

#Abrir chrome
pyautogui.moveTo(659,736)
pyautogui.click()

#Korber
pyautogui.moveTo(153,0)
pyautogui.click()

#...
pyautogui.moveTo(31,179)
pyautogui.click()

#Supply
pyautogui.moveTo(154,256)
pyautogui.click()

#Advantage
pyautogui.moveTo(130,609)

pyautogui.click()

#Movimentação
pyautogui.moveTo(120,453)

pyautogui.click()

#Ressuprimento
pyautogui.moveTo(161,471)
pyautogui.click()

#Fila
pyautogui.moveTo(148,647)
pyautogui.click()

#Consultar
pyautogui.moveTo(975,134)
pyautogui.click()

#Exportar
pyautogui.click()
time.sleep(0.5)

#Abrir arquivo
pyautogui.moveTo(105,651)
pyautogui.click()
time.sleep(1)

#Habilitar edição
pyautogui.moveTo(1188,76)
pyautogui.click()

#Pagina inicial
pyautogui.moveTo(116,51)
pyautogui.click()

#Apagar linhas
pyautogui.moveTo(707,220)
pyautogui.mouseDown()
pyautogui.moveTo(63,215)
pyautogui.mouseUp()

#Apagar linhas
pyautogui.hotkey('ctrl','-')

#Apagar linhas
pyautogui.moveTo(313,212)
pyautogui.mouseDown()
pyautogui.moveTo(116,214)
pyautogui.mouseUp()

#Apagar linhas
pyautogui.hotkey('ctrl','-')

#Apagar linhas
pyautogui.moveTo(278,218)
pyautogui.mouseDown()
pyautogui.moveTo(1327,203)
pyautogui.mouseUp()

#Apagar linhas
pyautogui.hotkey('ctrl','-')
pyautogui.press('enter')

#Inserir
pyautogui.moveTo(225,56)
pyautogui.click()
pyautogui.moveTo(143,353)
pyautogui.click()

#Tabela dinamica
pyautogui.moveTo(40,77)
pyautogui.click()
pyautogui.moveTo(142,546)
pyautogui.click()
pyautogui.press('enter')

#Arrastar tabela
pyautogui.moveTo(1045,364)
pyautogui.click()
pyautogui.moveTo(1040,341)
pyautogui.click()

#Imprimir
pyautogui.hotkey('ctrl','p')
pyautogui.press('enter')



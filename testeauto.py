import pyautogui
import time

pyautogui.PAUSE = 3

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

time.sleep(1)

linkLoja = 'https://www.artwalk.com.br/tenis-nike-air-max-terrascape-plus-nn-masculino-dq397-7-003/p'
pyautogui.write(linkLoja)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=956, y=279)
time.sleep(0.5)
pyautogui.scroll(-150)
pyautogui.click(x=1248, y=576)
time.sleep(1.5)
pyautogui.scroll(-160)
time.sleep(1)
pyautogui.click(x=1077, y=621)
time.sleep(1)
pyautogui.click(x=1117, y=421)
time.sleep(5)
pyautogui.click(x=1191, y=605)
time.sleep(1)
pyautogui.write('pg20041312@gmail.com')
pyautogui.press('enter')
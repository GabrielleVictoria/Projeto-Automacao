import pyautogui
import time

pyautogui.PAUSE = 0.5


pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)


pyautogui.click(x=688, y=451)
pyautogui.write('gaby.victoria0213@gmail.com')
pyautogui.press('tab')
pyautogui.write('102030')
pyautogui.press('tab')
pyautogui.press('enter')

import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=752, y=299)

    codigo = tabela.loc[linha, "codigo"]
    print(codigo)
    
    pyautogui.write((codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
    
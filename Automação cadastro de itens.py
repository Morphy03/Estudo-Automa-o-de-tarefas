# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar o pyautogui: pip install pyautogui

import pyautogui as pa
import time as tm
import pandas as pd

pa.PAUSE =  0.4

#pyautogui.click (clicar com o mouse)
#pyautogui.write (escreve um texto)chrome
#pyautogui.press (pressiona a tecla)
#pyautogui.hotkey (pressiona a tecla com o shift)

# 1.1 Abrir o navegador (opera gx)

pa.hotkey('win')
pa.write('chrome')
pa.press('enter')

# 1.2 entrar no site do sistema

pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')

tm.sleep(3)

# 2. fazer login

pa.press('tab')
pa.write('williamalvariisto5@gmail.com')
pa.press('tab')
pa.write('0123456')
pa.press('enter')

# 3. Abrir/importar a base de daos de produtos para cadastrar

tabela = pd.read_csv('meu.csv')


# 4. Cadastrar um produto

for linha in tabela.index:
    # 4.1 Clicar no botão de adicionar produto
    pa.click(x=415, y=326)
    # 4.2 Preencher o codigo do produto 
    codigo = str(tabela.loc[linha, 'codigo'])
    pa.write(codigo)
    # 4.3 Passar pro proximo campo
    pa.press('tab')
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pa.write(marca)
    pa.press('tab')
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pa.write(tipo)
    pa.press('tab')
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pa.write(categoria)
    pa.press('tab')
    #preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pa.write(preco)
    pa.press('tab')
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pa.write(custo)
    pa.press('tab')
    #obs 
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':     
        pa.write(obs)
    pa.press('tab')
    #aperta botao
    pa.press('enter')
    pa.scroll(5000)

# 5. Repetir isso tudo ate acabar a lista 



 
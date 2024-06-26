# Passo a passo do projeto 
# Passo 1: Entrar no sistema da empresa # https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui
import time
import pandas
# Comando para configurar o tempo de execução dos comandos

pyautogui.PAUSE = 5
#comandos para executar a tecla windows(pyautogui.press) e pesquisar o software desejado(pyautogui.write)

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')        

# Entrar no site
linkSite = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(linkSite)
pyautogui.press('enter')

# Dar uma pausa um pouco maior
time.sleep(2)

# Passo 2: Fazer login
# Apoós pegar a posição(usando o pyautogui.position), passar o valor de X e Y para o comando click

# Primeira opção de login usando a localização do elemento
#pyautogui.click(x=211, y=370)
# Segunda opção usando o pyautogui.press selecionando a tecla tab
pyautogui.press('tab')
pyautogui.write('pedro@gmail.com')

# Escrever a senha
pyautogui.press('tab')
pyautogui.write('pedrog13')

# Primeira opção de login usando a localização do elemento
#pyautogui.click(x=435, y=510)
# Segunda opção para enviar o formulário usando o comando press com a tecla enter
pyautogui.press('enter')
time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv('produtos.csv')

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    
    # Clicar no primeiro campo
    pyautogui.press('tab')

    # Codigo Produto
    # O comando tabela.loc é para localizar, precisamos passar os nomes corretos para a busca dos dados.
    
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
       
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')


    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
# Passo 5: Repetir o processo até finalizar a base de dados


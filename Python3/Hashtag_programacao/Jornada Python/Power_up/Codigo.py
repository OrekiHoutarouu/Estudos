# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui, time, pandas

# pyautogui.write = Escreve um texto
# pyautogui.press = Aperta uma tecla
# pyautogui.click = Clica em algum lugar da tela
# pyautogui.hotkey = Combina teclas
pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(1)

# Entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# Passo 2: Fazer login
# Selecionar o campo de email
pyautogui.click(x=757, y=356)

# Escrever o email
pyautogui.write('samuelcampelo25@gmail.com')
pyautogui.press('tab') # Passando para o próximo campo
pyautogui.write('senha')
pyautogui.click(x=975, y=513) # Clique no botão de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
produtos = pandas.read_csv("produtos.csv")
print(produtos)

# Passo 4: Cadastrar um produto

linha = 0

# Clicar no campo de código
pyautogui.click(x=762, y=242)

# Pegar da tabela o valor do campo para preencher
codigo = produtos.loc[linha, 'codigo']

# Preencher o campo
pyautogui.write(str(codigo))

# Passar para o próximo campo
pyautogui.press('tab')

# Preencher os campos
pyautogui.write(str(produtos.loc[linha, 'marca']))
pyautogui.press('tab')
pyautogui.write(str(produtos.loc[linha, 'tipo']))
pyautogui.press('tab')
pyautogui.write(str(produtos.loc[linha, 'categoria']))
pyautogui.press('tab')
pyautogui.write(str(produtos.loc[linha, 'preco_unitario']))
pyautogui.press('tab')
pyautogui.write(str(produtos.loc[linha, 'custo']))
pyautogui.press('tab')
obs = produtos.loc[linha, 'obs']
if not pandas.isna(obs):
    pyautogui.write(str(produtos.loc[linha, 'obs']))
    
pyautogui.press('tab')
pyautogui.press('enter')
# Dar scroll total para cima
pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até o fim
#pip install pyautogui    - no cmd
import pyautogui         
import time
import pandas as pd #pip install pandas numpy openpyxl    - no cmd

#Passo 1 - Entrar no sistema da empresa
        ## https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 2 - Fazer login
#Passo 3 - Importar a base de dados
#Passo 4 - Cadastrar um produto
# Passo 5 - Repetir isso até acabar a base de dados


# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar atalho -> pyautogui.hotkey("ctrl, c")
# rolar a tela pra baixo -> pyautogui.scroll(-1000 (numero negativo move pra baixo e positivo pra cima) )

#Passo 1
pyautogui.PAUSE = 1 # pausa antes de executar todas linhas de codigo
pyautogui.press("win")  # abrir a tela do wi    25.0ndows
pyautogui.write("opera") # digitar o nome do programa (navegador opera)
pyautogui.press("enter") # aperta enter 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #variavel com o link
#Passo 2
#pyautogui.write(link) #escrever o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # digitar o link
pyautogui.press("enter") # ou  - pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # digitar o link
time.sleep(2) # pausa por 2 sec em uma linha de cpythonimpressionador@gmail.com minha senhaodigo especifica
pyautogui.click(x = 2539, y = 562) #move o mouse ppythonimpressionador@gmail.comara a posiçao desejada
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x = 2609, y = 700)
#Passo 3
time.sleep(2)
tabela = pd.read_csv("produtos.csv")
print(tabela)
#Passo 4
for linha in tabela.index:  #loop para ler a tabela toda
    pyautogui.click(x=2554, y=437)
   
    #codigo
    codigo = tabela.loc[linha, "codigo"] #identificar o campo
    pyautogui.write(str(codigo))
    pyautogui.press("tab") #passar para o proximo codigo

    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):    # verifica se o valor é vazio
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") #enviar 
    pyautogui.scroll(5000) #rolar ate o inicio da paghttps://dlp.hashtagtreinamentos.com/python/intensivao/login


#Passo 5 - Repetir isso até acabar a base de dados

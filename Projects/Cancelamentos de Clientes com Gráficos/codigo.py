#Passo a passo do projeto:
    #Passo 1 - Importar a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")

    #Passo 2 - Visualizar a base de dados
print(tabela) #ou print(tabela)

#Passo 3 - Corrigir os erros da base de dados - identificar colunas inuteis e valores vazios e remover

tabela = tabela.drop(columns="CustomerID") #remove uma coluna desnecessaria 

tabela = tabela.dropna() # remove as linhas que tem valores vazios

print(tabela.info()) #resumo da base de dados, informaçoes

#Passo 4 - Analise inicial dos cancelamentos

#quantas pessoas cancelaram e quantas nao cancelaram
print(tabela["cancelou"].value_counts(normalize=True)) #nornmalize coloca o valor em porcentagem

#Passo 5 - Analise das causas dos cancelamentos (como as colunas das bases impactam no cancelamento) - #graficos e dashboards
import plotly.express as px

for coluna in tabela.columns: #criando um grafico para cada coluna    
    grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou") #criar o grafico
    grafico.show() #exibir o grafico


    #clientes com contrato mensal TODOS cancelam
    #oferecer descontos nos planos anuais e trimestrais
#clientes que ligal mais de que 4 vezes no callcenterm, cancelam
    #criar um processo para resolver o problema do cliente e, no maximo 3 ligações
#clientes que atrasaram mais de 20 dias, cancelaram
    #politica de resolver atrasos em até 10 dias (equipe financeira)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]    #filtrar
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize = True)) # em percentual
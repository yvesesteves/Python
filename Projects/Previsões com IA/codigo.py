#Passo a Passo:
#Passo 0 - Entender o desafio da empresa
#Passo 1 - Importar a base de dados
#Passo 2 - Preparar a base de dados para a IA
#Passo 3 - Criar um modelo IA -> Score de Credito (ruim, médio, bom)
#Passo 4 - Escolher o melhor modelo
#Passo 5 - Usar a IA para fazer novas previsões

import pandas as pd
tabela = pd.read_csv("clientes.csv")
print(tabela)
print(tabela.info())

#profissao
#mix_credito
#comportamento_pagamento
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

#codificador -> aplicar na coluna profissão
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])

#codificador -> aplicar na coluna mix_credito
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])

#codificador -> aplicar na coluna comportamento_pagamento
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

print(tabela.info())

# aprendizado de máquina (dados de treino e dados de teste)
# y - a coluna que quer prever
# x - sao as colunas q vai usar para fazer a previsao
# nao se usa a coluna id_cliente pois é um numero aleatorio

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# criar a inteligencia artificial
# arvores de decisao -> RandomForest
# KNN -> Vizinhos próximos -> Kneighbors

# importa a IA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# cria a IA
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

#treinar a iIA
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)


#testar e comparar os modelos
#curacia
from sklearn.metrics import accuracy_score

previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

print(accuracy_score(y_teste, previsao_arvoredecisao)) #melhor modelo de acordo com o teste
print(accuracy_score(y_teste, previsao_knn))

#melhor modelo? modelo_arvoredecisao
#fazer novas previsões
#importar novos clientes
tabela_novos_clientes = pd.read_csv("novos_clientes.csv")
print(tabela_novos_clientes)


#codificar os novos clientes
#codificador -> aplicar na coluna profissão
tabela_novos_clientes["profissao"] = codificador.fit_transform(tabela_novos_clientes["profissao"])

#codificador -> aplicar na coluna mix_credito
tabela_novos_clientes["mix_credito"] = codificador.fit_transform(tabela_novos_clientes["mix_credito"])

#codificador -> aplicar na coluna comportamento_pagamento
tabela_novos_clientes["comportamento_pagamento"] = codificador.fit_transform(tabela_novos_clientes["comportamento_pagamento"])


# fazer as previsões
previsoes = modelo_arvoredecisao.predict(tabela_novos_clientes)
print(previsoes)

# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import datetime

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

cont = 0
while cont < 21:
  print("Amostra: "+str(cont),data_list[cont+1])
  cont+=1

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

cont = 0
for i in range(20):
  print("Número:",cont+1, "Gênero:",data_list[i][-2])
  cont+=1

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
def column_to_list(data, index):
    """ Função retona uma lista contendo as amostras de uma determinada coluna
    Argumentos:
    	data = lista que contem todas as colunas do arquivo
    	index = posição da coluna desejada
    
    Saida:
		column_list = lista que contem as informações extraidas de acordo com o index, no caso os generos
    """
    column_list = []
    
    for i in data:
        column_list.append(i[index])
    
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

male = 0
female = 0

for i in column_to_list(data_list,-2):
    if i.lower() == "male":
        male+=1
    elif i.lower() == "female":
        female+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """ Função distingue os generos que foram relatados e os que foram deixados em branco pelos usuarios
    Argumentos:
    data_list = lista contendo informações de toda a coluna de generos
    Saida:
    lista contendo apenas generos feminino e masculino
    """
    male = 0
    female = 0
    
    for i in column_to_list(data_list,-2):
        if i.lower() == "male":
            male+=1
        elif i.lower() == "female":
            female+=1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list): 
    """Retorna uma string de qual foi o genero que ocorreu em maior quantidade, chama a função anterior count_gender e compara os resultados
    Argumentos:
    data_list = lista que contem as informações da coluna sobre generos
    Saida:
    answer = string que contem qual foi o genero que mais ocorreu
    """
    count_gender(data_list)
    if male > female:
    	answer = "Male"
    elif female > male:
    	answer = "Female"
    else:
    	answer = "Equal"
  
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def user_types(data_list):
	"""Retorna uma lista com os tipos de clientes e a quantidade de cada
	Argumentos:
	data_list = coluna que contem informações sobre os tipos de clientes
	Saida:
	lista retornando o numero de clientes de cada tipo que foi encontrado no arquivo
	"""
	cliente = 0
	dependente = 0
	inscrito = 0

	for i in column_to_list(data_list,-3):
		if i.lower() == "customer":
			cliente+=1
		elif i.lower() == "dependent":
			dependente+=1
		elif i.lower() == "subscriber":
			inscrito+=1
		else:
			continue

	return [cliente,dependente,inscrito]

types = ["Customer","Dependent","Subscriber"]
quantity = user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos,quantity)
plt.ylabel("Quantidade")
plt.xlabel("\nTipos de usuários")
plt.xticks(y_pos,types)
plt.title("Quantidade por tipo de cliente")
plt.show(block = True)

input("Aperte Enter para continuar...")

# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque a lista  de generos tem alguns valores que estão vazios."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

a = trip_duration_list[1]
for i in trip_duration_list:
	if int(i) < int(a):
		min_trip = int(i)
		a = min_trip

b = trip_duration_list[1]
for i in trip_duration_list:
	if int(i) > int(b):
		max_trip = int(i)
		b = max_trip

ac = 0
for i in trip_duration_list:
    ac += int(i)
mean_trip = round(ac / len(trip_duration_list))

lista = sorted(int(i) for i in trip_duration_list)
t = len(lista)
o = t/2
o = int(o)
if t%2 == 0:
	median_trip = lista[o]
else:
	median_trip = round((lista[o]+lista[o+1])/2)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

start_stations = set(column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
    Argumentos:
    column_list = lista da colunas do arquivo
    Saida:
    item_types = lista com os tipos
    count_items = lista de contagem dos itens
    """
    item_types = []
    count_items = []

    item_types = set(column_list)

    for i in item_types:
    	if i in item_types:
    		c = column_list.count(i)
    		count_items.append(c)

    return item_types,count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

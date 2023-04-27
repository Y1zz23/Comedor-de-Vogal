# pede ao usuário para inserir uma palavra
palavra = input("Insira uma palavra: ")

# converte a palavra em maiúsculas
palavra = palavra.upper()

# cria uma lista de vogais
vogais = ['A', 'E', 'I', 'O', 'U']

# cria uma string vazia para armazenar as letras não consumidas
sem_vogais = ""

# loop for para percorrer cada letra da palavra
for i in palavra:
    # execução condicional para verificar se a letra é uma vogal
    if i in vogais:
        # se for uma vogal, use a declaração continue para ignorá-la e ir para a próxima iteração
        continue
    else:
        # se não for uma vogal, adicione a letra à string sem_vogais
        sem_vogais += i

# imprime as letras não consumidas na tela, cada uma delas em uma linha separada
for i in sem_vogais:
    print(i)
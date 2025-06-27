import time
def lin():
    print(30*"=")

def procurador():
    N1 = input("Digite o Nome do Livro: ").strip().upper()  #Criando uma função para encontrar um determinado livro dentro da lista.
    encontrado = False                                      # Encontrado = recebendo False para que possamos quebrar o loop
    for livro in lista:                                     # Procurando  em lista
        if N1 == livro[0]:                                  # SE N1 estiver dentro da subclass Livro mostrará que foi encontrado
            print(f'O livro "{N1}" está disponível.')
            print(f'Estoque disponível {livro[3]}')
            retirar=str(input("\033[32m Dejesa Fazer a retirada ? Sim/Não\033[0m"))
            if retirar in ["sim", "s"]:                    # se o estoque estiver disponível  eo usuario quiser fazer a retirada
                livro[3]-=1                                # a subclasse receberá o valor menos 1
                if livro[3] ==0:
                    print("o livro se encontra no sistema,Mas sem estoque disponivel")
                print(f'Retirada Realizada com sucesso estaram {livro[3]}')
                encontrado = True
            break

    if not encontrado:
        print("Livro NÃO Encontrado!")
        print('Verifique se está digitado corretamente.')


lista=[] #Declarando a lista fora do loop para receber os dados.
tupla = ()
while True:
    lin()
    print("\033[32mCadastramento de Sebo\033[0m")
    lin()
    nome = input("Digite o Nome do Livro:").strip().upper()
    autor = (str(input("Digite o Nome do autor"))).strip().upper()
    data = int(input("Digite a data de lançamento"))
    estoque = (int(input("Estoque: ")))
    lista.append([nome,autor,data,estoque]) # A lista aprende os dados solicitados e guarda todos de uma vez

    continuar = input("\033[32mDejesa continuar?..\033[0m").strip().lower()
    if continuar in ["nao", "n", "não"]:
        break
for livro in lista:
    print(f"Titulo:\033[32m{livro[0]}\033[0m  Autor:\033[31m{livro[1]}\033[0m - Publicação: \033[33m{livro[2]}\033[0m Estoque: \033[32m{livro[3]}\033[0m") # Exibe o livro cadastrado e o estoque
print(30*"-")
procurador()
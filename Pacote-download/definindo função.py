def linhas():
    print("-=-"*10)
    print("\033[32m Iniciando Programa\033[0m")
    print("-=-" * 10)


linhas()
comprimento=int(input('Digite a largura: '))
largura=int(input("Digite o comprimento"))
area= comprimento*largura
print(f'O comprimento da area é {area}')

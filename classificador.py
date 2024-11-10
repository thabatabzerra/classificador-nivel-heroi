# Função para classificar o herói com base na experiência
def classificar_heroi(nome, xp):
    if xp < 1000:
        nivel = 'Ferro'
    elif 1001 <= xp <= 2000:
        nivel = 'Bronze'
    elif 2001 <= xp <= 5000:
        nivel = 'Prata'
    elif 5001 <= xp <= 7000:
        nivel = 'Ouro'
    elif 7001 <= xp <= 8000:
        nivel = 'Platina'
    elif 8001 <= xp <= 9000:
        nivel = 'Ascendente'
    elif 9001 <= xp <= 10000:
        nivel = 'Imortal'
    else:
        nivel = 'Radiante'
    
    # Exibe o resultado
    print(f"O Herói de nome {nome} está no nível de {nivel}.")

# Testando a função com um exemplo
nome_heroi = input("Qual o nome do herói? ")
xp_heroi = int(input("Qual a quantidade de experiência do herói? "))
classificar_heroi(nome_heroi, xp_heroi)

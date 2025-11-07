import os

def processar_diretorio(diretorio_alvo):
    print(f"Caminho recebido: {diretorio_alvo}")

    if os.path.isdir(diretorio_alvo):
        print("O diretório existe")

        try:
            itens = os.listdir(diretorio_alvo)

            for i, item in enumerate(itens[:5]):
                print(f"{item}")
            
        except PermissionError:
            print("Erro: permissão negada")
    else:
        print(f"O diretório {diretorio_alvo} não é um diretório válido")
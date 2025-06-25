import os


file = 'wordlist.txt'

user = os.path.expanduser('~')

origem = os.path.join(user,'Downloads')

destino = os.path.join(origem,'Imagens PNG')
destino_minecraft = os.path.join(destino,'MINECRAFT')
destino_roblox = os.path.join(destino,'ROBLOX')
destino_construcao = os.path.join(destino,'BUILDS')

extensao = '.png'

#construcao = 'construcao'
minecraft = 'minecraft'
roblox = 'roblox'

def detectar_e_mover_png():
    if not os.path.exists(destino):
        print(f'A pasta {destino} não existe, criando uma...')
        os.makedirs(destino)

    arquivos_movidos = 0

    for nome_arquivo in os.listdir(origem):
        if nome_arquivo.lower().endswith(extensao):
            caminho_origem = os.path.join(origem, nome_arquivo)
            caminho_destino = os.path.join(destino,nome_arquivo)

            if os.path.isfile(caminho_origem):
                try:
                    os.rename(caminho_origem,caminho_destino)
                    arquivos_movidos += 1
                except Exception as e:
                    print(f' -> ERRO ao mover {nome_arquivo}: {e}')

    if arquivos_movidos > 0:
        print("Sucesso!")
    else:
        print('Nenhum arquivo novo com a extensão foi encontrado')

def detectar_minecraft():
    if not os.path.exists(destino_minecraft):
        print(f'A pasta {destino_minecraft} não existe, criando uma...')
        os.makedirs(destino_minecraft)

    arquivos_movidos_minecraft = 0

    for nome_arquivo_minecraft in os.listdir(destino):
        if nome_arquivo_minecraft.lower().startswith(minecraft):
            caminho_origem_minecraft = os.path.join(destino, nome_arquivo_minecraft)
            caminho_destino_minecraft = os.path.join(destino_minecraft,nome_arquivo_minecraft)
            try:
                os.rename(caminho_origem_minecraft,caminho_destino_minecraft)
                arquivos_movidos_minecraft += 1
            except Exception as e:
                print(f' -> ERRO ao mover {nome_arquivo_minecraft}: {e}')
    
    if arquivos_movidos_minecraft > 0:
        print("Sucesso para o MINECRAFT")
    else:
        print("MINECRAFT -> Nenhum arquivo novo com esse nome...")

def detectar_roblox():
    if not os.path.exists(destino_roblox):
        print(f'A pasta {destino_roblox} não existe, criando uma...')
        os.makedirs(destino_roblox)

    arquivos_movidos_roblox = 0

    for nome_arquivo_roblox in os.listdir(destino):
        if nome_arquivo_roblox.lower().startswith(roblox):
            caminho_origem_roblox = os.path.join(destino, nome_arquivo_roblox)
            caminho_destino_roblox = os.path.join(destino_roblox,nome_arquivo_roblox)
            try:
                os.rename(caminho_origem_roblox,caminho_destino_roblox)
                arquivos_movidos_roblox += 1
            except Exception as e:
                print(f' -> ERRO ao mover {nome_arquivo_roblox}: {e}')

    if arquivos_movidos_roblox > 0:
        print("Sucesso para o ROBLOX")
    else:
        print("ROBLOX -> Nenhum arquivo novo com esse nome...")

def carregar_palavras(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f]
            print('Palavras carregadas')
            return palavras
    except FileNotFoundError:
        print(f'ERRO -> Arquivo {file} não encontrado')
        return []

def detectar_wordlist_construcao(palavras_chave):
    if not os.path.exists(destino_construcao):
        print(f'A pasta {destino_construcao} não existe, criando uma...')
        os.makedirs(destino_construcao)

    arquivos_movidos_construcao = 0

    for nome_arquivo_construcao in os.listdir(destino):
        if nome_arquivo_construcao.endswith(extensao):

            for palavra in palavras_chave:
                if palavra in nome_arquivo_construcao.lower():
                    caminho_origem_construcao = os.path.join(destino,nome_arquivo_construcao)
                    caminho_destino_construcao = os.path.join(destino_construcao,nome_arquivo_construcao)
                    try:
                        os.rename(caminho_origem_construcao,caminho_destino_construcao)
                        arquivos_movidos_construcao += 1
                    except Exception as e:
                        print(f' -> ERRO ao mover {nome_arquivo_construcao}: {e}')


if __name__ == '__main__':
    detectar_e_mover_png()
    detectar_minecraft()
    detectar_roblox()

    palavras_construcao = carregar_palavras(file)

    if palavras_construcao:
        detectar_wordlist_construcao(palavras_construcao)

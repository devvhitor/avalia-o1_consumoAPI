import requests

def buscar_cep(cep):
    url = f'http://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if 'erro' not in dados:
            return dados
    print('Falha ao buscar informações do CEP.')
    return None

def exibir_informacoes(dados):
    if dados:
        print('Informações do CEP:')
        print(f'CEP: {dados.get("cep", "N/A")}')
        print(f'Estado: {dados.get("uf", "N/A")}')
        print(f'Cidade: {dados.get("localidade", "N/A")}')
        print(f'Bairro: {dados.get("bairro", "N/A")}')
        print(f'Rua: {dados.get("logradouro", "N/A")}')
    else:
        print('Nenhuma informação encontrada para este CEP.')

def main():
    print("Bem-vindo ao buscador de CEP!")
    cep = input("Digite o CEP que deseja buscar (apenas números): ")
    dados = buscar_cep(cep)
    exibir_informacoes(dados)
    input("Pressione Enter para sair...")  # Adiciona uma pausa antes de fechar a tela

if __name__ == "__main__":
    main()

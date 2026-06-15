import json

def load_reports(path_file):
    """Lê o arquivo JSON e retorna a lista de dicionários."""
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            print(f"Sucesso! {len(dados)} relatórios carregados.")
            return dados
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return []
# Teste de execução local
if __name__ == "__main__":
    reports = load_reports('../dados/dataset.json')
    if reports:
        print("Exemplo do primeiro relatório:", reports[0]['texto'])
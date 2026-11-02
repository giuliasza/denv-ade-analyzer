import pandas as pd #ler o csv
from Bio import Entrez #usar o ncbi
import time #pausar o código

Entrez.email = "msgiuliamartins@gmail.com" 

def leitura_id(caminho_csv: str, coluna_id: str, tamanho_lote: int = 2): #function com parametros tipados
    try: #"faz isso"
        print(f"Abrindo {caminho_csv} em lotes de {tamanho_lote}...")
        lotes_csv = pd.read_csv(caminho_csv, usecols=[coluna_id], chunksize=tamanho_lote) #usando o metodo read do panda, e aplicando o chunksize para dividir o csv em lotes

        for lote in lotes_csv:
            lista_ids = lote[coluna_id].dropna().tolist() #transformando a coluna em uma lista, e removendo os valores nulos com dropna
            yield lista_ids #o yield é usado para retornar um gerador, que permite iterar sobre os lotes de IDs sem carregar tudo na memória de uma vez

    except FileNotFoundError:
        print(f"\n⚠️ Aviso: CSV não encontrado no caminho '{caminho_csv}'.")
        print("🔄 Entrando em Modo de Demonstração com dados de teste automáticos...")
        # Fallback automático: injeta IDs diretamente se o usuário não tiver o CSV
        yield ["JN638327.1", "KF672791.1"]
        
    except Exception as e:
        print(f"Erro inesperado ao ler CSV: {e}")
        yield []    
def teste(caminho_csv: str):

    nome_coluna = "ID_GenBank"

    gerador_lotes = leitura_id(caminho_csv, nome_coluna, tamanho_lote=2) #chamando a função leitura_id e passando os parametros
    primeiro_lote = next(gerador_lotes, None) #pegando o primeiro lote do gerador

    if primeiro_lote:
        ids_formatados = ",".join(primeiro_lote) #formatando a lista de IDs em uma string separada por vírgulas, o join é usado para concatenar os elementos da lista em uma única string, com vírgulas entre eles
        print(f"IDs do primeiro lote: {ids_formatados}")

        req = Entrez.efetch(db="nucleotide", id=ids_formatados, rettype="fasta", retmode="text") #fazendo a requisição ao NCBI para buscar as sequências em formato FASTA
        resultado = req.read() 
        req.close() #fechando a requisição para liberar recursos
        print(f"Resultado da requisição:\n{resultado[:500]}")
            

if __name__ == "__main__":
    teste("data/amostra_rai.csv")
import csv  # Importando o módulo csv

# Nome do arquivo CSV
arquivo_csv = "pessoas.csv"

try:
   
    with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

       
        for linha in leitor:
            print(", ".join(linha))  # Exibe os dados separados por vírgula

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")

from datetime import date  # Importação correta

def idade_em_dias(ano):
    ano_atual = date.today().year  # Correção do atributo 'year' ao invés de 'ano'
    idade_anos = ano_atual - ano
    return idade_anos * 365  # Correção da palavra-chave 'return'

ano_nascimento = int(input("Digite o ano de seu nascimento: "))  # Variável corrigida para manter coerência
print(f"Você tem aproximadamente {idade_em_dias(ano_nascimento)} dias de vida.")  # Correção do nome da variável

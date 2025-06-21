from contagem.letras import contar_letras
from contagem.palavras import contar_palavras
from contagem.palavrasComplexas import contar_palavras_complexas, carregar_banco_palavras
from contagem.frases import contar_frases

def ler_arquivo_texto(caminho='texto.txt'):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' não encontrado.")
        return ""

if __name__ == "__main__":
    texto = ler_arquivo_texto()
    
    if texto:
        total_letras = contar_letras(texto)
        total_palavras = contar_palavras(texto)

        print(f"Total de letras: {total_letras}")
        print(f"Total de palavras: {total_palavras}")


# Contagem de palavras complexas
texto = open('texto.txt', 'r', encoding='utf-8').read()
banco = carregar_banco_palavras()
complexas = contar_palavras_complexas(texto, banco)

print(f"Palavras complexas: {complexas}")


# Contagem de frases com opções de ponto e vírgula e dois pontos
chk_ponto_e_virgula = True
chk_dois_pontos = True

total_frases = contar_frases(
    texto,
    considerar_ponto_e_virgula=chk_ponto_e_virgula,
    considerar_dois_pontos=chk_dois_pontos
)

print(f"Total de frases: {total_frases}")
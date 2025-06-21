import os
from contagem.letras import contar_letras
from contagem.palavras import contar_palavras
from contagem.silabas import contar_silabas
from contagem.frases import contar_frases
from contagem.palavrasComplexas import carregar_banco_palavras, contar_palavras_complexas

# Carregar banco de palavras mais comuns
banco = carregar_banco_palavras()

# Caminho para a pasta com os textos
PASTA_TEXTOS = "textos"

# Cabeçalho da tabela
print(f"{'arquivo':30} {'Letras':>7} {'Sílabas':>8} {'Palavras':>9} {'Sentencas':>10} {'Complexas':>11}" 
        f"{'Flesch':>7} {'Flesch-Kincaid':>14} {'Gunning Fog':>12} {'ARI':>4} {'CLI':>4} {'Gulpease':>9}")

resultados = []

# Processar cada arquivo .txt na pasta
for nome_arquivo in os.listdir(PASTA_TEXTOS):
    if nome_arquivo.endswith(".txt"):
        caminho = os.path.join(PASTA_TEXTOS, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            texto = f.read()

        letras = contar_letras(texto)
        silabas = contar_silabas(texto)
        palavras = contar_palavras(texto)
        complexas = contar_palavras_complexas(texto, banco)
        sentencas  = contar_frases(texto)

        flesch = 226 - 1.04 * (palavras) / sentencas  - 72 * silabas / (palavras)
        fleschKincaid = 0.36 * (palavras) / sentencas + 10.4 * silabas / (palavras) - 18
        gunningFog = 0.49 * palavras / sentencas + 19 * complexas / palavras + 0
        ari = 4.6 * letras / (palavras) + 0.44 * (palavras) / sentencas - 20
        cli = 5.4 * letras / (palavras) - 21 * sentencas / (palavras) - 14
        gulpease = 89 + (300 * sentencas - 10 * letras) / palavras

        linha = {
            "arquivo": nome_arquivo,
            "letras": letras,
            "silabas": silabas,
            "palavras": palavras,
            "sentencas": sentencas,
            "complexas": complexas,
            "flesch": round(flesch, 1),
            "fleschKincaid": round(fleschKincaid, 1),
            "gunningFog": round(gunningFog, 1),
            "ari": round(ari, 1),
            "cli": round(cli, 1),
            "gulpease": round(gulpease, 1),
        }
        resultados.append(linha)

        print(f"{nome_arquivo:30} {letras:7} {silabas:8} {palavras:9} {sentencas:10} {complexas:11}" 
              f" {flesch:6.1f} {fleschKincaid:14.1f} {gunningFog:12.1f} {ari:4.1f} {cli:4.1f} {gulpease:9.1f}")

import csv
import json

# Criar pasta resultados/ se não existir
os.makedirs("resultados", exist_ok=True)

# Salvar como .txt (OriginLab)
with open("resultados/resultados_origin.txt", "w", encoding="utf-8") as f:
    f.write("\t".join(resultados[0].keys()) + "\n")
    for linha in resultados:
        f.write("\t".join(str(v) for v in linha.values()) + "\n")

# Salvar como .csv (Excel)
with open("resultados/resultados.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
    writer.writeheader()
    writer.writerows(resultados)

# Salvar como .json
with open("resultados/resultados.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print("\nDados salvos na pasta 'resultados/' como:")
print(" - resultados_origin.txt (formato tabulado para Origin)")
print(" - resultados.csv         (compatível com Excel)")
print(" - resultados.json        (para uso em aplicações)")

# ALT – Análise de Legibilidade Textual

**alt-legibilidade** é um pacote Python de código aberto que permite analisar a legibilidade de textos em **língua portuguesa**. Ele calcula automaticamente o número de letras, palavras, sílabas, frases e diversos índices consagrados de legibilidade (como Flesch, Flesch-Kincaid, Gunning Fog, ARI, CLI e Gulpease).

📌 Página oficial do projeto: [https://legibilidade.com/](https://legibilidade.com/)

📄 Artigo de referência:  
Gleice Carvalho de Lima Moreno, Marco P. M. de Souza, Nelson Hein, Adriana Kroenke Hein,  
**ALT: um software para análise de legibilidade de textos em Língua Portuguesa**.  
arXiv:2203.12135 [cs.CL]  
[https://doi.org/10.48550/arXiv.2203.12135](https://doi.org/10.48550/arXiv.2203.12135)

---

## 🚀 Instalação

Você pode instalar o pacote diretamente via [PyPI](https://pypi.org/project/alt-legibilidade/) com:

```bash
pip install alt-legibilidade

# 1. Crie uma pasta chamada "textos" no mesmo diretório onde você irá executar o comando:
mkdir textos

# 2. Coloque dentro dela os arquivos que deseja analisar.
# Os seguintes formatos são aceitos:
# - .txt
# - .pdf
# - .docx

# 3. Execute o programa no terminal com:
alt-legibilidade

# O terminal mostrará uma tabela com os resultados e salvará três arquivos na pasta resultados/:

# resultados_origin.txt  → ideal para uso no OriginLab
# resultados.csv         → compatível com Excel, LibreOffice etc.
# resultados.json        → útil para desenvolvedores e APIs
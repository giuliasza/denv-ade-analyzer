# 🧬 DENV ADE Analyzer (DENV_Duo)

Este pacote Python está sendo desenvolvido como parte do projeto prático da **PyLadies Bioinfo (2026)**.

## Objetivo
Nosso objetivo é construir uma aplicação de nível intermediário que analise a distância genética da Proteína E dos serotipos do vírus da Dengue (DENV-1 a 4) extraídos do NCBI. A partir da manipulação desses arquivos FASTA e das anotações biológicas, o pacote avalia a relação das mutações com o fenômeno de Escape Imunológico (ADE - *Antibody-Dependent Enhancement*).

## A Dupla (DENV_Duo)
* **Desenvolvimento e Arquitetura Python:** Maria Giulia Souza Martins
* **Regras Biológicas e Validação Científica:** Raissa Alves Teixeira Pinto

## Tecnologias Utilizadas
* `Python 3.x`
* `Biopython` (Manipulação das sequências)
* `Pandas` (Leitura de metadados e arquivos de anotação)

## Como testar:

* 1: Copie a url desse repositório
* 2: Dentro de uma pasta, coloque no terminal da sua IDE:
```bash 
git clone url-do-repo"
```
* 3: Entre na pasta local do projeto:
```bash
cd denv-ade-analyzer"
```
* 4: Crie o ambiente virtual (venv):
```bash
python3 -m venv venv
source venv/bin/activate  # Em Mac/Linux
# venv\Scripts\activate   # Em Windows
```
* 5: Instale as dependências:
```bash
pip install -r requirements.txt
```
* 6: Rode no terminal:
```bash
python3 src/teste.py
```



---
*Status: Em desenvolvimento (Checkpoint 2)*
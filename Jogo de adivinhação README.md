# ADS-2026
# 🎯 Jogo de Adivinhação

Um jogo simples desenvolvido em **Python**, no qual o jogador deve tentar adivinhar um número secreto entre **1 e 100**.

O jogador possui **7 tentativas** para acertar o número.

## 🕹️ Como funciona

1. O computador escolhe aleatoriamente um número entre **1 e 100**.
2. O jogador informa um palpite.
3. O programa verifica o palpite:

   * Se o número for **maior** que o número secreto, informa que o palpite está alto.
   * Se o número for **menor**, informa que o palpite está baixo.
   * Se o jogador acertar, o jogo informa que ele venceu.
4. Caso o jogador não acerte após **7 tentativas**, o número secreto é revelado.

## 📋 Regras

* O número secreto está entre **1 e 100**.
* O jogador tem no máximo **7 tentativas**.
* Os palpites devem ser números inteiros.
* O jogo termina quando o jogador acerta ou quando as 7 tentativas são utilizadas.

## 💻 Tecnologias

* **Python 3**
* Biblioteca `random`

## ▶️ Como executar

Clone o repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd nome-do-projeto
```

Execute o programa:

```bash
python adivinhacao.py
```

## 📌 Exemplo

```text
🎯 Jogo de Adivinhação

Estou pensando em um número entre 1 e 100.
Você tem 7 tentativas!

Tentativa 1/7
Digite seu palpite: 50

O número é maior!

Tentativa 2/7
Digite seu palpite: 75

O número é menor!

Tentativa 3/7
Digite seu palpite: 68

🎉 Parabéns! Você acertou!
```

## 👨‍💻 Autor

Desenvolvido como projeto de estudo em **Python**.

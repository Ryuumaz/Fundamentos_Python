'''
ENUNCIADO
    1. Pedir uma classificação quantitativa ao utilizador (deve estar entre 0 e 20)
    2. Exibir classificação qualitativa da classificação quantitativa introduzida:
        0-4: Fraco
        5-9: Insuficiente
        10-14: Suficiente
        15-20: Bom
        not 0 <= quantitativa <= 20: Inválida (ou seja, é um erro)

EXEMPLO:
    $ python classificacao_qualitativa1.py
    Insira uma classificação: 12
    Classificação qualitativa "Suficiente"

    $ python classificacao_qualitativa1.py
    Insira uma classificação: 7
    Classificação qualitativa "Insuficiente"

    $ python classificacao_qualitativa1.py
    Insira uma classificação: 17
    Classificação qualitativa "Bom"

    $ python classificacao_qualitativa1.py
    Insira uma classificação: 31
    ATENÇÃO: classificação 31 INVÁLIDA!
'''

nota = int(input("Indica a tua nota (0-20): "))

if 0 <= nota <= 4:
    print("Fraco.")
elif 5 <= nota <= 9:
    print("Insuficiente.")
elif 10 <= nota <= 14:
    print("Suficiente.")
elif 15 <= nota <= 20:
    print("Bom.")
elif not 0 <= nota <= 20:
    print("Nota inválida.")
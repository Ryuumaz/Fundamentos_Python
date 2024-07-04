'''
11. Vamos fazer um programa de adivinha. Este programa começa por solicitar um número ao utilizador e,
caso este número seja igual a um número pré-defnido (o número mágico), o programa felicita o
utlizador por ter acertado. Caso contrário, indica que o utilizador falhou.
'''

def main():
    num_magico = 10
    num = int(input("Tenta adivinhar o número mágico: "))

    if num < num_magico:
        print("O número mágico é maior!")
    elif num > num_magico:
        print("O número mágico é menor!")
    elif num == num_magico:
        print("Acertaste!")


if __name__ == "__main__":
    main()
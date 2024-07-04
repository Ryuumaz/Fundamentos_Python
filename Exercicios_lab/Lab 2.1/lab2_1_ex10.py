''' 
10. Fazer um programa para calcular a contribuição para Segurança Social, IRS e o sindicato a partir do
    salário bruto, que é um atributo de entrada.
    • SS - 11,5%
    • IRS - 25%
    • Sindicato - 0,5 %
O programa deve imprimir o valor das contribuições e o valor do salário líquido.
'''

import decimal
from decimal import Decimal as dec

print("\nExercício 10\n")

sal_bruto = dec(input("Indica o teu salário bruto: "))

ss = sal_bruto * dec(0.115)
irs = sal_bruto * dec(0.25)
sind = sal_bruto * dec(0.005)

sal_liquido = sal_bruto - ss - irs - sind

print()
print(f"O salário bruto é           | {sal_bruto:^10.2f}€ |")
print(f"A contribuição para a SS    | {ss:^10.2f}€ |")
print(f"O desconto do IRS é         | {irs:^10.2f}€ |")
print(f"O desconto do sindicato é   | {sind:^10.2f}€ |")
print(f"E o salário líquido é       | {sal_liquido:^10.2f}€ |")
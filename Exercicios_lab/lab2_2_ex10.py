'''
10. Faça um programa para calcular o preço de venda final de um produto. Para tal solicita, através da linha de
comandos (shell), o preço do produto, o valor da taxa de IVA a aplicar e (opcionalmente) o valor de um
desconto a aplicar ao valor final do produto. O programa deverá dar instruções ao utilizador de como deve
ser invocado. O valor do IVA e do desconto deve ser dado em percentagem.
'''

import sys
from decimal import Decimal as dec

if len(sys.argv) not in (3, 4):
    print(f"Uso: {sys.argv[0]} PRECO TAXA_IVA [DESCONTO]", file = sys.stderr)
    sys.exit(2)

preco = dec(sys.argv[1])
iva = dec(sys.argv[2])
if len(sys.argv) == 4:
    desconto_adicional = dec(sys.argv[3])
else:
    desconto_adicional = dec('0')

desconto_adicional_calculado = desconto_adicional / 100
iva_calculado = iva / 100

preco_final = dec(preco * (1 + iva_calculado) * (1 - desconto_adicional_calculado))

print()
print("Valor do produto s/ descontos: %.2f€" % preco)
print("Valor do IVA: %.2f€" % iva_calculado)
print("Valor do desconto adicional: %.2f€" % desconto_adicional_calculado)
print("Valor do produto c/ descontos: %.2f€" % preco_final)
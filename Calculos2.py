import decimal
from decimal import Decimal as dec

num1  = dec(input("Indica o número: "))

print("O dobro: ", num1 * 2)
print("O triplo: ", num1 * 3)
print("O quadrado: ", num1 ** 2)
print("O cubo: ", num1 ** 3)
print("Expressão (2.5x + 10): ", dec('2.5') * num1 + 10)
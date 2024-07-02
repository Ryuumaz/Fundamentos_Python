import decimal
from decimal import Decimal as dec

num1  = dec(input("Indica o número: "))

print(f"O dobro               | {num1 * 2:^7.2f} |")
print(f"O triplo              | {num1 * 3:^7.2f} |")
print(f"O quadrado            | {num1 ** 2:^7.2f} |")
print(f"O cubo                | {num1 ** 3:^7.2f} |")
print(f"Expressão (2.5x + 10) | {dec('2.5') * num1 + 10:^7.2f} |")
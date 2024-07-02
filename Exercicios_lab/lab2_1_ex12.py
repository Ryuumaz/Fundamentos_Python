''' 
12. Faça um programa que produza na saída padrão uma carta formatada semelhante à indicada no exemplo
    que se segue. Deverá solicitar a introdução da informação em sublinhado, e dos restantes dados que achar
    necessários. A primeira linha e as últimas duas ("Caro Alberto/Armanda", "O seu," e "Arnaldo Antunes")
    deverão ser indentadas com 10 caracteres. A primeira linha de cada parágrafo deverá estar afastada 4
    caracteres da margem esquerda. A linha a tracejado deverá conter 20 traços e estar indentada com 7
    caracteres. Deverá dar as linhas de espaço indicadas no exemplo:
        Caro Alberto/Armanda,
        Venho por este meio convidá-lo/la para a cerimónia a realizar pelas (16h00) do dia
        (31/05/2036). Caro (Alberto/Armanda), o código de vestimento é formal, o que significa que
        deverá usar um fato com gravata/vestido e saltos altos.
        O dia (31/05/2036) é uma data muito especial para mim e contamos com a sua presença. O
        convite é extensível à sua (companheira/companheiro).
        Aguardamos a sua confirmação
        O seu,
        --------------------
        Arnaldo Antunes
'''
print("\nExercício 12\n")

nome = input("Indica o nome (Alberto/Armanda): ")
horas = int(input("Indica as horas: "))
minutos = int(input("Indica os minutos: "))
#dia = int(input("Indica o dia: "))
#mes = int(input("Indica o mês: "))
#ano = int(input("Indica o ano: "))

if nome == 'Alberto':
    linha1 = "Caro " + nome
    linha2 = "Venho por este meio convidá-lo para a cerimónia a realizar pelas " + str(horas) + "h" + str(minutos) + " do dia"
    print()
    print(f"{linha1:<10},")
    print(f"{linha2:<4}")

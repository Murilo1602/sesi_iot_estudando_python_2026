# Compara dois números para ver qual é o maior ou se são iguais

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais.")
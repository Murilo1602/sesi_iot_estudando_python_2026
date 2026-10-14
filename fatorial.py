# Calcula o fatorial de um número inteiro positivo

n = int(input("Digite um número inteiro positivo: "))
fatorial = 1

if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    for i in range(1, n + 1):
        fatorial *= i
    print("O fatorial de", n, "é", fatorial)
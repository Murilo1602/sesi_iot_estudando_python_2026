# Classifica o triângulo com base nos comprimentos dos lados

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("O triângulo é Equilátero (todos os lados iguais).")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é Isósceles (dois lados iguais).")
    else:
        print("O triângulo é Escaleno (todos os lados diferentes).")
else:
    print("Os valores informados não formam um triângulo válido.")
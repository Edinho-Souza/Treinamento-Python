# Condicional Simples (1 ou 2 respostas):
idade = 16

if idade >= 18:
    print("Pode obter a CNH")
else:
    print("Não pode obter a CNH")
    
# Condicional Aninhada/Composta:
media = 7

if media == 10:
    print("Nota máxima! Parabéns!")
elif media >= 9:
    print("Ótimo")
elif media >= 8:
    print("Bom!")    
elif media >= 7:
    print("Na média")
elif media >= 5:
    print("Em exame")
else:
    print("Reprovado")
    
# Operadores Lógicos:
valor = 84

if valor >= 0 and valor <= 100:
    print("O valor está entre 0 e 100")
else:
    print("O valor não está entre 0 e 100")

print("Informe o valor da compra:")
total = float(input())
formaPgto = "À vista"

if total >= 100 and formaPgto == "À vista":
    print("Valor a pagar R$ " + str(total * 0.9))
else:
    print("Valor a pagar R$ " + str(total))
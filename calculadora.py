valor1 = int(input("Digite o primeiro valor"))
valor2 = int(input("Digite o segundo valor"))

print("Veja as opções:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

opcao = int(input("Escolha uma opção"))

if opcao == 1:
    resultado = valor1 + valor2
    print("Seu resultado é: ", resultado)
elif opcao == 2:
    resultado = valor1 - valor2
    print("Seu resultado é: ", resultado)
elif opcao == 3:
    resultado = valor1 * valor2
    print("Seu resultado é: ", resultado)
else:
    resultado = valor1 / valor2
    print("Seu resultado é: ", resultado)
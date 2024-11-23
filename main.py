import math


def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("Selecione a operação desejada:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raiz Quadrada")
        print("6. Sair")

        escolha = input("Insira o número da operação que deseja: ")

        if escolha == '1':
            numeros = input("Insira os números separados por virgulas: ")
            numeros = list(map(float, numeros.split(',')))
            resultado = sum(numeros)
            print(f"Resultado: {resultado}")

        elif escolha == '2':
            numeros = input("Insira os números separados por virgulas: ")
            numeros = list(map(float, numeros.split(',')))
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado -= num
            print(f"Resultado: {resultado}")

        elif escolha == '3':
            numeros = input("Insira os números separados por virgulas: ")
            numeros = list(map(float, numeros.split(',')))
            resultado = 1
            for num in numeros:
                resultado *= num
            print(f"Resultado: {numeros} {resultado}")

        elif escolha == '4':
            numeros = input("Insira os números separados por virgulas: ")
            numeros = list(map(float, numeros.split(',')))
            resultado = numeros[0]
            for num in numeros[1:]:
                if num == 0:
                    print("A divisão por zero não é permitida.")
                    break
                resultado /= num
            else:
                print(f"Resultado:({numeros[0]}) : ({numeros[1]}) = {resultado}")

        elif escolha == '5':
            num = float(input("Insira o número para calcular a raiz quadrada: "))
            if num >= 0:
                print(f"Resultado: √{num} = {math.sqrt(num)}")
            else:
                print("Não é possível calcular a raiz quadrada de um número negativo!")

        elif escolha == '6':
            print("Saiu da calculadora.")
            break

        else:
            print("Escolha inválida. Tente novamente.")

calculadora()

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: Digite um número válido!")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: Digite um número válido!")

while True:
    operacao = input("Digite a operação (+, -, *, /): ")
    
    if operacao in ['+', '-', '*', '/']:
        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida!")
                resultado = num1 / num2
            
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break
            
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
            while True:
                try:
                    num2 = float(input("Digite um novo segundo número (diferente de zero): "))
                    if num2 != 0:
                        break
                    else:
                        print("Erro: O segundo número não pode ser zero para divisão!")
                except ValueError:
                    print("Erro: Digite um número válido!")
    else:
        print("Erro: Operação inválida! Use apenas +, -, * ou /")

def solicitar_numero(prompt):
    while True:
        try:
            valor = input(prompt)
            numero = float(valor)
            return numero
        except ValueError:
            print(f"Erro: '{valor}' não é um número válido. Tente novamente.")

def solicitar_operacao():
    operacoes_validas = ['+', '-', '*', '/']
    while True:
        op = input("Digite a operação (+, -, *, /): ").strip()
        if op in operacoes_validas:
            return op
        else:
            print(f"Erro: operação '{op}' inválida. Tente novamente.")

def calcular(num1, num2, operacao):
    try:
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            return num1 / num2
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        return None

def main():
    while True:
        num1 = solicitar_numero("Digite o primeiro número: ")
        num2 = solicitar_numero("Digite o segundo número: ")
        operacao = solicitar_operacao()

        resultado = calcular(num1, num2, operacao)
        if resultado is not None:
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break  # Sai do loop e encerra o programa

if __name__ == "__main__":
    main()

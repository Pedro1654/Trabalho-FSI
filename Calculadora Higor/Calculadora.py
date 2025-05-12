import math

def verificar_numero(numero):
    if math.isnan(numero):
        raise ValueError("Esse número não é aceito!")
    return numero

def verificar_operador(operador):
    operadores_validos = {'+', '-', '*', '/', '^'}
    if operador not in operadores_validos:
        raise ValueError(f"Operador '{operador}' inválido!")
    return operador

def calcular(x, y, op):
    verificar_numero(x)
    verificar_numero(y)
    verificar_operador(op)

    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            raise ZeroDivisionError("Ainda não é possível dividir por zero! :(")
        return x / y
    elif op == '^':
        return x ** y

def main():
    print("Calculadora!")

    try:
        x = float(input("\nDigite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print("\nEscolha a operação:")
        print("'+', '-', '*', '/', '^'")
        op = input("Digite a operação: ")

        resultado = calcular(x, y, op)
        print(f"\nResultado: ({x}) {op} ({y}) = {resultado}")

    except ValueError as ve:
        print(f"\nErro de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"\nErro de matemática: {zde}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main()

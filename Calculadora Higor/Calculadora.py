print ("Calculadora!")

x = float(input("\nDigite o primeiro número: "))
y = float(input("\nDigite o segundo número: "))

print("\nEscolha a operação: ")

print ("\n'+' Para soma.")
print ("\n'-' Para subtração.")
print ("\n'*' Para multiplicação.")
print ("\n'/' Para divisão.")
print ("\n'^' Para potenciação.")
op = input("\nDigite a operação: ")
match op:
    case '+':
        print(f"\nResultado: {x} + {y} = {x + y}")
    case '-':
        print(f"\nResultado: {x} - {y} = {x - y}")
    case '*':
        print(f"\nResultado: {x} * {y} = {x * y}")
    case '/':
        if y == 0:
            print("\nErro: Divisão por zero não é permitida.")
        else:
            print(f"\nResultado: {x} / {y} = {x / y}")
    case '^':
        print(f"\nResultado: {x} ^ {y} = {x ** y}")
    case _:
        print("\nOperação inválida.")
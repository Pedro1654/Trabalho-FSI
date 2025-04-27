def bissecao(f, a, b, tol=1e-6):
    
    max_iter = 100

    if a > b:
        a, b = b, a
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print("\nA função não muda de sinal no intervalo [a, b].")
        exit(1)
    
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        if fc == 0:
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        if (b - a) < tol:
            return (a + b) / 2
    
    return (a + b) / 2

def falsa_posicao(f, a, b, tol=1e-6):
    
    max_iter=100

    if a > b:
        a, b = b, a
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print("\nA função não muda de sinal no intervalo [a, b].")
        exit(1)
    
    for _ in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if fc == 0 or abs(fc) < tol:
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        if abs(b - a) < tol:
            return c
    
    return c

def newton(f, f_derivada, x0, tol=1e-6):
    
    max_iter=100

    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        
        dfx = f_derivada(x)
        if dfx == 0:
            print("\nDerivada igual a zero. O método não pode continuar.")
            exit(1)
        
        x_novo = x - fx / dfx
        
        if abs(x_novo - x) < tol:
            return x_novo
        
        x = x_novo
    
    return x

op = int(input("Escolha o problema desejado:\n1 - Problema 1\n2 - Problema 2\n3 - Problema 3\n4 - Problema 4\n--------->"))

while op < 1 or op > 4:
    op = int(input("Escolha o problema desejado:\n1 - Problema 1\n2 - Problema 2\n3 - Problema 3\n4 - Problema 4\n--------->"))
        

match op:
    case 1:
        def funcao(x):
            return 5 *x - 100
        
        def f_linha(x):
            return x
        
        met = int(input("Escolha o método desejado:\n1 - Bisseção\n2 - Falsa Posição\n3 - Método de Newton\n---------> "))

        
        while met < 1 or met > 3:
            met = int(input("Escolha o método desejado:\n1 - Bisseção\n2 - Falsa Posição\n3 - Método de Newton\n---------> "))
        
        match met:
            case 1:
                a = float(input("\nDigite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                
                raiz = bissecao(funcao, a, b, tol=1e-6)
                
                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")

            case 2:
                a = float(input("\nDigite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                
                raiz = falsa_posicao(funcao, a, b, tol=1e-6)

                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")
                
            case 3:
                X0 = float(input("\nDigite o valor de X0: "))
                
                raiz = newton(funcao, f_linha, X0, tol=1e-6)
                
                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")
                
    case 2:
        def funcao(x):
            Is = 1/(10**12)
            I = 0.01
            Vt = 0.025
            return Is*(2.71828**(x/Vt)-1) - I
        
        def f_linha(x):
            return x
        
        met = int(input("Escolha o método desejado:\n1 - Bisseção\n2 - Falsa Posição\n3 - Método de Newton\n---------> "))

        
        while met < 1 or met > 3:
            met = int(input("Escolha o método desejado:\n1 - Bisseção\n2 - Falsa Posição\n3 - Método de Newton\n---------> "))
        
        match met:
            case 1:
                a = float(input("\nDigite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                
                raiz = bissecao(funcao, a, b, tol=1e-6)
                
                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")

            case 2:
                a = float(input("\nDigite o valor de A: "))
                b = float(input("Digite o valor de B: "))
                
                raiz = falsa_posicao(funcao, a, b, tol=1e-6)

                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")
                
            case 3:
                X0 = float(input("\nDigite o valor de X0: "))
                
                raiz = newton(funcao, f_linha, X0, tol=1e-6)
                
                raiz = raiz + 0.00005
                
                print(f"\nA raiz encontrada é {raiz:.4f}")
                
        



def Numerico(x0, x1):
    def funcao(x):
        return 5 * x - 100
    
    f0 = funcao(x0)
    f1 = funcao(x1)
    
    if f0 * f1 >= 0:
        print("Erro: A função não tem sinais opostos em x0 e x1.")
        return None
    
    while True:
        Xi = (x0 + x1) / 2
        Fi = funcao(Xi)
        
        if abs(Fi) < 1e-6:  #Critério de parada
            return Xi
        
        elif f0 * Fi < 0:
            x0 = x0
            x1 = Xi
            f1 = Fi
            
        elif f0 * Fi > 0:
            x0 = Xi
            x1 = x1
            f0 = Fi     

p1 = float(input("Digite o valor de P1: "))
p2 = float(input("Digite o valor de P2: "))

k = Numerico(p1, p2)

print(f"A raiz eh: {k}")  # Saída: 5

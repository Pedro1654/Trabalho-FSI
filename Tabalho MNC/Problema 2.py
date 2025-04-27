def Numerico (a, b):
    def funcao(x):
        Is = 1/(10**12)
        I = 0.01
        Vt = 0.025
        return Is*(2.71828**(x/Vt)-1) - I
    
    fa = funcao(a)
    fb = funcao(b)
    
    if fa * fb >= 0:
        print("Erro: A função não tem sinais opostos em x0 e x1.")
        return None
    
    while True:
        Xi = (a * fb -  b * fa) / (fb - fa)
        
        #  5
        # / \
        #4   6
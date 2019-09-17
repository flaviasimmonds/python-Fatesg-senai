class Veiculo:
    def __init__(self):
        print('Veiculo criado')
        
    def getMotor(self):
        print('Tenho um motor')
        
class Caminhao(Veiculo):
    def __init__(self):
        super().__init__()
    
    def getMotor(self):
        print('Meu motor é diesel')
        
def fatorial(n):
    r = 1
    for i in range(1, n+1):
        r = r * i
    return r

def imprimir(r):
    print('=================')
    print(f'Resultado: {r}')
    

def escreve(func):
    def wrapper():
        print('-------')
        func()
        print('-------')
    return wrapper    

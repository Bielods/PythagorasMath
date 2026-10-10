def linha ():
    print("-"*40)

def titulo (texto):
    linha()
    print(texto.center(40))
    linha()

def linha ():
    print("-"*40)

def titulo (texto):
    linha()
    print(texto.center(40))
    linha()

def ler_numero(mensagem="Digite um número: "):
    while True:
        try:
            return float(input(mensagem))
        except:
            print("Valor inválido. Tente novamente")

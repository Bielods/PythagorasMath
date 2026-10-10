def linha ():
    print("-"*40)

def titulo (texto):
    linha()
    print(texto.center(40))
    linha()

def ler_numero():
    while True:
        try:
            valor= float(input("Digite o valor: "))
            return  valor
        except:
            print("Valor inválido. Tente novamente")
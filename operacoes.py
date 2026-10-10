from dados import OPERACOES, FIGURAS
from utils import titulo, ler_numero

def somar():
    n1= ler_numero()
    n2= ler_numero()
    soma= n1+n2
    print(f"O resultado da soma entre {n1} e {n2} é {soma}")

def subtrair():
    n1= ler_numero()
    n2= ler_numero()
    sub= n1-n2
    print(f"O resuldado da subtração entre {n1} e {n2} é {sub}")

def multiplicar():
    n1= ler_numero()
    n2= ler_numero()
    multi= n1*n2
    print(f"O resuldado da multiplicação entre {n1} e {n2} é {multi}")

def dividir():
    n1 = ler_numero()
    n2 = ler_numero()
    if n2 == 0:
        print("Não é possível dividir por zero")
    elif n1 % n2 == 0:
        resultado = int(n1 // n2)   
        print(f"O resultado da divisão entre {n1} e {n2} é {resultado} (divisão exata)")
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão entre {n1} e {n2} é {resultado:.2f} (com resto: {n1 % n2})")

def porcentagem():
    total = ler_numero()
    parte = ler_numero()
    porcem = (parte/100)*total
    print(f"{parte}% de {total} corresponde a {porcem}")

def equacao_primeiro_grau():
    a = ler_numero()
    b = ler_numero()
    if a == 0:
        print("Equação sem solução")
    else:
        x = -b / a
        print(f"O valor da incógnita é {x}")


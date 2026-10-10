from dados import OPERACOES, FIGURAS
from utils import titulo, ler_numero

def somar():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    soma= n1+n2
    print(f"O resultado da soma entre {n1} e {n2} é {soma}")

def subtrair():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    sub= n1-n2
    print(f"O resuldado da subtração entre {n1} e {n2} é {sub}")

def multiplicar():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    multi= n1*n2
    print(f"O resuldado da multiplicação entre {n1} e {n2} é {multi}")

def dividir():
    n1 = ler_numero("Digite o valor do dividendo: ")
    n2 = ler_numero("Digite o valor do divisor: ")
    if n2 == 0:
        print("Não é possível dividir por zero")
    elif n1 % n2 == 0:
        resultado = int(n1 // n2)   
        print(f"O resultado da divisão entre {n1} e {n2} é {resultado} (divisão exata)")
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão entre {n1} e {n2} é {resultado:.2f} (com resto: {n1 % n2})")

def porcentagem():
    total = ler_numero("Digite o valor base: ")
    parte = ler_numero("Digite o valor do percentual desejado: ")
    porcem = (parte/100)*total
    print(f"{parte}% de {total} corresponde a {porcem}")

def equacao_primeiro_grau():
    a = ler_numero("Digite o valor de a: ")
    b = ler_numero("Digite o valor de b: ")
    if a == 0:
        print("Equação sem solução")
    else:
        x = -b / a
        print(f"O valor da incógnita é {x}")

def equacao_segundo_grau():
    a= ler_numero("Digite o valor de a: ")
    b= ler_numero("Digite o valor de b: ")
    c= ler_numero("Digite o valor de c: ")
    delta= b**2-4*a*c
    if delta <0:
        print("Equação sem solução real")
    elif delta == 0:
        x= -b / (2*a)
        print(f"O valor da incógnita é {x}")
    else:
        x1= (-b + delta**0.5) / (2*a)
        x2= (-b - delta**0.5) / (2*a)
        print(f"O valor das incógnitas é x1= {x1} e x2= {x2}")

def baskhara():
    a= ler_numero("Digite o valor de a: ")
    b= ler_numero("Digite o valor de b: ")
    c= ler_numero("Digite o valor de c: ")
    delta= b**2-4*a*c
    print(f"O valor de delta é {delta}")
    if delta <0:
        print("Sem raízes reais")
    elif delta == 0:
        x= -b / (2*a)
        print(f"O valor da raiz é {x}")
    else:
        x1= (-b + delta**0.5) / (2*a)
        x2= (-b - delta**0.5) / (2*a)
        print(f"O valor das duas raízes é x1= {x1} e x2= {x2}")

def regra_de_tres():
    a= ler_numero("Digite o primeiro valor: ")
    b= ler_numero("Digite o segundo valor: ")
    c= ler_numero("Digite o terceiro valor: ")
    x= (b * c) / a
    print(f"O quarto valor é {x}")

def potenciacao():
    base= ler_numero("Digite o valor da base: ")
    expoente= ler_numero("Digite o valor do expoente: ")
    poten= base ** expoente
    print(f"O resultado da potenciação é {poten}")

def radiacacao():
    n= ler_numero("Digite o valor da base: ")
    ind= ler_numero("Digite o valor do índice: ")
    if n < 0 and ind % 2 == 0:
        print("Sem solução real para raiz par de número negativo")
    else:
        raiz= n**(1 / ind)
        print(f"A raiz {ind} de {n} é {raiz}")

def teorema_pitagoras():
    opcao= input("Deseja calcular hipotenusa ou cateto?").strip().lower()
    if opcao == 'hipotenusa':
        cateto1= ler_numero("Digite o valor do primeiro cateto: ")
        cateto2= ler_numero("Digite o valor do segundo cateto: ")
        h= (cateto1**2 + cateto2**2) ** 0.5
        print(f"A hipotenusa vale {h}")
    elif opcao == 'cateto':
        hipotenusa= ler_numero("Digite o valor da hipotenusa")
        cateto_descoberto= ler_numero("Digite o valor do cateto conhecido")
        c= (hipotenusa**2 - cateto_descoberto**2) **0.5
        print(f"O outro cateto vale {c}")
    else:
        print("Escolha entre hipotenusa e cateto")

def media_moda_mediana():
    lista= input("Digite os números separados por espaços: ")
    numeros= [float(x) for x in lista.split()]
    media= sum(numeros)/ len(numeros)
    ordenados= sorted(numeros)
    meio= len(ordenados) // 2
    mediana= ordenados[meio]
    moda= max(numeros, key=numeros.count)
    print(f"A média de todos os números é {media}. A moda dos números é {moda}. E a mediana dos números é {mediana}")

def juros_simples():
    c= ler_numero("Digite o capital inicial: ")
    i= ler_numero("Digite o valor da taxa de juros: ")
    t= ler_numero("Digite o tempo: ")
    juros= c * (i/100) * t
    montante= c + juros
    print(f"O valor dos juros resultara em {juros} e o montante ficará em {montante}")

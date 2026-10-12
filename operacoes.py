from dados import OPERACOES, FIGURAS
from utils import titulo, ler_numero

def somar():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    soma= n1+n2
    print(f"O resultado da soma entre {n1} e {n2} é [{soma}]")

def subtrair():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    sub= n1-n2
    print(f"O resuldado da subtração entre {n1} e {n2} é [{sub}]")

def multiplicar():
    n1= ler_numero("Digite o primeiro valor: ")
    n2= ler_numero("Digite o segundo valor: ")
    multi= n1*n2
    print(f"O resuldado da multiplicação entre {n1} e {n2} é [{multi}]")

def dividir():
    n1 = ler_numero("Digite o valor do dividendo: ")
    n2 = ler_numero("Digite o valor do divisor: ")
    if n2 == 0:
        print("Não é possível dividir por zero")
    elif n1 % n2 == 0:
        resultado = int(n1 // n2)   
        print(f"O resultado da divisão entre {n1} e {n2} é [{resultado}] (divisão exata)")
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão entre {n1} e {n2} é [{resultado:.2f}] (com resto: {n1 % n2})")

def porcentagem():
    total = ler_numero("Digite o valor base: ")
    parte = ler_numero("Digite o valor do percentual desejado: ")
    porcem = (parte/100)*total
    print(f"{parte}% de {total} corresponde a [{porcem}]")

def equacao_primeiro_grau():
    a = ler_numero("Digite o valor de a: ")
    b = ler_numero("Digite o valor de b: ")
    if a == 0:
        print("Equação sem solução")
    else:
        x = -b / a
        print(f"O valor da incógnita é [{x}]")

def equacao_segundo_grau():
    a= ler_numero("Digite o valor de a: ")
    b= ler_numero("Digite o valor de b: ")
    c= ler_numero("Digite o valor de c: ")
    delta= b**2-4*a*c
    if delta <0:
        print("Equação sem solução real")
    elif delta == 0:
        x= -b / (2*a)
        print(f"O valor da incógnita é [{x}]")
    else:
        x1= (-b + delta**0.5) / (2*a)
        x2= (-b - delta**0.5) / (2*a)
        print(f"O valor das incógnitas é x1= [{x1}] e x2= [{x2}]")

def baskhara():
    a= ler_numero("Digite o valor de a: ")
    b= ler_numero("Digite o valor de b: ")
    c= ler_numero("Digite o valor de c: ")
    delta= b**2-4*a*c
    print(f"O valor de delta é [{delta}]")
    if delta <0:
        print("Sem raízes reais")
    elif delta == 0:
        x= -b / (2*a)
        print(f"O valor da raiz é [{x}]")
    else:
        x1= (-b + delta**0.5) / (2*a)
        x2= (-b - delta**0.5) / (2*a)
        print(f"O valor das duas raízes é x1= [{x1}] e x2= [{x2}]")

def regra_de_tres():
    a= ler_numero("Digite o primeiro valor: ")
    b= ler_numero("Digite o segundo valor: ")
    c= ler_numero("Digite o terceiro valor: ")
    x= (b * c) / a
    print(f"O quarto valor é [{x}]")

def potenciacao():
    base= ler_numero("Digite o valor da base: ")
    expoente= ler_numero("Digite o valor do expoente: ")
    poten= base ** expoente
    print(f"O resultado da potenciação é [{poten}]")

def radiacacao():
    n= ler_numero("Digite o valor da base: ")
    ind= ler_numero("Digite o valor do índice: ")
    if n < 0 and ind % 2 == 0:
        print("Sem solução real para raiz par de número negativo")
    else:
        raiz= n**(1 / ind)
        print(f"A raiz {ind} de {n} é [{raiz}]")

def teorema_pitagoras():
    opcao= input("Deseja calcular hipotenusa ou cateto? ").strip().lower()
    if opcao == 'hipotenusa':
        cateto1= ler_numero("Digite o valor do primeiro cateto: ")
        cateto2= ler_numero("Digite o valor do segundo cateto: ")
        h= (cateto1**2 + cateto2**2) ** 0.5
        print(f"A hipotenusa vale [{h}]")
    elif opcao == 'cateto':
        hipotenusa= ler_numero("Digite o valor da hipotenusa")
        cateto_descoberto= ler_numero("Digite o valor do cateto conhecido")
        c= (hipotenusa**2 - cateto_descoberto**2) **0.5
        print(f"O outro cateto vale [{c}]")
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
    print(f"A média de todos os números é [{media}]. A moda dos números é [{moda}]. E a mediana dos números é [{mediana}]")

def juros_simples():
    c= ler_numero("Digite o capital inicial: ")
    i= ler_numero("Digite o valor da taxa de juros: ")
    t= ler_numero("Digite o tempo: ")
    juros= c * (i/100) * t
    montante= c + juros
    print(f"O valor dos juros resultara em [{juros}] e o montante ficará em [{montante}]")

def juros_compostos():
     c= ler_numero("Digite o capital inicial: ")
     i= ler_numero("Digite o valor da taxa de juros: ")
     t= ler_numero("Digite o tempo: ")
     montante= c * (1 + i / 100) ** t
     juros= montante - c
     print(f"O valor dos juros resultara em [{juros}] e o montante ficará em [{montante}]")

def probabilidade():
    fav= ler_numero("Digite o número de casos favoráveis: ")
    pos= ler_numero("Digite o número de casos possíveis: ")
    if pos == 0:
        print("O número de possíveis não pode ser 0")
    else:
        prob= fav / pos
        print(f"A probabilidade de {fav} casos favoráveis em {pos} possíveis é [{prob*100:.2f}%]")

def expressao_numerica():
    expressao = input("Digite a expressão numérica completa: ")
    try:
        resultado = eval(expressao)
        print(f"O resultado da expressão é [{resultado}]")
    except:
        print("Expressão inválida")

def fracao():
    numerador= ler_numero("Digite o numerador: ")
    denominador= ler_numero("Digite o denominador: ")
    if denominador == 0:
        print("O denominador não pode ser 0")
    else:
        result= numerador/denominador
        print(f"A fração {numerador} sobre {denominador} equivale a [{result:.2f}]")

def area():
    figura= input("Qual figura você quer calcular a área?").strip().lower()
    if figura == 'quadrado':
        lado= ler_numero("Digite o valor do lado: ")
        area_q= lado*lado
        print(f"A área do quadrado é [{area_q}]")
    elif figura == 'retangulo' or figura == 'retângulo':
        base= ler_numero("Digite o valor da base: ")
        altura= ler_numero("Digite o valor da altura")
        area_r= base*altura
        print(f"A área do retângulo é [{area_r}]")
    elif figura == 'triangulo' or figura == 'triângulo':
        base= ler_numero("Digite o valor da base: ")
        altura= ler_numero("Digite o valor da altura: ")
        area_t= (base * altura) / 2
        print(f"A área do triângulo é [{area_t}]")
    elif figura == 'circulo' or figura == 'círculo':
        pi= 3.14
        raio= ler_numero("Digite o valor do raio: ")
        area_c= pi * raio **2
        print(f"A área do círculo é [{area_c}]")
    else:
        print("Resposta inválida")

def perimetro():
    figura= input("Qual figura você deseja saber o perímetro?").strip().lower()
    if figura == 'quadrado':
        lado= ler_numero("Digite o valor do lado: ")
        perimetro_q= 4 * lado
        print(f"O perímetro do quadrado é [{perimetro_q}]")
    elif figura == 'retangulo' or figura == 'retângulo':
        base= ler_numero("Digite o valor da base: ")
        altura= ler_numero("Digite o valor da altura: ")
        perimetro_r= 2 * (base + altura)
        print(f"O perímetro do retângulo é [{perimetro_r}]")
    elif figura == 'triangulo' or figura == 'triângulo':
        lado1= ler_numero("Digite o valor do primeiro lado: ")
        lado2= ler_numero("Digite o valor do segundo lado: ")
        lado3= ler_numero("Digite o valor do terceiro lado: ")
        perimetro_t= lado1 + lado2 + lado3
        print(f"O perímetro do triângulo é [{perimetro_t}]")
    elif figura == 'circulo' or figura == 'círculo':
        pi= 3.14
        raio= ler_numero("Digite o valor do raio: ")
        perimetro_c= 2 * pi * raio
        print(f"O perímetro do círculo é [{perimetro_c}]")
    else:
        print("Resposta inválida")

def sistema_equacoes():
    a1= ler_numero("Digite o valor de a1: ")
    b1= ler_numero("Digite o valor de b1: ")
    c1= ler_numero("Digite o valor de c1: ")
    a2= ler_numero("Digite o valor de a2: ")
    b2= ler_numero("Digite o valor de b2: ")
    c2= ler_numero("Digite o valor de c2: ")
    denominador= a1 * b2 - a2 * b1
    if denominador == 0:
        print("Sistema sem solução única")
    else:
        x= (c1 * b2 - c2*b1) / denominador
        y= (a1 * c2 - a2 * c1) / denominador
        print(f"O valor de x vale [{x}] e o valor de y vale [{y}]")

def parabola():
    a= ler_numero("Digite o coeficiente de a: ")
    b= ler_numero("Digite o coeficiente de b: ")
    c= ler_numero("Digite o coeficiente de c: ")
    delta= b**2-4*a*c
    x= -b / (2 * a)
    y= -delta / (4*a)
    if a>0:
        direcao= 'cima'
    else:
        direcao= 'baixo'
    print(f"Os valores dos vértices são [{x}] e [{y}] e a direção da parabola é [{direcao}]")

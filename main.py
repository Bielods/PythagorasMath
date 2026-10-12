from operacoes import somar, subtrair, multiplicar, dividir, porcentagem, equacao_primeiro_grau, equacao_segundo_grau, baskhara, regra_de_tres, potenciacao, radiacacao, teorema_pitagoras, media_moda_mediana, juros_simples, juros_compostos, probabilidade, expressao_numerica, fracao, area, perimetro, sistema_equacoes, parabola
from utils import titulo

def menu_operacoes():
    while True:
        titulo("Operações Básicas")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Expressão Numérica")
        print("6. Fração")
        print("7. Potenciação")
        print("8. Radiciação")
        print("9. Porcentagem") 
        print("10. Regra de Três")
        print("0. Voltar ao menu anterior")
        opcao= input("Escolha uma operação: ")
        if opcao == '1':
            somar()
        elif opcao == '2':
            subtrair()
        elif opcao == '3':
            multiplicar()
        elif opcao == '4':
            dividir()
        elif opcao == '5':
            expressao_numerica()
        elif opcao == '6':
            fracao()
        elif opcao == '7':
            potenciacao()
        elif opcao == '8':
            radiacacao()
        elif opcao == '9':
            porcentagem()
        elif opcao == '10':
            regra_de_tres()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, digite apenas o número referente a opção")    

def menu_algebra():
    while True:
        titulo("Álgebra")
        print("1. Equação 1º grau")
        print("2 Equação 2º grau")
        print("3. Bhakara")
        print("4. Parábola")
        print("5. Sistema de Equações")
        print("0. Voltar ao menu anterior")
        opcao= input("Escolha uma categoria: ")
        if opcao == '1':
            equacao_primeiro_grau()
        elif opcao == '2':
            equacao_segundo_grau()
        elif opcao == '3':
            baskhara()
        elif opcao == '4':
            parabola()
        elif opcao == '5':
            sistema_equacoes()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, digite apenas o número referente a opção")  

def menu_geometria():
    while True:
        titulo("Geometria")
        print("1. Área")
        print("2. Perímetro")
        print("3. Teorema de Pitágoras")
        print("0. Voltar ao menu anterior")
        opcao= input("Escolha uma categoria: ")
        if opcao == '1':
            area()
        elif opcao == '2':
            perimetro()
        elif opcao == '3':
            teorema_pitagoras()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, digite apenas o número referente a opção")  

def menu_estatisticas():
    while True:
        titulo("Estatísticas")
        print("1. Média, Moda e Mediana")
        print("2. Probabilidade")
        print("0. Voltar ao menu anterior")
        opcao= input("Escolha uma categoria: ")
        if opcao == '1':
            media_moda_mediana()
        elif opcao == '2':
            probabilidade()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, digite apenas o número referente a opção")  

def menu_financas():
    while True:
        titulo("Finanças")
        print("1. Juros Simples")
        print("2. Juros Compostos")
        print("0. Voltar ao menu anterior")
        opcao= input("Escolha uma categoria: ")
        if opcao == '1':
            juros_simples()
        elif opcao == '2':
            juros_compostos()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, digite apenas o número referente a opção")  
while True:
    titulo("PythagorasMath")
    print("1. Operações Básicas")
    print("2. Álgebra")
    print("3. Geometria")
    print("4. Estatística")
    print("5. Finanças")
    print("0. Sair")
    opcao= input("Escolha uma categoria: ")
    if opcao == '1':
        menu_operacoes()
    elif opcao == '2':
        menu_algebra()
    elif opcao == '3':
        menu_geometria()
    elif opcao == '4':
        menu_estatisticas()
    elif opcao == '5':
        menu_financas()
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida, digite apenas o número referente a opção")  




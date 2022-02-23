stop = False
option = int(input('''Bem-Vindo a sua calculadora de bordo, escolha a operação desejada:
(1) - Soma
(2) - Subtração
(3) - Multiplicação
(4) - Divisão       

Para cancelar a operação digite 'STOP'.                                                  
'''))

numbers = []
result = 0
operation = ""

while not stop:
    number = float(input('Digite um número para realizar a operação: '))
    numbers.append(number)
    finalize = input('Ótimo, número anotado. Deseja digitar mais números (Sim/Nao)? ').lower()
    if finalize == "nao":
        stop = True
        if option == 1:
            for x in numbers:
                result += x
                operation += " " + str(x) + " +"
        elif option == 2:
            for x in numbers:
                result -= x
                operation += " " + str(x) + " -"
        elif option == 3:
            result = 1
            for x in numbers:
                result = (result * x)
                operation += " " + str(x) + " *"
        elif option == 4:
            for x in numbers:
                result = 1
                result = (result / x)
                operation += " " + str(x) + " /"
        print("Legal! O resultado de{} é: {}".format(operation, result))



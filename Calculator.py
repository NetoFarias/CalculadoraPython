def Calculadora():
    numeros = []
    operacoes = []
    historico = []
    numero = float(input("Digite o primeiro número: "))
    numeros.append(numero)
    while True:
        operador = input("Diga a operação desejada (+, -, *, /) Digite = para calcular: ")
        if operador not in ["+", "-", "*", "/", "="]:
            print("Operador inválido. Digite novamente.")
            continue

        if operador == "=":
            break

        operacoes.append(operador)
        numero = float(input("Digite o próximo número: "))
        numeros.append(numero)
        historico.append(f"{numeros[-2]} {operador} {numero}")

    resultado = numeros[0]
    for i in range(len(operacoes)):
        operacao = operacoes[i]
        numero = numeros[i + 1]

        if operacao == "+":
            resultado += numero
        elif operacao == "-":
            resultado -= numero
        elif operacao == "*":
            resultado *= numero
        elif operacao == "/":
            if numero == 0:
                print("Não é possível dividir por 0")
                Calculadora()
                return

            resultado /= numero
    print(resultado)
    print("Historico completo:")
    for operacao in historico:
        print("{} = {}".format(operacao, resultado))


def Novamente():
    retry = input("Deseja continuar? (Y/N): ").lower()
    if retry == "y":
        Calculadora()
        return
    elif retry == "n":
        print("Até a proxima")
    else:
        print("Entrada inválida. Digite corretamente. ".lower())
        Novamente()


if __name__ == "__main__":
    print("Bem vindo à Calculadora Farias.")
    Calculadora()
    Novamente()



cpf = []
dados = {}
listaContendoOsDicionario = list()
resposta = str('S')
qtdInvalido = int(0)
qtdValido = int(0)
while resposta == 'S':
    print('-'*50)
    cpfDigitado = input('Digite o seu cpf: ')
    while len(cpfDigitado) > 11 or len(cpfDigitado) < 11:
        cpfDigitado = input('Cpf inválido, digite o cpf novamente: ')
    cpfPrimeiraLista = []
    contadorAux = []
    contador = int(10)
    for i, c in enumerate(cpfDigitado):
        if i <= 8:
            cpfPrimeiraLista.append([c])
            contadorAux.append([contador])
        contador -= 1
    somaDigitosCpf = int(0)
    digitoGerado1 = int(0)
    for x in range(0, 9):
        somaDigitosCpf = somaDigitosCpf + (int(cpfPrimeiraLista[x][0]) * contadorAux[x][0])
    digitoGerado1 = int(0)
    restoDivisaoDigito = somaDigitosCpf % 11
    if restoDivisaoDigito < 2:
        digitoGerado1 = 0
    else:
        digitoGerado1 = 11 - restoDivisaoDigito
    novaPrimeirasListaCpf = []
    novoContadorAux = []
    contador2 = int(11)
    for i, c in enumerate(cpfDigitado):
        if i <= 8:
            novaPrimeirasListaCpf.append([c])
            novoContadorAux.append([contador2])
        else:
            novoContadorAux.append([contador2])
            novaPrimeirasListaCpf.append([digitoGerado1])
        contador2 = contador2 - 1
    novoSomaDigitosCpf = int(0)
    for x in range(0, 10):
        novoSomaDigitosCpf = novoSomaDigitosCpf + (int(novaPrimeirasListaCpf[x][0]) * novoContadorAux[x][0])
        digitoGerado2 = int(0)
    restoDivisaoDigito2 = novoSomaDigitosCpf % 11
    if restoDivisaoDigito2 % 11 < 2:
        digitoGerado2 = 0
    else:
        digitoGerado2 = 11 - restoDivisaoDigito2
    validacao = str()
    if int(digitoGerado1) == int(cpfDigitado[-2]) and int(digitoGerado2) == int(cpfDigitado[-1]):
        validacao = "VÁLIDO"
        qtdValido += 1
    else:
        qtdInvalido += 1
        validacao = "INVÁLIDO"
    dados = {'cpf': cpfDigitado, 'VALIDACAO': validacao}
    listaContendoOsDicionario.append(dados)
    resposta = input('\nDeseja continuar o programa (S - sim/N - não): ')
    while resposta != 'S' and resposta != 'N':
        resposta = input('\nResposta inválida, digite somente (S - sim/N - não): ')
porcValido = qtdValido / len(listaContendoOsDicionario) * 100
porInvalido = qtdInvalido / len(listaContendoOsDicionario) * 100
print('='*50)
print(f"A quantidade de cpf's testados é igual a: {len(listaContendoOsDicionario)}")
print(f"A quantidade de cpf's válidos é igual a: {qtdValido}")
print(f"A quantidade de cpf's inválidos é igual a: {qtdInvalido}")
print(f"A porcentagem de cpf's válidos em relação ao total de testes realizados é igual a: {porcValido:.2f}%")
print(f"A porcentagem de cpf's inválidos em relação ao total de testes realizados é igual a: {porInvalido:.2f}%")

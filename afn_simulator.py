import sys


# identifica as caracteristicas do afn com base formato de arquivo
# recebe como parametro um arquivo
# retorna um dicioanrio que representa um afn
def read_afn(arq):
    alfabeto = []
    estados = []
    inicial = []
    finais = []
    transicoes = []
    tran = False

    for line in arq:
        line = line.replace(" ", "")
        line = line.replace("\n", "")

        if line.startswith('alfabeto='):
            equal = line.find("=")
            alfabeto = line[equal + 1:]
            if len(alfabeto) == 0:
                raise ValueError('A entrada não possui alfabeto')
            alfabeto = alfabeto.split(',')

        elif line.startswith('estados='):
            equal = line.find("=")
            estados = line[equal + 1:]
            if len(estados) == 0:
                raise ValueError('A entrada não possui estados')
            estados = estados.split(',')

        elif line.startswith('inicial='):
            equal = line.find("=")
            inicial = line[equal + 1:]
            if len(inicial) == 0:
                raise ValueError('A entrada não possui estado inicial')

        elif line.startswith('finais='):
            equal = line.find("=")
            finais = line[equal + 1:]
            finais = finais.split(',')

        elif line == 'transicoes':
            tran = True

        elif tran:
            aux = line.split(',')
            if len(aux) != 3:
                raise ValueError(f'A transicao {line} não está adequada')
            elif aux[0] not in estados or aux[1] not in estados:
                raise ValueError(f'A transição {line} possui um estado que não foi informado')
            elif aux[2] not in alfabeto and aux[2] != 'epsilon':
                raise ValueError(f'A transição {line} não está no alfabeto informado')
            transicoes.append(aux)

        else:
            raise ValueError('A entrada não se adequa ao formato')

    afn = {
        'alfabeto': alfabeto,
        'estados': estados,
        'inicial': inicial,
        'finais': finais,
        'transicoes': transicoes,
    }

    return afn


# retorna True se tem transicao com cadeia vazia para o estado atual
# False caso contrario
def verifica_vazia(afn, estado_atual):
    for transicao in afn['transicoes']:
        if transicao[0] == estado_atual and transicao[2] == "epsilon":
            return True
    return False


# funcao feita para caso a cadeia tenha acabado
# se houver transicoes de cadeia vazia ela vai indicar o processamento
def processa_vazia(afn, estado_atual, resultado):
    for transicao in afn['transicoes']:
        if transicao[0] == estado_atual and transicao[2] == "epsilon":
            processa_cadeia(afn, '', transicao[1], resultado)


# essa função realiza o processamento da cadeia de forma recursiva
# recebe como parametro o dicionario que representa o afn
# recebe a cadeia que deseja ser processada
# recebe o estado que o automato se encontra
# como parametro adicional recebe o que ja foi processado
# ao final imprime o resultado de todas as possibilidades
def processa_cadeia(afn, cadeia, estado_atual, resultado=''):
    cadeia_vazia = False
    if cadeia == '':
        if verifica_vazia(afn, estado_atual):
            processa_vazia(afn, estado_atual, resultado)
        if estado_atual in afn['finais']:
            resultado += estado_atual + " V"
            print(resultado)
        else:
            resultado += estado_atual + " X"
            print(resultado)
    else:
        count = 0
        for transicao in afn['transicoes']:
            if transicao[0] == estado_atual and (transicao[2] == cadeia[0] or transicao[2] == "epsilon"):
                count += 1
                if count == 1:
                    resultado += estado_atual + ' '
                if transicao[2] == "epsilon":
                    old = estado_atual + ' '
                    s = ''
                    cadeia_vazia = True
                    count -= 1
                    processa_cadeia(afn, cadeia, transicao[1], s.join(resultado.rsplit(old, 1)))
                elif len(cadeia) <= 1:
                    processa_cadeia(afn, '', transicao[1], resultado)
                else:
                    processa_cadeia(afn, cadeia[1:], transicao[1], resultado)
        if count == 0:
            if cadeia_vazia:
                print(resultado + "X")
            else:
                resultado += estado_atual + " X"
                print(resultado)


# main
if __name__ == '__main__':

    fname = input("Digite o nome do arquivo: ")

    try:
        text = open(fname, "r")
    except OSError:
        print(f"Não foi possível ler o arquivo: {fname}")
        sys.exit()
    afn = read_afn(text)
    cadeia = input(f'Digite a cadeia que deseja processar: ')
    for letra in cadeia:
        if letra not in afn['alfabeto']:
            print(f'\n\n{letra} não pertence ao alfabeto do AFN')
            sys.exit()
        print(f" {letra}", end=" ")
    print(' λ')
    processa_cadeia(afn, cadeia, afn['inicial'])
    text.close()

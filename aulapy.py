# def conta_letras(palavra):
#     conta={}
#     for letra in palavra:
#         if letra  not in conta.keys():
#             conta[letra] = 1
#         else:
#             conta[letra] = conta[letra] + 1
#         #aumenta o valor associado a
#         #chave letra
#     return conta

# conta_letras('banana')

def contra_letras(palavra):
    conta = {}
    for letra in palavra:
        conta[letra] = conta.get(letra, 0) + 1
    return conta

contra_letras('banana')
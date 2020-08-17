import sys

ALFA='abcdefghijklmnopqrstuvwxyz'
ROT=13

def cifra(mensagem, dir):
    m=''
    for x in mensagem:
        if x in ALFA: # condicional para tratar caracteres que nao estejam dentro de ALFA
            x_index = ALFA.index(x) # encontra o indice do caracter dentro de ALFA
            m += ALFA[(x_index + (dir * ROT)) % len(ALFA)] # soma do indice + rotacao (multiplica por 1 ou -1) % tamanho de ALFA
        else:
            m += x # condicional para tratar caracteres que nao estejam dentro de ALFA
    return m

def decifrar(mensagem):
    return cifra(mensagem, -1)
def cifrar(mensagem):
    return cifra(mensagem, 1)

def main():
    # 2 argumentos para processar por linha de comando
    comando = sys.argv[1].lower() 
    mensagem = sys.argv[2].lower()

    if comando == 'decifrar':
        print (decifrar(mensagem)) # funcao decifrar com dir -1
    elif comando == 'cifrar':
        print (cifrar(mensagem)) # funcao cifrar com dir 1
    else:
        print (comando +' -> comando nao encontrado')

main()
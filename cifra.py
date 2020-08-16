import sys

ALFA='abcdefghijklmnopqrstuvwxyz'
ROT=3

def cifra(mensagem, dir):
    m=''
    for x in mensagem:
        if x in ALFA:
            x_index = ALFA.index(x)
            m += ALFA[(x_index + (dir * ROT)) % len(ALFA)]
        else:
            m += x
    return m

def decifrar(mensagem):
    return cifra(mensagem, -1)
def cifrar(mensagem):
    return cifra(mensagem, 1)

def main():
    comando = sys.argv[1].lower()
    mensagem = sys.argv[2].lower()

    if comando == 'decifrar':
        print (decifrar(mensagem))
    elif comando == 'cifrar':
        print (cifrar(mensagem))
    else:
        print (comando +' -> comando nao encontrado')

main()
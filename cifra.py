import sys

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'decifrar':
        print ('decifrar')
    elif command == 'cifrar':
        print ('cifrar')
    else:
        print (command +' -> comando nao encontrado')


main()
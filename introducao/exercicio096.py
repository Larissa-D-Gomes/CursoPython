"""
Fazer um programa com método recursivo para ler uma cadeia de caracteres e
para mostrar cada símbolo separadamente, um por linha.
"""

def mostrarChar(leitura, n, index):
    if index < n:
        print(leitura[index])
        mostrarChar(leitura, n, index+1)

def main():
    leitura = input('Digite uma cadeia de caracteres: ')
    mostrarChar(leitura, len(leitura), 0)

if __name__ == '__main__':
    main()

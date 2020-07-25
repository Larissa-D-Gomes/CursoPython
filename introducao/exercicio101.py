"""
Implemente uma funcao que recebe uma string como parâmetro e retorna true
se essa é um palíndromo.
"""

def verificadorPalindromo(leitura):
    aux = leitura[::-1]
    return aux.lower() == leitura.lower()

def main():
    leitura = input('Digite a string: ')

    print('Eh palindromo?',verificadorPalindromo(leitura))


if __name__ == '__main__':
    main()

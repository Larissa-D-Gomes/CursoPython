"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""






def main():
    leitura = input('Digite o dado: ')
    print('Tipo primitivo',type(leitura))
    print('Eh um numero?', leitura.isnumeric())
    print('Apenas letras?', leitura.isalpha())
    print('Apenas letras maiusculas?', leitura.isupper())
    print('Apenas letras minusculas?', leitura.islower())



if __name__ == '__main__':
    main()

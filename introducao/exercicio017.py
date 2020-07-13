"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""






def main():
    cateto_op = input('Digite o cateto oposto: ')
    cateto_op = cateto_op.replace(",", ".")

    cateto_adj = input('Digite o cateto adjacente: ')
    cateto_adj = cateto_adj.replace(",", ".")

    try:
        print(f'O comprimento da hipotenusa eh: {cateto_op}^2 +'
              f' {cateto_adj}^2 = {((float(cateto_op)**2) + (float(cateto_adj)**2))**(1/2)} ')
    except ValueError:
        print('Dado(s) invalido(s).')

if __name__ == '__main__':
    main()

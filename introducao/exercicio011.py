"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""






def main():
    pass
    altura = input('Digite a altura da parede: ')
    altura = altura.replace(",",".")

    largura = input('Digite a largura da parede: ')
    laragura = largura.replace(",",".")
    try:
        area = float(altura)*float(largura)
        print(f'Area = {area} m^2\nQuantidade de tinta: {area/2} l')
    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()

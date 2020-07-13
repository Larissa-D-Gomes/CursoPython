"""
EXERCÍCIO 043: Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

def main():

    try:
        peso = float(input('Digite o seu peso: ').replace(',', '.'))
        altura = float(input('Digite a sua altura: ').replace(',', '.'))

        if peso > 0.0 and altura > 0.0:
            imc = peso / altura**2

            if imc < 18.5:
                print(f'IMC = {imc}: Abaixo do Peso')
            elif imc < 25:
                print(f'IMC = {imc}: Peso Ideal.')
            elif imc < 30:
                print(f'IMC = {imc}: Sobrepeso.')
            elif imc < 40:
                print(f'IMC = {imc}: Obesidade Morbida.')
            else:
                print(f'IMC = {imc}: Sobrepeso.')

        else:
            raise ValueError
    except ValueError:
        print('Dado invalido')


if __name__ == '__main__':
    main()

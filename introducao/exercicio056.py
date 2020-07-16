"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

from pessoa import Pessoa

def main():
    mais_velho = None
    menos_vinte = 0
    soma_idades = 0
    pessoas = []

    for x in range(4):
        try:
            nome = input(f'Digite o nome da pessoa {x+1}: ')
            idade = input(f'Digite a idade da pessoa {x+1}: ')
            sexo = input(f'Digite o sexo da pessoa {x+1} [F/M]: ').upper()

            pessoas.append(Pessoa(nome, idade, sexo))
            if pessoas[x].getSexo() == 'M' and mais_velho == None:
                mais_velho = pessoas[x]

            elif pessoas[x].getSexo() == 'M' and mais_velho.getIdade() < pessoas[x].getIdade():
                mais_velho = pessoas[x]
            elif pessoas[x].getIdade() < 20:
                menos_vinte += 1

            soma_idades += pessoas[x].getIdade()
        except ValueError:
            print('Dado invalido.')

    print(f'A media das idades eh: {soma_idades/4} '
          f'\nO homem mais velho eh: {mais_velho.getNome()}'
          f'\nA quantidade de mulheres com menos de 20 anos eh: {menos_vinte}')

if __name__ == '__main__':
    main()

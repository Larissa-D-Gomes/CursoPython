"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

from pessoa import Pessoa

def main():
    pessoas = []

    for x in range(4):
        nome = input(f'Digite o nome da pessoa {x+1}: ')
        idade = input(f'Digite a idade da pessoa {x+1}: ')
        sexo = input(f'Digite o sexo da pessoa {x+1} [F/M]: ')
        pessoas.append(Pessoa(nome, idade, sexo.upper()))
        print(pessoas[x])

if __name__ == '__main__':
    main()

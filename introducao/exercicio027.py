"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

def main():
    nome = input('Digite o nome completo: ')
    nomes = nome.split(' ')

    print(f'Primeiro = {nomes[0]} \nUltimo = {nomes[len(nomes)-1]}')


if __name__ == '__main__':
    main()

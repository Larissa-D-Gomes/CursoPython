"""
Fazer um programa para ler o email do usuário (string)
Separar o nome do domínio.

EXEMPLO:

email = teste@pucminas.br
nome = teste
dominio = pucminas.br
"""


def main():
    leitura = input('Digite o endereco de email: ')
    try:
        aux = leitura.split('@')
        if len(aux) != 2:
            raise ValueError
        print(f'EMAIL: {leitura} \nNome: {aux[0]} '
              f'\nDominio: {aux[1]}')
    except ValueError:
        print('Endereco invalido.')
if __name__ == '__main__':
    main()

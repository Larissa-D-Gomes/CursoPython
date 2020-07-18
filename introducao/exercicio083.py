"""
EXERCÍCIO 083: Validando Expressões Matemáticas

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
"""


def main():
    expressao = input('Digite a expressao: ')
    erro = False
    l = len(expressao) - 1
    p = []
    while l >= 0 and not erro:
        if expressao[l] == ')':
            p.append(')')
        elif expressao[l] == '(' and len(p) > 0:
            p.pop()
        else:
            erro = True
        l-=1
    if len(p) > 0 or erro:
        print('Expressao errada.')
    else:
        print('Expressao correta.')


if __name__ == '__main__':
    main()

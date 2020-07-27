"""
A secretária, Carol, do curso de Ciência da Computação, deseja enviar uma mensagem de Feliz
Aniverśario a alguns os professores do departamento, que coincidentemente, fazem aniversário no mesmo dia.

São incluídos, também, professores dos cursos de sistemas de informação e de jogos.

A mensagem possui a seguinte estrutura:

    Bom dia, <nome_do_professor>!

    Gostaria de dar os meus parabéns a você. É um prazer enorme fazer parte
    dessa equipe de profissionais da PUC. Desejo-te muita saúde, paz e dinheiro!

    Atenciosamente, Carol.


A única coisa que ela possui é um arquivo "cadastro_professores.txt".
Infelizmente, os nomes dos professores não estão presentes no arquivo. Cada linha do arquivo possui
apenas o email do(a) professor(a).

Porém, para a sorte da secretária, o email é composto da seguinte forma:

<nome_do_professor>@gmail.com

Mesmo assim, se ela for mandar email por email, manualmente, vai levar o dia inteiro
para realizar a tarefa.

Ajude a Carol a enviar os emails de forma correta e rápida.

OBS: Obviamente nao precisa enviar um email (ate' porque os emails sao fake). Só
precisa printar na tela a mensagem correta com o nome de cada professor com a primeira
letra maiuscula

DICA: Usar a funcao 'capitalize()' da classe string to Python.

Amanha, no comeco da aula, vou corrigir este exercicio.

Divirta-se!
"""

import os

def enviar_email(nome, email):
    mensagem = f"""
      Bom dia, {nome.capitalize()}!

      Gostaria de dar os meus parabéns a você. É um prazer enorme fazer parte
      dessa equipe de profissionais da PUC. Desejo-te muita saúde, paz e dinheiro!

      Atenciosamente, Carol.
    """
    print('='*80,'\n')
    print(f'Para: {email}\n', mensagem)


def main():
    try:
        arq = open(os.path.join(os.getcwd(), 'cadastro_professores.txt'), 'rt')
        for i in arq:
            p = i.index('@')
            nome = i[:p]
            enviar_email(nome, i)
    except FileNotFoundError:
        print('Arquivo nao encontrado.')

if __name__ == '__main__':
    main()

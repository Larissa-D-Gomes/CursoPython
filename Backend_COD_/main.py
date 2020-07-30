"""Programa principal COD"""

from banco_de_dados import Database
from my_exception import MyException


def main():
    bd = Database()
    try:
        #bd.create('a', 'b')
        bd.create('c', 'd')
    except MyException as e:
        print(e)

    bd.print_dados()

if __name__ == '__main__':
    main()

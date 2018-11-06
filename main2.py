#!/usr/bin/python3

from BCP import BCP
from gerenciador import Gerenciador     # do arquivo gerenciador importa a classe gerenciandor
from escalonador import Escalonador

def leitor(file_name):
    file_reader = open(file_name, 'r');
    
    file_list = file_reader.readlines()
    file_list = [ i[:-1] for i in file_list]
    file_list = [ i.split(' ') for i in file_list]
    
    file_reader.close()

    return file_list


def main():
    lista_processos = leitor("processos.txt")

    gp = Gerenciador()
    for lista in lista_processos:
        bcp = BCP()
        bcp.set_id(lista[0])
        bcp.set_tempo_CPU(lista[1])                        # setando os dados no bcp
        bcp.set_prioridade(lista[2])
        bcp.set_tempo_chegada(lista[3])
        bcp.set_lista_io(lista[4:])
        gp.add_lista_processos(bcp)
    
    for i in gp.get_lista_processos():
        print(i.get_id(), i.get_tempo_chegada(), i.get_lista_io())
    
    escalonador = Escalonador()

if __name__ == '__main__':
	main()
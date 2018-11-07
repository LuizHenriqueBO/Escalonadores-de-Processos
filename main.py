#!/usr/bin/python3

from BCP import BCP
from gerenciador import Gerenciador     # do arquivo gerenciador importa a classe gerenciandor
from escalonador import Escalonador

def leitor(file_name):
    file_reader = open(file_name, 'r');
    
    file_list = file_reader.readlines()
    file_list = [ i.replace('\n', '') for i in file_list]
    file_list = [ i.split(' ') for i in file_list]
    
    file_reader.close()

    return file_list


def main():
    lista_processos = leitor("processos.txt")

    gp = Gerenciador()
    for processo in lista_processos:
        bcp = BCP()
        bcp.set_id(processo[0])
        bcp.set_tempo_CPU(int(processo[1]))                        # setando os dados no bcp
        bcp.set_prioridade(processo[2])
        bcp.set_tempo_chegada(processo[3])
        bcp.set_lista_io(processo[4:])
        
        gp.add_lista_processos(bcp)

        

    
    for i in gp.get_lista_processos():
        #i.lista_IO = [int(k) for k in i.lista_IO]
        print(i.get_id(), i.get_tempo_chegada(), i.get_lista_io(), i.get_tempo_CPU())
             
    escalonador = Escalonador()
    escalonador.prioridade(gp)
    print(escalonador.tempo_total())
    'Tempo total {}'.format(escalonador.tempo_total())

if __name__ == '__main__':
	main()
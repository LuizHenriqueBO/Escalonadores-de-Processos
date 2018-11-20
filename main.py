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
    print("Algoritmos de escalonamento")

    opcao = -1
    while(opcao != '0'):

        fila_processos = leitor("processos.txt")

        gp = Gerenciador()
        for processo in fila_processos:
            bcp = BCP()
            bcp.set_id(processo[0])
            bcp.set_tempo_CPU(processo[1])                        # setando os dados no bcp
            bcp.set_prioridade(processo[2])
            bcp.set_tempo_chegada(processo[3])
            bcp.set_fila_io(processo[4:])
            
            gp.add_fila_processos(bcp)
        
        for i in gp.get_fila_processos():
            #i.fila_IO = [int(k) for k in i.fila_IO]
            print(i.get_id(), i.get_tempo_chegada(), i.get_fila_io(), i.get_tempo_CPU())
            
        escalonador = Escalonador()

        print("Escalonadores")
        print("[1] FIFO")
        print("[2] SJF")
        print("[3] Prioridade")
        print("[4] Round Robin")
        print("[0] Sair")
        
        opcao = input(">> ")
        if(opcao == '1'):
            escalonador.fifo(gp)
        if(opcao == '2'):
            escalonador.sjf(gp)
        if(opcao == '3'):
            escalonador.prioridade(gp)
        if(opcao == '4'):
            escalonador.RoundRobin(gp)
        
        print(escalonador.tempo_total())
        'Tempo total {}'.format(escalonador.tempo_total())

if __name__ == '__main__':
	main()
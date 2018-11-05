#!/usr/bin/python3

from BCP import BCP
from gerenciador import Gerenciador     # do arquivo gerenciador importa a classe gerenciandor



def leitor(file_name):
    file_reader = open(file_name, 'r');
    
    file_list = file_reader.readlines()
    file_list = [ i[:-1] for i in file_list]
    file_list = [ i.split(' ') for i in file_list]
    
    file_reader.close()

    return file_list




def main():
    file_r = leitor("processos.txt")
    Gp = Gerenciador()

    lista_processo = []
    for i in file_r:
        lista_processo
        Gp.add_lista_processos(Processo(i[0], i[1], i[2], i[3], i[4:]))

    print(Gp.get_lista_processos())




    #print(*lista_processo, sep='\n')

    #print(lista_processo[0].io)

    
    processo = 0
    valor = ''
    while True:
        if((processo < 1) or (processo > 3)):
            print("    Escolha o processo! \n\n")
            print("    [1] -> Shortest Job First (SJF)\n")
            print("    [2] -> Prioridade (PRIO)\n")
            print("    [3] -> Round­Robin  (RR)\n\n")
        valor = input()
        if(valor == ''):
            processo = processo
        else: 
            processo = int(valor)  

##################### preenche o BCP ##########################
     bcp = BCP()

        for i in lista:
            bcp.set_id = lista[0]
            bcp.set_tempo_CPU = lista[1]                        # setando os dados no bcp
            bcp.set_prioridade = lista[2]
            bcp.set_tempo_chegada = lista[3]
            bcp.set_lista_io = lista[4:]

        for i in lista:
            print(bcp.get_id)





    if(processo == 1):
        fifo(lista_processo)
        #shortest_job_first()
    elif(processo == 2):
        prioridade()
    elif(processo == 3):
        roundrobin()
    




if __name__ == '__main__':
	main()


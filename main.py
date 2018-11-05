from BCP import BCP
from gerenciador import gerenciador     # do arquivo gerenciador importa a classe gerenciandor





def fifo(lista):

    bcp = BCP()

    for(i in lista):
        bcp.set_id = lista[0]
        bcp.set_tempo_CPU = lista[1]
        bcp.set_prioridade = lista[2]
        bcp.set_tempo_chegada = lista[3]
        bcp.set_lista_io = lista[4:]

    # falta testar pra ver se funciona os getters e setters




    GE = gerenciador()          # estânciando a classe gerenciador 


    GE.set_lista_pronto()


    while 



'''
Algoritmo FIFO
 procedure FIFO(processos)
	contador ← 0
	while True do
		em_espera ← processos.obter(contador)
		executar ← em_espera[0]
		executar.exe()
		contador ← contador + 1
		if executar.finalizado() then
			em_espera.remove(0)
		if em_espera.vazia() then
			break
'''







def leitor(file_name):
    file_reader = open(file_name, 'r');
    
    file_list = file_reader.readlines()
    file_list = [ i[:-1] for i in file_list]
    file_list = [ i.split(' ') for i in file_list]
    
    file_reader.close()

    return file_list



'''
class Processo(object):
    def __init__(self, id, df, prio, dc, io):
        self.id = id
        self.df = df
        self.prio = prio
        self.dc = dc
        self.io = io

    #def __str__(self):
     #   return '{},{},{},{},{}'.format(self.id, self.df, self.prio, self.dc, self.io)

    def __repr__(self):
        return '{},{},{},{},{}'.format(self.id, self.df, self.prio, self.dc, self.io)
'''
def main():
    file_r = leitor("processos.txt")
    #print(file_r)

    lista_processo = []
    for i in file_r:
        lista_processo.append(Processo(i[0], i[1], i[2], i[3], i[4:]))

    print(*lista_processo, sep='\n')

    print(lista_processo[0].io)

    
    processo = 0
    valor = ''
    while True:
        if((processo < 1) or (processo > 3)):
            print("    Escolha o processo! \n\n\n")
            print("    [1] -> Shortest Job First (SJF)\n")
            print("    [2] -> Prioridade (PRIO)\n")
            print("    [3] -> Round­Robin  (RR)\n\n")
        valor = input()
        if(valor == ''):
            processo = processo
        else: 
            processo = int(valor)

    if(processo == 1):
        fifo(lista_processo)
        #shortest_job_first()
    elif(processo == 2):
        prioridade()
    elif(processo == 3):
        roundrobin()
    




if __name__ == '__main__':
	main()


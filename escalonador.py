
'''
Algoritmo FIFO
 procedure FIFO(processos)
	contador = 0
	while True do
		em_espera = processos.obter(contador)
		executar = em_espera[0]
		executar.exe()
		contador = contador + 1
		if executar.finalizado() then
			em_espera.remove(0)
		if em_espera.vazia() then
			break
'''
from gerenciador import Gerenciador
from BCP import BCP

gp = Gerenciador()
bcp = BCP()



class Escalonador():
    timer = 0

    def __init__(self):
        pass

    def tempo_total(self):
        return self.timer



    def fifo(self, lista_processos):
        print("entrei")
        self.timer = 0
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        for processo in lista_processos:
            #print(processo.get_tempo_CPU)
            processo.set_tempo_inicio(self.timer)
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(processo.get_tempo_inicio(), processo.get_tempo_chegada()))
            for tempo in range(processo.get_tempo_CPU):
                if processo.solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:        
                    self.timer+=1
                processo.executar()





    def sjf(self, lista_processos):
        print("\n\n\n\n")
        print("entrei no sjf")
        self.timer = 0
        #lista_processos.sort(key = lambda x: x.get_tempo_CPU())
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        #print(lista_processos[3].get_tempo_chegada())




        
                                                        
        while (self.timer < lista_processos[0].get_tempo_chegada()):
            print("OCIOSO")
            self.timer +=1
            
        gp.add_lista_pronto(lista_processos[0])
        lista_processos.remove(lista_processos[0])

        for p in lista_processos:
            print("ID = %s" % (p.get_id()))

        
        #for processo in gp.get_lista_pronto():
            #print(processo)
    
        while(len(gp.lista_pronto) > 0):
            gp.lista_pronto[0].set_tempo_inicio(self.timer)
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(gp.lista_pronto[0].get_tempo_inicio(), gp.lista_pronto[0].get_tempo_chegada())) 
            for tempo in range(gp.lista_pronto[0].get_tempo_CPU):

                if gp.lista_pronto[0].solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:        
                    self.timer+=1
                gp.lista_pronto[0].executar()
            del gp.lista_pronto[0]    
            print("Timer %d" %self.timer)
            for p in lista_processos:
                #print("ID = %s" % (p.get_id()))
                #print(p.get_id())
                # PEGAR O ID COM O .INDEX 
                if p.get_tempo_chegada() <= self.timer:
                    print("ID = %s" % (p.get_id()))
                    gp.add_lista_pronto(p)
                    lista_processos.remove(p)
                #gp.lista_pronto.remove(processo)
            #print(gp.lista_pronto[1].get_tempo_CPU)    
            gp.lista_pronto.sort(key = lambda x: x.get_tempo_CPU)
            print('\n\n\n')
            for p in gp.lista_pronto:
                print(p.get_id())
            print('\n\n\n')  
               


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

class Escalonador():

    def __init__(self):
	    self.timer = 0

    def tempo_total(self):
        return self.timer


    ###################--------FIFO------##################

    def fifo(self, gp):
        print("entrei")
        self.timer = 0

        #mudei a forma de chegada dos dados
        
        lista_processos = gp.get_lista_processos()

        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        for processo in lista_processos:
            #print(processo.get_tempo_CPU)
            processo.set_tempo_inicio(self.timer)
            print("Cheguei no tempo %d" %(processo.get_tempo_inicio()))            
            for tempo in range(processo.get_tempo_CPU()):
                if processo.solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:        
                    self.timer+=1
                processo.executar()


    ###################--------SJF------##################


    def sjf(self, gp):
        lista_remocao = list()
        lista_processos = gp.get_lista_processos()
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
            for tempo in range(gp.lista_pronto[0].get_tempo_CPU()):

                if gp.lista_pronto[0].solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:
                    self.timer+=1
                gp.lista_pronto[0].executar()
            del gp.lista_pronto[0]    
            print("Timer %d" %self.timer)

            if len(lista_processos) > 0:
                for i in range(len(lista_processos)):
                    #print("ID = %s" % (p.get_id()))
                    #print(p.get_id())
                    # PEGAR O ID COM O .INDEX 
                    if lista_processos[i].get_tempo_chegada() <= self.timer:
                        print("ID = %s" % (p.get_id()))
                        gp.add_lista_pronto(lista_processos[i])
                        #del lista_processos[i]]
                        lista_remocao.append(lista_processos[i])
                        if len(lista_processos) == 0:
                            break
            for process in lista_remocao:
                if process in lista_processos:
                    lista_processos.remove(process)

                #gp.lista_pronto.remove(processo)
            #print(gp.lista_pronto[1].get_tempo_CPU)    
            gp.lista_pronto.sort(key = lambda x: x.get_tempo_CPU())
            print('\n\n\n')
            for p in gp.lista_pronto:
                print(p.get_id())
            print('\n\n\n')  
                



    ###################--------PRIORIDADE------##################


    ###################--------RoundRobin------##################

    def RoundRobin(self, gp):
        print("entrei no RoundRobin")

        quantum = 3         # tempo que ficará no processador
        self.timer= 0

        # Ordeno a lista de processos por ordem de chegada
        lista_processos = gp.get_lista_processos()
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())

        # adiciona o primeiro processo na lista de pronto e tira da lista de processo
        gp.add_lista_pronto(lista_processos[0])
        del(lista_processos[0])

        # caso ainda tenha processo na lista de pronto, continua executando o algoritmo
        while(len(gp.get_lista_pronto()) > 0):
            
            # se o tempo atual for menor que o tempo de chegada do primeiro processo da lista de pronto,
            # o processador fica ocioso, caso contrário, executa o processo
            if(self.timer < gp.get_lista_pronto()[0].get_tempo_chegada()):
                print("OCIOSO")
                self.timer +=1
            else:
                # processo executando é o primeiro processo pronto
                processo_executando = gp.get_lista_pronto()[0]

                for tempo in range(quantum):
                    processo_executando.decrementar_tempo_cpu()

                    if(processo_executando.solicita_io()):
                        
                        gp.add_lista_bloqueio(processo_executando)

                    
                        #print("Entrei io")
                        print("processo ocioso")
                        self.timer += 6
                    else:        
                        self.timer+=1
                    processo.executar()



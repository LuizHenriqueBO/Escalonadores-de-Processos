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

    def prioridade(self, gp):
        print("entrei em prioridade")
        self.timer = 0
        self.tempo_ocioso = 0
        
        gp.lista_processos.sort(key = lambda x: x.get_tempo_chegada())

        while( (len(gp.lista_processos) != 0 or len(gp.lista_bloqueado) != 0 or len(gp.lista_pronto) != 0) and self.timer < 100):
            print("%d %d %d" %(len(gp.lista_processos), len(gp.lista_bloqueado), len(gp.lista_pronto)))
            # chegou algum processo nesse ciclo?
            if((len(gp.lista_processos) != 0) and (int(gp.lista_processos[0].tempo_chegada) == self.timer)):
                print('chegou')
                print(gp.lista_processos[0].id)
                print(self.timer)
                gp.add_lista_pronto(gp.lista_processos[0])
                gp.lista_processos.remove(gp.lista_processos[0])
            
            gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)
            
            # o processo em execucao tem evento io? se sim, coloca na lista de io e remove da lista de prontos
            if(len(gp.lista_pronto) > 0):
                while(gp.lista_pronto[0].solicita_io()): 
                    gp.lista_pronto[0].tempo_executando_io = 5
                    gp.add_lista_bloqueio(gp.lista_pronto[0])
                    gp.lista_pronto.remove(gp.lista_pronto[0])
                    if(len(gp.lista_pronto) == 0):
                        break
                    pass
                pass
            # tem processos a serem executados?
            if(len(gp.lista_pronto) == 0):
                self.tempo_ocioso += 1
                pass

            else:
                # soma +1 no tempo de espera do processos na lista de prontos
                for processo in gp.lista_pronto:
                    processo.tempo_espera += 1
                    pass

                executando = gp.lista_pronto[0]

                # processo em execucao nao ta em espera, tira -1 do tempo de espera dele
                executando.tempo_espera -= 1

                executando.executar()
                if(executando.tempo_executado == executando.get_tempo_CPU()):
                    gp.add_lista_finalizados(executando)
                    gp.lista_pronto.remove(executando)
                    pass
                
            # consome 1 ciclo de IO de cada processo bloqueado
            tam = len(gp.lista_bloqueado)
            i = 0
            while(i < tam):
                gp.lista_bloqueado[i].tempo_executando_io -= 1
                if(gp.lista_bloqueado[i].tempo_executando_io == 0):
                    gp.add_lista_pronto(gp.lista_bloqueado[i])
                    del(gp.lista_bloqueado[i])
                    gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)
                    tam = len(gp.lista_bloqueado)
                else:
                    i += 1

            self.timer += 1
          
        
        print("wwwwwwwwwwwwwwwwwwww")
        print(self.tempo_ocioso)
        print(self.timer)
        print(len(gp.lista_pronto))
        print(len(gp.lista_bloqueado))
        print(len(gp.lista_processos))

        for processo in gp.lista_finalizados:
            print("processo")
            print(processo.id)
            print("tempo executado")
            print(processo.tempo_executado)
            print("tempo de espera")
            print(processo.tempo_espera)
            





    ###################--------RoundRobin------##################
    def escalonar(self, tempo_atual, lista_saida, lista_chegada):
        #   lista_saida.sort(key = lambda x: x.get_tempo_chegada())

        for lista in range(lista_saida):
            if(tempo_atual >= lista.tempo_chegada):
                lista_chegada.append(lista_saida[0])
                del(lista_saida[0])




    def RoundRobin(self, gp):
        print("entrei no RoundRobin")

        quantum = 3         # tempo que ficará no processador
        self.timer= 0

        # Ordeno a lista de processos por ordem de chegada
        lista_processos = gp.get_lista_processos()
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())

        # adiciona o primeiro processo na lista de pronto e tira da lista de processo
        gp.add_lista_pronto(lista_processos[0])
        del(gp.get_lista_processos[0])

        # caso ainda tenha processo na lista de pronto, continua executando o algoritmo
        while(len(gp.get_lista_pronto()) > 0):
            
            # se o tempo atual for menor que o tempo de chegada do primeiro processo da lista de pronto,
            # o processador fica ocioso, caso contrário, executa o processo
            if(self.timer < gp.get_lista_pronto()[0].get_tempo_chegada()):
                print("OCIOSO")
                self.timer +=1
            else:

                # processo executando é o primeiro processo pronto, assim ele sai de pronto e,
                # vai para processo_executando
                processo_executando = gp.get_lista_pronto()[0]
                del(gp.get_lista_pronto()[0])

                # Executar o processo o tempo de quantum
                for tempo in range(quantum):
                    #incrementa o tempo atual
                    self.timer +=1
                    
                    escalonar(tempo, gp.get_lista_processos(), pg.get_lista_pronto())

                    # caso o processo acabou seu tempo de CPU vai para lista de finalizado e,
                    # escalona o próximo processo da lista de pronto.
                    if(not(processo_executando.decrementar_tempo_cpu())):
                        gp.add_lista_finalizados(processo_executando)
                        processo_executando = gp.get_lista_pronto()[0]

                    if(processo_executando.solicita_io()):
                        
                        gp.add_lista_bloqueio(processo_executando)

                    
                        #print("Entrei io")
                        print("processo ocioso")
                        self.timer += 6
                    else:        
                        self.timer+=1
                    processo.executar()



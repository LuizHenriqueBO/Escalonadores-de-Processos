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


    def statistical_graphs(self, title_plus='',):
        import matplotlib.pyplot as plt
        import seaborn as sns
        import pandas as pd 
        sns.set()
        #plt.style.use('classic')

        x = self.lista_execucao[0]
        y = self.lista_execucao[1]

        colors = ['#2300A8', '#00A658']

        plt.xticks(range(len(x)), x)
        plt.bar(range(len(y)), y, align='center', color=colors)

        plt.title(title_plus)
        plt.xlabel('Processo (ID)')
        plt.ylabel('Tempo (ciclo de cloque)')

        plt.show()


    ###################--------FIFO------##################

    def fifo(self, gp):
        print("entrei")
        self.timer = 0

        #mudei a forma de chegada dos dados
        
        fila_processos = gp.get_fila_processos()

        fila_processos.sort(key = lambda x: x.get_tempo_chegada())
        for processo in fila_processos:
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
        fila_remocao = list()
        fila_processos = gp.get_fila_processos()
        print("entrei no sjf")
        self.timer = 0
        #fila_processos.sort(key = lambda x: x.get_tempo_CPU())
        fila_processos.sort(key = lambda x: x.get_tempo_chegada())
        #print(fila_processos[3].get_tempo_chegada())


                                                        
        while (self.timer < fila_processos[0].get_tempo_chegada()):
            print("OCIOSO")
            self.timer +=1
            
        gp.add_fila_pronto(fila_processos[0])
        fila_processos.remove(fila_processos[0])

        for p in fila_processos:
            print("ID = %s" % (p.get_id()))


        #for processo in gp.get_fila_pronto():
            #print(processo)

        while(len(gp.fila_pronto) > 0):
            gp.fila_pronto[0].set_tempo_inicio(self.timer)
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(gp.fila_pronto[0].get_tempo_inicio(), gp.fila_pronto[0].get_tempo_chegada())) 
            for tempo in range(gp.fila_pronto[0].get_tempo_CPU()):

                if gp.fila_pronto[0].solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:
                    self.timer+=1
                gp.fila_pronto[0].executar()
            del gp.fila_pronto[0]    
            print("Timer %d" %self.timer)

            if len(fila_processos) > 0:
                for i in range(len(fila_processos)):
                    #print("ID = %s" % (p.get_id()))
                    #print(p.get_id())
                    # PEGAR O ID COM O .INDEX 
                    if fila_processos[i].get_tempo_chegada() <= self.timer:
                        print("ID = %s" % (p.get_id()))
                        gp.add_fila_pronto(fila_processos[i])
                        #del fila_processos[i]]
                        fila_remocao.append(fila_processos[i])
                        if len(fila_processos) == 0:
                            break
            for process in fila_remocao:
                if process in fila_processos:
                    fila_processos.remove(process)

                #gp.fila_pronto.remove(processo)
            #print(gp.fila_pronto[1].get_tempo_CPU)    
            gp.fila_pronto.sort(key = lambda x: x.get_tempo_CPU())
            print('\n\n\n')
            for p in gp.fila_pronto:
                print(p.get_id())
            print('\n\n\n')  
                



    ###################--------PRIORIDADE------##################

    def prioridade(self, gp):
        print("entrei em prioridade")
        self.timer = 0
        self.tempo_ocioso = 0
        
        gp.fila_processos.sort(key = lambda x: x.get_tempo_chegada())

        while( (len(gp.fila_processos) != 0 or len(gp.fila_bloqueado) != 0 or len(gp.fila_pronto) != 0) and self.timer < 100):
            print("%d %d %d" %(len(gp.fila_processos), len(gp.fila_bloqueado), len(gp.fila_pronto)))
            # chegou algum processo nesse ciclo?
            if((len(gp.fila_processos) != 0) and (int(gp.fila_processos[0].tempo_chegada) == self.timer)):
                print('chegou')
                print(gp.fila_processos[0].id)
                print(self.timer)
                gp.add_fila_pronto(gp.fila_processos[0])
                gp.fila_processos.remove(gp.fila_processos[0])
            
            gp.fila_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)
            
            # o processo em execucao tem evento io? se sim, coloca na fila de io e remove da fila de prontos
            if(len(gp.fila_pronto) > 0):
                while(gp.fila_pronto[0].solicita_io()): 
                    gp.fila_pronto[0].tempo_executando_io = 5
                    gp.add_fila_bloqueio(gp.fila_pronto[0])
                    gp.fila_pronto.remove(gp.fila_pronto[0])
                    if(len(gp.fila_pronto) == 0):
                        break
                    pass
                pass
            # tem processos a serem executados?
            if(len(gp.fila_pronto) == 0):
                self.tempo_ocioso += 1
                pass

            else:
                # soma +1 no tempo de espera do processos na fila de prontos
                for processo in gp.fila_pronto:
                    processo.tempo_espera += 1
                    pass

                executando = gp.fila_pronto[0]

                # processo em execucao nao ta em espera, tira -1 do tempo de espera dele
                executando.tempo_espera -= 1

                executando.executar()
                if(executando.tempo_executado == executando.get_tempo_CPU()):
                    gp.add_fila_finalizados(executando)
                    gp.fila_pronto.remove(executando)
                    pass
                
            # consome 1 ciclo de IO de cada processo bloqueado
            tam = len(gp.fila_bloqueado)
            i = 0
            while(i < tam):
                gp.fila_bloqueado[i].tempo_executando_io -= 1
                if(gp.fila_bloqueado[i].tempo_executando_io == 0):
                    gp.add_fila_pronto(gp.fila_bloqueado[i])
                    del(gp.fila_bloqueado[i])
                    gp.fila_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)
                    tam = len(gp.fila_bloqueado)
                else:
                    i += 1

            self.timer += 1
          
        
        print("wwwwwwwwwwwwwwwwwwww")
        print(self.tempo_ocioso)
        print(self.timer)
        print(len(gp.fila_pronto))
        print(len(gp.fila_bloqueado))
        print(len(gp.fila_processos))

        for processo in gp.fila_finalizados:
            print("processo")
            print(processo.id)
            print("tempo executado")
            print(processo.tempo_executado)
            print("tempo de espera")
            print(processo.tempo_espera)
            





    ###################--------RoundRobin------##################
    def escalonar(self, tempo_atual, fila_saida, fila_chegada):
        #   fila_saida.sort(key = lambda x: x.get_tempo_chegada())

        for fila in (fila_saida):
            if(tempo_atual >= fila.tempo_chegada):
                fila_chegada.append(fila_saida[0])
                del(fila_saida[0])
                return True
            return False






   

    def imprimefila(self, fila):
        for processo in fila:
            processo.imprimedados()
        print("\n\n\n\n\n")
            


    def imprimeprocesso(self, processo):
        processo.imprimedados()
        print("\n\n\n\n\n")


    def RoundRobin(self, gp):
        print("entrei no RoundRobin")

        self.quantum = 4         # tempo que ficará no processador
        self.timer= 0

        # Ordeno a fila de processos por ordem de chegada
        gp.get_fila_processos().sort(key = lambda x: x.get_tempo_chegada())
        
        # caso ainda tenha processo na fila de pronto, bloqueado e processos
        # continua executando o algoritmo
        while((len(gp.get_fila_pronto()) > 0 ) or (len(gp.get_fila_bloqueado()) > 0 ) or (len(gp.get_fila_processos()) > 0 )):
    
            # se tem alguém na fila de bloqueado? caso tenha... tem alguém na
            # posição [0] que tem o tempo menor que o tempo atual ? 
            # se sim, adiciona na fila de pronto e tira da fila de bloqueio!
            #if((len(gp.get_fila_bloqueado()) > 0) and (self.timer >= gp.get_fila_bloqueado()[0].get_tempo_executado()) and gp.get_fila_bloqueado()[0].get_tempo_IO()):

            if((len(gp.get_fila_bloqueado()) > 0) and ( not (gp.get_fila_bloqueado()[0].decrem_tempo_IO()))):
                print("\n tem alguem na fila de bloqueado ?")
                print("tempo atual:",self.timer)
                self.imprimefila(gp.get_fila_bloqueado())
                gp.add_fila_pronto(gp.get_fila_bloqueado()[0])
                del(gp.get_fila_bloqueado()[0])
                print("fila de pronto")
                self.imprimefila(gp.get_fila_pronto())

            else:
                print("não verifico se tem bloqueado")
                print("tempo atual:",self.timer)


            # se tem alguém na fila de processos ? caso tenha... tem alguém na
            # posição [0] que tem o tempo de chegada menor que o tempo atual ? 
            # se sim, adiciona na fila de pronto e tira da fila de processos!
            if((len(gp.get_fila_processos()) > 0 ) and (self.timer >= gp.get_fila_processos()[0].get_tempo_chegada())):
                print("tem alguem na fila de processo ? tempo de chegada", self.timer)
                print("tempo atual:",self.timer)
                self.imprimefila(gp.get_fila_processos())
                gp.add_fila_pronto(gp.get_fila_processos()[0])
                del(gp.get_fila_processos()[0])
                print("fila de pronto")
                self.imprimefila(gp.get_fila_pronto())

            else:
                print("não verifico se tem processos")
                print("tempo atual:",self.timer)


            #tenho alguem na fila de pronto ? se sim executa, se não processador fica ocioso
            if( len(gp.get_fila_pronto()) > 0):
               
                print("fila de pronto")
                self.imprimefila(gp.get_fila_pronto())

                for processo in gp.get_fila_pronto():
                    processo  = gp.get_fila_pronto()[0]
                    #print(processo.get_tempo_CPU)
                    processo.set_tempo_inicio(self.timer)
                    print("tempo de inicio do processo: ")
                    self.imprimeprocesso(processo)
                    #print("Cheguei no tempo %d" %(processo.get_tempo_inicio()))   


                    #for tempo in range(self.quantum):
                    self.tempo = 0
                    while(1):
                        if(self.tempo < self.quantum):
                            
                            print("\n tempo: ",self.tempo)
                            
                            # se tem alguém na fila de bloqueado? caso tenha... tem alguém na
                            # posição [0] que tem o tempo menor que o tempo atual ? 
                            # se sim, adiciona na fila de pronto e tira da fila de bloqueio!
                            #if((len(gp.get_fila_bloqueado()) > 0) and (self.timer >= gp.get_fila_bloqueado()[0].get_tempo_executado())):
                            if((len(gp.get_fila_bloqueado()) > 0) and ( not (gp.get_fila_bloqueado()[0].decrem_tempo_IO()))):
                                print("\n\n ( interno )  tem alguem na fila de bloqueado ? tempo atual: ",self.timer)
                                
                                self.imprimefila(gp.get_fila_bloqueado())
                                gp.add_fila_pronto(gp.get_fila_bloqueado()[0])
                                del(gp.get_fila_bloqueado()[0])
                                print("fila de pronto")
                                self.imprimefila(gp.get_fila_pronto())
                                
                            else:
                                print("\n\n ( interno )  não verifico se tem bloqueado tempo atual: ",self.timer)


                            # se tem alguém na fila de processos ? caso tenha... tem alguém na
                            # posição [0] que tem o tempo de chegada menor que o tempo atual ? 
                            # se sim, adiciona na fila de pronto e tira da fila de processos!
                            if((len(gp.get_fila_processos()) > 0 ) and (self.timer >= gp.get_fila_processos()[0].get_tempo_chegada())):
                                print("\n\n ( interno ) tem alguem na fila de processo ? tempo atual:",self.timer)
                                self.imprimefila(gp.get_fila_processos())
                                gp.add_fila_pronto(gp.get_fila_processos()[0])
                                del(gp.get_fila_processos()[0])
                                print("\n\n fila de pronto")
                                self.imprimefila(gp.get_fila_pronto())

                            else:
                                print("\n\n ( interno ) não verifico se tem processos tempo atual:",self.timer)
                     
                     
                            #se tem tempo de CPU ? se sim executa
                            if((processo.get_tempo_CPU() - processo.get_tempo_executado()) > 0):
                                
                                processo.executar()
                                print("\n\n executa no tempo: ",self.timer)
                               # print("cccccccccccccccccc",processo.get_tempo_CPU() - processo.get_tempo_executado())
                                print("executou o processo: ",end = "")
                                self.imprimeprocesso(processo)
                                self.timer+=1
                                print("fila de pronto")
                                self.imprimefila(gp.get_fila_pronto())

                                #print("finalizados",)
                                #self.imprimefila(gp.get_fila_finalizados())
                                    
                                if((processo.get_tempo_CPU() - processo.get_tempo_executado()) <= 0):
                                    gp.add_fila_finalizados(gp.get_fila_pronto()[0])
                                    gp.get_fila_finalizados()[-1].set_tempo_fim(self.timer)
                                    del(gp.get_fila_pronto()[0])
                                    print("finalizados",)
                                    self.imprimefila(gp.get_fila_finalizados())
                                    break
                                #self.timer+=1
                                


                                if processo.solicita_io():
                                    # tira o processo da lista de pronto e coloca na lista de finalizado
                                    gp.get_fila_pronto()[0].get_fila_io().pop(0)
                                    print("\n\nDEI UM POP\n\n")
                                    gp.add_fila_bloqueio(gp.get_fila_pronto()[0])
                                    gp.get_fila_bloqueado()[0].add_tempo_IO()
                                    print("fila de bloqueio")
                                    self.imprimefila(gp.get_fila_bloqueado())
                                    del(gp.get_fila_pronto()[0])
                                    print("fila de pronto")
                                    self.imprimefila(gp.get_fila_pronto())
                                    break
                                
                                    
                                # senão: addiciona na lista de finalizado e tira da lista de pronto!
                            else:
                                gp.add_fila_finalizados(gp.get_fila_pronto()[0])
                                gp.get_fila_finalizados()[-1].set_tempo_fim(self.timer)
                                del(gp.get_fila_pronto()[0])
                                print("finalizados",)
                                self.imprimefila(gp.get_fila_finalizados())
                                #self.timer+=1

                            self.tempo += 1


                        elif((gp.get_fila_pronto())):
                            gp.add_fila_pronto(gp.get_fila_pronto()[0])
                            del(gp.get_fila_pronto()[0])
                            print("volta pro fim da fila....")
                            print("fila de pronto")
                            self.imprimefila(gp.get_fila_pronto())
                            self.tempo = 0
                            break
                        
            else:
                self.timer +=1

        self.lista_execucao = []
        #print(len(gp.get_fila_finalizados()))
        for processo in gp.get_fila_finalizados():
            self.lista_execucao.append((processo.get_id(), processo.get_tempo_execucao()))
            #print("ewdmekde")
        self.lista_execucao = list(zip(*self.lista_execucao))
        self.statistical_graphs('Escalonador de processo RoundRobin')
        print(self.lista_execucao)

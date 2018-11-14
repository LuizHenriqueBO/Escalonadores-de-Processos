class EscalonadorRoundRobin():

    def __init__(self):
	    self.timer = 0

    def tempo_total(self):
        return self.timer

 
 
 
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







    def verificaFilaBloqueio(self, gp, timer):
        # se tem alguém na fila de bloqueado? caso tenha... tem alguém na
        # posição [0] que tem o tempo menor que o tempo de IO ? 
        # se sim, adiciona na fila de pronto e tira da fila de bloqueio!
        #if((len(gp.get_fila_bloqueado()) > 0) and (self.timer >= gp.get_fila_bloqueado()[0].get_tempo_executado()) and gp.get_fila_bloqueado()[0].get_tempo_IO()):
        if((len(gp.get_fila_bloqueado()) > 0) and ( not (gp.get_fila_bloqueado()[0].decrem_tempo_IO()))):
            print("\n tem alguem na fila de bloqueado ?")
            print("tempo atual:",timer)
            self.imprimefila(gp.get_fila_bloqueado())
            gp.add_fila_pronto(gp.get_fila_bloqueado()[0])
            del(gp.get_fila_bloqueado()[0])
            print("fila de pronto")
            self.imprimefila(gp.get_fila_pronto())
        else:
            print("não verifico se tem bloqueado")
            print("tempo atual:",timer)



    def verificaFilaProcessos(self, gp, timer):
        # se tem alguém na fila de processos ? caso tenha... tem alguém na
        # posição [0] que tem o tempo de chegada menor que o tempo atual ? 
        # se sim, adiciona na fila de pronto e tira da fila de processos!
        if((len(gp.get_fila_processos()) > 0 ) and (timer >= gp.get_fila_processos()[0].get_tempo_chegada())):
            print("tem alguem na fila de processo ? tempo de chegada", timer)
            print("tempo atual:",timer)
            self.imprimefila(gp.get_fila_processos())
            gp.add_fila_pronto(gp.get_fila_processos()[0])
            del(gp.get_fila_processos()[0])
            print("fila de pronto")
            self.imprimefila(gp.get_fila_pronto())

        else:
            print("não verifico se tem processos")
            print("tempo atual:", timer)






    def RoundRobin(self, gp):
        print("entrei no RoundRobin")

        self.quantum = 4         # tempo que ficará no processador
        self.timer= 0

        # Ordeno a fila de processos por ordem de chegada
        gp.get_fila_processos().sort(key = lambda x: x.get_tempo_chegada())
        

        # caso ainda tenha processo na fila de pronto, bloqueado e processos
        # continua executando o algoritmo
        while((len(gp.get_fila_pronto()) > 0 ) or (len(gp.get_fila_bloqueado()) > 0 ) or (len(gp.get_fila_processos()) > 0 )):
    

            self.verificaFilaBloqueio(gp,self.timer)
            self.verificaFilaProcessos(gp,self.timer)
            

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
                            
                            self.verificaFilaBloqueio(gp,self.timer)
                            self.verificaFilaProcessos(gp,self.timer)



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
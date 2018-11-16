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
        # plt.style.use('classic')

        x = self.fila_execucao[0]
        y = self.fila_execucao[1]

        colors = ['#2300A8', '#00A658']

        plt.xticks(range(len(x)), x)
        plt.bar(range(len(y)), y, align='center', color=colors)

        plt.title(title_plus)
        plt.xlabel('Processo (ID)')
        plt.ylabel('Tempo (ciclo de cloque)')

        plt.show()
        
        
       
    def escalonar(self, tempo_atual, fila_saida, fila_chegada):
        # escalona o processo de fila de saida pra fila atual, e faz verificação
        # do tempo atual e tempo de chegada do processo ao cpu
        # pois só posso escalonar um processo que tenha passado pelo processador!

        if(tempo_atual >= fila_saida[0].tempo_chegada):
            fila_chegada.append(fila_saida[0])
            del(fila_saida[0])
            return True
        return False




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
        # inicia as variaveis contadoras de tempo com 0
        self.timer = 0
        self.tempo_ocioso = 0
        
        # ordena a fila de processos por tempo de chegada
        gp.fila_processos.sort(key = lambda x: x.get_tempo_chegada())

        # cada iteração do laço equivale a um ciclo da CPU
        # o loop termina quando todos os processos foram pra fila de finalizados
        while(len(gp.fila_processos) != 0 or len(gp.fila_bloqueado) != 0 or len(gp.fila_pronto) != 0):
            print("%d %d %d" %(len(gp.fila_processos), len(gp.fila_bloqueado), len(gp.fila_pronto)))

            # chegou algum processo nesse ciclo? se sim: remove da fila de processos e insere na fila de aptos
            if((len(gp.fila_processos) != 0) and (int(gp.fila_processos[0].tempo_chegada) == self.timer)):
                print('chegou')
                print(gp.fila_processos[0].id)
                print(self.timer)
                gp.add_fila_pronto(gp.fila_processos[0])
                gp.fila_processos.remove(gp.fila_processos[0])

            # A fila de prontos (aptos) é ordenada por prioridade
            # o processo que estiver na primeira posição da fila é o processo a ganhar a CPU
            gp.fila_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # Mas se o mesmo solicita um evento IO nesse momento,
            # ele é removido da fila de aptos e vai para a fila de bloqueados
            if(len(gp.fila_pronto) > 0):
                # só pára quando encontrar um processo sem requisição de IO no momento, 
                # ou se acabarem todos os processos da fila de prontos
                while(gp.fila_pronto[0].solicita_io()): 
                    gp.fila_pronto[0].tempo_executando_io = 5 # cada evento de IO deixa o processo bloqueado por 5 ciclos da CPU
                    gp.add_fila_bloqueio(gp.fila_pronto[0])
                    gp.fila_pronto.remove(gp.fila_pronto[0])
                    if(len(gp.fila_pronto) == 0):
                        break
                    pass
                pass

            # reordena a fila de aptos por prioridade (ordem crescente)
            gp.fila_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # verifica se ainda tẽm processos a serem executados na fila de aptos
            # se não houver processos, a CPU ficou ociosa nesse ciclo
            if(len(gp.fila_pronto) == 0):
                self.tempo_ocioso += 1
                pass

            # caso contrário, o processo deve ser executado e os demais da fila de aptos ficam em espera
            else:

                # esse é o processo que ganhou a CPU
                executando = gp.fila_pronto[0]

                # adiciona +1 ciclo de espera pra cada processo da fila de aptos
                for processo in gp.fila_pronto:
                    processo.tempo_espera += 1
                    pass

                # menos o processo em execução
                executando.tempo_espera -= 1

                # o processo é executado
                executando.executar()

                # Se o processo nao precisa mais usar a CPU
                # o mesmo é removido da fila de aptos, e vai pra fila de finalizados
                if(executando.tempo_executado == executando.get_tempo_CPU()):
                    gp.add_fila_finalizados(executando)
                    gp.fila_pronto.remove(executando)
                    pass
                
            # a cada ciclo que se passa, é preciso subtrair 1 ciclo de bloqueio dos processos que estão em evento IO 
            tam = len(gp.fila_bloqueado)
            i = 0
            while(i < tam):
                gp.fila_bloqueado[i].tempo_executando_io -= 1
                # se o evento já acabou, o processo é devolvido pra fila de aptos e removido da fila de bloqueio
                if(gp.fila_bloqueado[i].tempo_executando_io == 0):
                    gp.add_fila_pronto(gp.fila_bloqueado[i])
                    del(gp.fila_bloqueado[i])
                    tam = len(gp.fila_bloqueado)
                else:
                    i += 1
            
            # a fila de aptos é ordenada novamente
            gp.fila_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # +1 ciclo de CPU se encerra
            self.timer += 1
            pass

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
            pass       

    
    
    ###################--------RoundRobin------##################
    
    
    
    def verificaFilaBloqueio(self, gp, timer):
        # verifica se tem alguém na fila de bloqueio, caso tenha, decrementa o tempo de I/O e não escalona,
        # caso for decrementar e não possível, a função decrem_tempo_IO() retorna FALSE, negando essa
        # condição ela se torna verdadeira, portando devemos escalonar para a fila de pronto 
        # pois o tempo de I/O já esgotou.

        if((len(gp.get_fila_bloqueado()) > 0) and (not (gp.get_fila_bloqueado()[0].decrem_tempo_IO()))):
            self.escalonar(self.timer, gp.get_fila_bloqueado(),gp.get_fila_pronto())



    def verificaFilaProcessos(self, gp, timer):
        # todo processo que está na fila de processo deve ser escalonado para a fila de pronto de acordo
        # com o tempo de chegada e cada processo tem seu tempo diferente de chegada.
        #
        # Sendo assim verificamos se tem processo na fila de processos
        # Caso tenha, lembramos que os processos foram ordenados por tempo de chegada,
        # Assim verificamos na fila de processos se o timer (clock) é maior ou igual o 
        # tempo de chegada do processo.
        #
        # Se essas condições foram satisfeitas, escalonamos o processo para a fila de pronto.

        if((len(gp.get_fila_processos()) > 0) and (timer >= gp.get_fila_processos()[0].get_tempo_chegada())):
            self.escalonar(self.timer, gp.get_fila_processos(),gp.get_fila_pronto())



    def RoundRobin(self, gp):

        # tempo que ficará no processador
        self.quantum = 4
        # tempo de ciclo
        self.timer = 0

        # Ordeno a fila de processos por ordem de chegada
        gp.get_fila_processos().sort(key=lambda x: x.get_tempo_chegada())


        while((len(gp.get_fila_pronto()) > 0) or (len(gp.get_fila_bloqueado()) > 0) or (len(gp.get_fila_processos()) > 0)):
            # caso ainda tenha processo na fila de pronto, bloqueado e processos
            # continua executando o programa
            self.verificaFilaBloqueio(gp, self.timer)
            self.verificaFilaProcessos(gp, self.timer)

            
            if(len(gp.get_fila_pronto()) > 0):
                # tem alguem na fila de pronto ? se TRUE executa, se FALSE processador fica ocioso

                # executa cada processo da fila de prontos
                for processo in gp.get_fila_pronto():
                    processo = gp.get_fila_pronto()[0]

                    # seta o tempo de início de cada processo
                    processo.set_tempo_inicio(self.timer)
                    # inicializa o tempo de execução para comparar com Quantum
                    self.tempo = 0

                    # execute até que alguém impessa
                    while(1):

                        
                        if(self.tempo < self.quantum):
                            # se tempo de execução atual for menor que Quantum,
                            # continua executando e verifica as fila de bloqueados e fila de processos
                            # Para ver se tem algum processo que precisa ser escalonado para a fila de pronto
                            self.verificaFilaBloqueio(gp, self.timer)
                            self.verificaFilaProcessos(gp, self.timer)

                            # verifica se tem tempo de CPU, caso tenha, continua na fila de pronto
                            if((processo.get_tempo_CPU() - processo.get_tempo_executado()) > 0):

                                # Executa o processo atual e incrementa o timer
                                processo.executar()
                                self.timer += 1

                               
                                if((processo.get_tempo_CPU() - processo.get_tempo_executado()) <= 0):
                                    # Como o processo acabou de ser executado, devemos verificar novamente
                                    # se o tempo de CPU expirou, se isso acontecer, devemos movê-lo pra
                                    # fila de finalizados!
                                    # como no momento ele será o último processo da fila, adicionamos um
                                    # timer no atributo, que ajudará nas análises e geração de gráficos

                                    self.escalonar(self.timer, gp.get_fila_pronto(), gp.get_fila_finalizados())
                                    gp.get_fila_finalizados()[-1].set_tempo_fim(self.timer)
                                    break

                                
                                if processo.solicita_io():
                                    # Caso o processo não foi para a fila de finalizado, verificamos se
                                    # o mesmo solicita I/O, caso isso aconteça, movamos-o para
                                    # fila de bloqueado e adicionamos um tempo de I/O (padrão para todos os
                                    # processos).

                                    self.escalonar(self.timer, gp.get_fila_pronto(), gp.get_fila_bloqueado())
                                    gp.get_fila_bloqueado()[0].add_tempo_IO()
                                    break

                            
                            else:
                                # Caso a diferência do tempo de CPU e tempo Executando seja ZERO,
                                # logo o processo chegou ao fim, sendo assim escalonamos o processo para
                                # a fila de finalizados e adicionamos um timer que será seu tempo final
                                # isso servirá para fins de análise.

                                self.escalonar(self.timer, gp.get_fila_pronto(), gp.get_fila_finalizados())
                                gp.get_fila_finalizados()[-1].set_tempo_fim(self.timer)


                            # incrementa o tempo de execução atual
                            self.tempo += 1

                        
                        else:
                            # caso o tempo de execução atual seja maior ou igual ao Quantum,
                            # movamos o processo para o fim da fila de pronto
                            # logo após zeramos o tempo de execução

                            self.escalonar(self.timer, gp.get_fila_pronto(), gp.get_fila_pronto())
                            self.tempo = 0
                            break

            
            else:
                # caso não tiver nenhum processo a ser executado, o processador ficará ocioso e
                # o timer (tempo de ciclo) será incrementado.
                self.timer += 1


        # Para criar um gráfico de execução, primeiro criamos um array que conterá as informações
        self.fila_execucao = []
        # preenchemos o array fila_execução
        for processo in gp.get_fila_finalizados():
            self.fila_execucao.append((processo.get_id(), processo.get_tempo_execucao()))

        # formatamos os dados, para que fiquem em subvetores separados
        # chamamos a função que montará o gráfico e passamos um título
        self.fila_execucao = list(zip(*self.fila_execucao))
        print(self.fila_execucao)
        self.statistical_graphs('Escalonador de processos RoundRobin')

                                



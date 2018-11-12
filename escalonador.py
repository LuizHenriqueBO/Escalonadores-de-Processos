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
        # inicia as variaveis contadoras de tempo com 0
        self.timer = 0
        self.tempo_ocioso = 0
        
        # ordena a lista de processos por tempo de chegada
        gp.lista_processos.sort(key = lambda x: x.get_tempo_chegada())

        # cada iteração do laço equivale a um ciclo da CPU
        # o loop termina quando todos os processos foram pra lista de finalizados
        while(len(gp.lista_processos) != 0 or len(gp.lista_bloqueado) != 0 or len(gp.lista_pronto) != 0):
            print("%d %d %d" %(len(gp.lista_processos), len(gp.lista_bloqueado), len(gp.lista_pronto)))

            # chegou algum processo nesse ciclo? se sim: remove da lista de processos e insere na lista de aptos
            if((len(gp.lista_processos) != 0) and (int(gp.lista_processos[0].tempo_chegada) == self.timer)):
                print('chegou')
                print(gp.lista_processos[0].id)
                print(self.timer)
                gp.add_lista_pronto(gp.lista_processos[0])
                gp.lista_processos.remove(gp.lista_processos[0])

            # A lista de prontos (aptos) é ordenada por prioridade
            # o processo que estiver na primeira posição da lista é o processo a ganhar a CPU
            gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # Mas se o mesmo solicita um evento IO nesse momento,
            # ele é removido da lista de aptos e vai para a lista de bloqueados
            if(len(gp.lista_pronto) > 0):
                # só pára quando encontrar um processo sem requisição de IO no momento, 
                # ou se acabarem todos os processos da lista de prontos
                while(gp.lista_pronto[0].solicita_io()): 
                    gp.lista_pronto[0].tempo_executando_io = 5 # cada evento de IO deixa o processo bloqueado por 5 ciclos da CPU
                    gp.add_lista_bloqueio(gp.lista_pronto[0])
                    gp.lista_pronto.remove(gp.lista_pronto[0])
                    if(len(gp.lista_pronto) == 0):
                        break
                    pass
                pass

            # reordena a lista de aptos por prioridade (ordem crescente)
            gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # verifica se ainda tẽm processos a serem executados na lista de aptos
            # se não houver processos, a CPU ficou ociosa nesse ciclo
            if(len(gp.lista_pronto) == 0):
                self.tempo_ocioso += 1
                pass

            # caso contrário, o processo deve ser executado e os demais da lista de aptos ficam em espera
            else:

                # esse é o processo que ganhou a CPU
                executando = gp.lista_pronto[0]

                # adiciona +1 ciclo de espera pra cada processo da lista de aptos
                for processo in gp.lista_pronto:
                    processo.tempo_espera += 1
                    pass

                # menos o processo em execução
                executando.tempo_espera -= 1

                # o processo é executado
                executando.executar()

                # Se o processo nao precisa mais usar a CPU
                # o mesmo é removido da lista de aptos, e vai pra lista de finalizados
                if(executando.tempo_executado == executando.get_tempo_CPU()):
                    gp.add_lista_finalizados(executando)
                    gp.lista_pronto.remove(executando)
                    pass
                
            # a cada ciclo que se passa, é preciso subtrair 1 ciclo de bloqueio dos processos que estão em evento IO 
            tam = len(gp.lista_bloqueado)
            i = 0
            while(i < tam):
                gp.lista_bloqueado[i].tempo_executando_io -= 1
                # se o evento já acabou, o processo é devolvido pra lista de aptos e removido da lista de bloqueio
                if(gp.lista_bloqueado[i].tempo_executando_io == 0):
                    gp.add_lista_pronto(gp.lista_bloqueado[i])
                    del(gp.lista_bloqueado[i])
                    tam = len(gp.lista_bloqueado)
                else:
                    i += 1
            
            # a lista de aptos é ordenada novamente
            gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)

            # +1 ciclo de CPU se encerra
            self.timer += 1
            pass

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
            pass       


    ###################--------RoundRobin------##################
    def escalonar(self, tempo_atual, lista_saida, lista_chegada):
        #   lista_saida.sort(key = lambda x: x.get_tempo_chegada())

        for lista in lista_saida:
            if(tempo_atual >= lista.tempo_chegada):
                lista_chegada.append(lista_saida[0])
                del(lista_saida[0])




    def RoundRobin(self, gp):
        print("entrei no RoundRobin")

        quantum = 3         # tempo que ficara no processador
        self.timer= 0

        # Ordeno a lista de processos por ordem de chegada
        lista_processos = gp.get_lista_processos()
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())

        # adiciona o primeiro processo na lista de pronto e tira da lista de processo
        gp.add_lista_pronto(lista_processos[0])
        del(gp.lista_processos[0])

        # caso ainda tenha processo na lista de pronto, continua executando o algoritmo
        while( (len(gp.lista_processos) > 0 or len(gp.lista_bloqueado) > 0 or len(gp.lista_pronto) > 0)):
            print('\n\n')
            print("Tamanho lista de bloqueio: %d" %(len(gp.lista_bloqueado)))
            print("While principal")
            # se o tempo atual for menor que o tempo de chegada do primeiro processo da lista de pronto,
            # o processador fica ocioso, caso contrario, executa o processo
            if(len(gp.lista_pronto) <= 0 or self.timer < gp.lista_pronto[0].get_tempo_chegada()):
                
                print("OCIOSO")
                self.timer +=1
            else:

                # processo executando eh o primeiro processo pronto, assim ele sai de pronto e,
                # vai para processo_executando
                processo_executando = gp.lista_pronto[0]
                print("Executando proceso ID: %d" %(processo_executando.id))
                print("Tempo Executado: %d| Tempo Necessario %d" %(processo_executando.tempo_executado, processo_executando.tempo_necessario))
                del(gp.lista_pronto[0])

                # Executar o processo o tempo de quantum
                for tempo in range(quantum):
                    processo_executando.executar()
                    #incrementa o tempo atual
                    #self.timer +=1
                    
                    self.escalonar(self.timer, gp.lista_processos, gp.lista_pronto)

                    # caso o processo acabou seu tempo de CPU vai para lista de finalizado e,
                    # escalona o proximo processo da lista de pronto.
                    if(not(processo_executando.decrementar_tempo_cpu())):
                        gp.add_lista_finalizados(processo_executando)
                        if(len(gp.lista_pronto) > 0):
                            processo_executando = gp.lista_pronto[0]
                        break

                    if(processo_executando.solicita_io()):
                        processo_executando.tempo_executando_io = 5
                        gp.add_lista_bloqueio(processo_executando)
                        #print("Entrei io")
                        print("Processo %d bloqueado pra IO" %(processo_executando.id))
                        self.timer += 1
                        break
                    else:        
                        self.timer+= 1
                    #processo_executando.executar()
                    if(tempo == 2):
                        gp.lista_pronto.append(processo_executando)
            tam = len(gp.lista_bloqueado)
            i = 0
            while(i < tam):
                #print("While true")
                gp.lista_bloqueado[i].tempo_executando_io -= 1
                if(gp.lista_bloqueado[i].tempo_executando_io == 0):
                    print("Processo com o id %d saiu do IO" %(gp.lista_bloqueado[i].id))
                    gp.add_lista_pronto(gp.lista_bloqueado[i])
                    del(gp.lista_bloqueado[i])
                    gp.lista_pronto.sort(key = lambda x: x.get_prioridade(), reverse = True)
                    tam = len(gp.lista_bloqueado)
                else:
                    i += 1    
                                



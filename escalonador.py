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

<<<<<<< HEAD
    def fifo(self, gp):
=======
    def tempo_total(self):
        return self.timer



    def fifo(self, lista_processos):
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
        print("entrei")
        self.timer = 0

        #mudei a forma de chegada dos dados
        
        lista_processos = gp.get_lista_processos()

        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        for processo in lista_processos:
            #print(processo.get_tempo_CPU)
            processo.set_tempo_inicio(self.timer)
<<<<<<< HEAD
            print("Cheguei no tempo %d" %(processo.get_tempo_inicio()))            
            for tempo in range(processo.get_tempo_CPU()):
=======
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(processo.get_tempo_inicio(), processo.get_tempo_chegada()))
            for tempo in range(processo.get_tempo_CPU):
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
                if processo.solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
                else:        
                    self.timer+=1
                processo.executar()


<<<<<<< HEAD
###################--------SJF------##################


    def sjf(self, gp):
        lista_remocao = list()
        lista_processos = gp.get_lista_processos()
=======



    def sjf(self, lista_processos):
        print("\n\n\n\n")
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
        print("entrei no sjf")
        self.timer = 0
        #lista_processos.sort(key = lambda x: x.get_tempo_CPU())
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        #print(lista_processos[3].get_tempo_chegada())


<<<<<<< HEAD
=======


        
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
                                                        
        while (self.timer < lista_processos[0].get_tempo_chegada()):
            print("OCIOSO")
            self.timer +=1
            
        gp.add_lista_pronto(lista_processos[0])
        lista_processos.remove(lista_processos[0])

        for p in lista_processos:
            print("ID = %s" % (p.get_id()))

<<<<<<< HEAD

        #for processo in gp.get_lista_pronto():
            #print(processo)

        while(len(gp.lista_pronto) > 0):
            gp.lista_pronto[0].set_tempo_inicio(self.timer)
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(gp.lista_pronto[0].get_tempo_inicio(), gp.lista_pronto[0].get_tempo_chegada())) 
            for tempo in range(gp.lista_pronto[0].get_tempo_CPU()):
=======
        
        #for processo in gp.get_lista_pronto():
            #print(processo)
    
        while(len(gp.lista_pronto) > 0):
            gp.lista_pronto[0].set_tempo_inicio(self.timer)
            print("Ganhei o processador no tempo %d e cheguei no tempo %d" %(gp.lista_pronto[0].get_tempo_inicio(), gp.lista_pronto[0].get_tempo_chegada())) 
            for tempo in range(gp.lista_pronto[0].get_tempo_CPU):
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b

                if gp.lista_pronto[0].solicita_io():
                    #print("Entrei io")
                    print("processo ocioso")
                    self.timer += 6
<<<<<<< HEAD
                else:
=======
                else:        
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
                    self.timer+=1
                gp.lista_pronto[0].executar()
            del gp.lista_pronto[0]    
            print("Timer %d" %self.timer)
<<<<<<< HEAD

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
=======
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
>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b
            print('\n\n\n')
            for p in gp.lista_pronto:
                print(p.get_id())
            print('\n\n\n')  
<<<<<<< HEAD
                



###################--------PRIORIDADE------##################
=======
               

>>>>>>> 89c4bbeec53facb11cc6b7ce86877fea260c945b

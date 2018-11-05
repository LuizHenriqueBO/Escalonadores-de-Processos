
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
from gerenciador import Gerenciador
from BCP import BCP

gp = Gerenciador()
bcp = BCP()



class Escalonador():
    timer = 0

    def __init__(self):
        pass

    def fifo(self, lista_processos):
        self.timer = 0
        lista_processos.sort(key = lambda x: x.get_tempo_chegada())
        for processo in lista_processos:
            processo.set_tempo_inicio(self.timer)
            for tempo in range(processo.get_tempo_cpu()):
                if processo.solicita_io:
                    for i in range(5):
                        self.timer +=1
                else:        
                    self.timer+=1
                    processo.executar()

        

            


class BCP():
    def __init__(self): #, id, prioridade, estado, tempo_chegada, tempo_inicio,tempo_CPU
        self.id = 0
        self.prioridade = 0
        self.tempo_chegada = 0
        self.tempo_inicio = 0
        self.tempo_CPU = 0
        self.tempo_executado = 0
        self.lista_IO = []

    def get_id(self):
        return self.id
    
    def get_prioridade(self):
        return self.prioridade
    
    def get_tempo_chegada(self):
        return self.tempo_chegada
    
    def get_tempo_inicio(self):
        return self.tempo_inicio
    
    def get_tempo_CPU(self):
        return self.get_tempo_CPU

    def get_lista_io(self):
        return self.lista_IO            # testar pra ver se funciona com pop

    def remove_lista_io(self):
        self.lista_IO.remove(self.lista_IO[0])


################# setters ############################
                
    
    def set_id(self, id):
        self.id = id
    
    def set_prioridade(self, prioridade):
        self.prioridade = prioridade
    
    def set_tempo_chegada(self, chegada):
        self.tempo_chegada = chegada
    
    def set_tempo_inicio(self, tempo_inicio):
        self.tempo_inicio = tempo_inicio
    
    def set_tempo_CPU(self, tempo_cpu):
        self.get_tempo_CPU = tempo_cpu

    def set_lista_io(self, lista):
        self.lista_IO = lista

    def decrementar_tempo_cpu(self):
        self.tempo_CPU -=1

        ###################### métodos #############
    def executar(self):
        self.tempo_executado +=1
    
    def finalizado(self):
        if(self.tempo_executado == self.tempo_CPU):
            return True
        else:
            return False

    def solicita_io(self):
        if(self.tempo_executado in self.lista_IO):
            return True
        else:
            return False


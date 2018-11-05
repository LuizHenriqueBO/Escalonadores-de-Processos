
class BCP():
    def __init__(self): #, id, prioridade, estado, tempo_chegada, tempo_inicio,tempo_CPU
        self.id
        self.prioridade
        self.estado
        self.tempo_chegada
        self.tempo_inicio
        self.tempo_CPU
        self.lista_IO = []

    def get_id(self):
        return self.id
    
    def get_prioridade(self):
        return self.prioridade
    
    def get_estado(self):
        return self.estado
    
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


################# setters ############################--------------------------
                
    
    def set_id(self, id):
        self.id = id
    
    def set_prioridade(self, prioridade):
        self.prioridade = prioridade
    
    def set_estado(self, estado):
        self.estado = estado
    
    def set_tempo_chegada(self, chegada):
        self.tempo_chegada = chegada
    
    def set_tempo_inicio(self, tempo_inicio):
        self.tempo_inicio = tempo_inicio
    
    def set_tempo_CPU(self, tempo_cpu):
        self.get_tempo_CPU = tempo_cpu

    def set_lista_io(self, lista):
        self.lista_IO = lista
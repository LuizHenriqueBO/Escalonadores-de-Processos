 
class Gerenciador():
    def __init__(self):
        self.lista_processos = []
        self.lista_pronto = []
        self.lista_bloqueado = []
        
    
    ##### getters
    def get_lista_pronto(self):
        return self.lista_pronto
    
    def get_lista_bloqueado(self):
        return self.lista_bloqueado[0]

    def get_lista_processos(self):
        return self.lista_processos


    #### add
    def add_lista_pronto(self, processo):
        self.lista_pronto.append(processo)
    
    def add_lista_bloqueio(self, processo):
        self.lista_bloqueado.append(processo)

    def add_lista_processos(self, processo):
        self.lista_processos.append(processo)
    
    
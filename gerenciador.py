class Gerenciador():
    def __init__(self):
        self.lista_processos = []
        self.lista_pronto = []
        self.lista_bloqueado = []
        self.lista_finalizados = []
        
    
    ##### getters
    def get_lista_pronto(self):
        return self.lista_pronto[0]
    
    def get_lista_bloqueado(self):
        return self.lista_bloqueado[0]

    def get_lista_processos(self):
        return self.lista_processos

    def get_lista_finalizados(self):
        return self.lista_finalizados[0]


    #### add
    def add_lista_finalizados(self, processo):
        self.lista_finalizados.append(processo)

    def add_lista_pronto(self, processo):
        self.lista_pronto.append(processo)
    
    def add_lista_bloqueio(self, processo):
        self.lista_bloqueado.append(processo)

    def add_lista_processos(self, processo):
        self.lista_processos.append(processo)
    
    
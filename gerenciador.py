
class gerenciador():
    def __init__(self):
        #self.processo_novo = []
        self.lista_pronto = []
        self.lista_bloqueado = []
        self.programa_executando = []
    
    def get_lista_pronto(self):
        return self.lista_processo[0]
    
    def get_lista_bloqueado(self):
        return self.lista_bloqueado[0]

    #def get_processo_novo(self):
     #   return self.processo_novo

    def get_programa_executando(self):
        return self.programa_executando

    def set_lista_pronto(self, processo):
        self.lista_pronto.append(processo)

    #def set_processo_novo(self, processo):
     #   self.processo_novo = processo
    
    def set_lista_bloqueio(self, processo):
        self.lista_bloqueado.append(processo)

    def set_programa_executando(self, processo):
        self.processo_executando = processo


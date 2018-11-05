
class gerenciador():
    self.processo_novo = []
    self.lista_pronto = []
    self.lista_bloqueado = []
    self.programa_executando = []
    
    def get_lista_pronto():
        return self.lista_processo[0]
    
    def get_lista_bloqueado():
        return self.lista_bloqueado[0]

    def get_processo_novo():
        return self.processo_novo

    def get_programa_executando():
        return self.programa_executando

    def set_lista_pronto(processo):
        self.lista_pronto.append(processo)

    def set_processo_novo(processo):
        self.processo_novo = processo
    
    def set_lista_bloqueio(processo):
        self.lista_bloqueado.append(processo)

    def set_programa_executando(processo):
        self.processo_executando = processo


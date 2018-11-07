
class BCP():
    def __init__(self): #, id, prioridade, estado, tempo_chegada, tempo_inicio,tempo_CPU
        self.id = 0
        self.prioridade = 0
        self.tempo_chegada = 0
        self.tempo_inicio = 0
        self.tempo_CPU = 0
        self.tempo_executado = 0
        self.lista_IO = []

        self.tempo_executando_io = 0
        self.tempo_espera = 0

    def get_id(self):
        return self.id
    
    def get_prioridade(self):
        return self.prioridade
    
    def get_tempo_chegada(self):
        return self.tempo_chegada
    
    def get_tempo_inicio(self):
        return self.tempo_inicio
    
    def get_tempo_CPU(self):
        return self.tempo_CPU

    def get_lista_io(self):
        return self.lista_IO            # testar pra ver se funciona com pop

    def get_tempo_executado(self):
        return self.tempo_executado


 ################# setters ############################
                
    
    def set_id(self, id):
        self.id = int(id)
    
    def set_prioridade(self, prioridade):
        self.prioridade = int(prioridade)
    
    def set_tempo_chegada(self, chegada):
        self.tempo_chegada = int(chegada)
    
    def set_tempo_inicio(self, tempo_inicio):
        self.tempo_inicio = int(tempo_inicio)
    
    def set_tempo_CPU(self, tempo_cpu):
        self.tempo_CPU = int(tempo_cpu)

    def set_lista_io(self, lista):
        print(lista)
        self.lista_IO = list(map(int,lista)) if lista and lista[-1] else []

   

        ###################### metodos #############
    def executar(self):
        self.tempo_executado +=1
    
    def remove_lista_io(self):
        self.lista_IO.remove(self.lista_IO[0])
    

    def decrementar_tempo_cpu(self):
        if(self.tempo_CPU  <= 0):
            return False
        else:
            self.tempo_CPU -=1
            return True


    def finalizado(self):
        if(self.tempo_executado == self.tempo_CPU):
            return True
        else:
            return False

    def solicita_io(self):
        #print("Solicita io %d" % self.tempo_executado)
        if(self.tempo_executado in self.lista_IO):
            print("Entrei em IO %d" % self.tempo_executado)
            #print("QQQ")
            return True
        else:
            return False




class Hornoindustrial:  
    estado = ""
    temperatura = 0
    modo_coccion = ""
    #Constructor con parametros
    def __init__(self, modo_coccion , temperatura ):  
        self.modo_coccion = modo_coccion
        self.estado = "Apagado" 
        self.temperatura =  temperatura
        
    def get_modo_coccion (self):
        return self._modo_coccion
    def set_modo_coccion(self,modo_coccion ):
        self._modo_coccion = modo_coccion 
            
            
             
    def get_estado (self):
        return self._estado
    def set_estado(self, estado ):
        self._estado  = estado     
    def set_temperatura(self , temperatura):
        self.temperatura=temperatura
             
    def encender(self,h):
            
        if h.estado == "Encendido":
            return False
        else:
            h.set_estado("Encendido")
        return True
            
         
        
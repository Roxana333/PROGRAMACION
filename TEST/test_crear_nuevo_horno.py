from Entidades.hornoindustial import Hornoindustrial
import unittest


class testHorno(unittest.TestCase):
    #Este test es para verificar de que al crear un nuevo horno se crea con el estado Apagado
    def test_crear_nuevo_horno(self) -> None:
        horno = Hornoindustrial("Lento",1000)
        self.assertEqual(horno.estado,"Apagado")
        #self.assertTrue()
    #Este test es para verificar que al encender un horno, este pase a estado encendido
    def test_encender_horno(self) -> None:
        horno = Hornoindustrial("rapido",1000)
        self.assertTrue(horno.encender(horno))
    
        
       
if __name__ == '__main__':
    unittest.main()       
       
       
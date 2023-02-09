class Transaccion():
    def __init__(self, fecha, iva, total_sin_iva):
        self.fecha = fecha
        self.iva =iva
        self.total_sin_iva = total_sin_iva
        
class Compra(Transaccion):
    def calcular_total_gasto(self):
        return self.iva+self.total_sin_iva

class Venta(Transaccion):
    pass
class Transaccion():
    def __init__(self, fecha, iva, total_sin_iva):
        self.fecha = fecha
        self.iva =iva
        self.total_sin_iva = total_sin_iva
        
class Compra(Transaccion):
    pass

class Venta(Transaccion):
    pass
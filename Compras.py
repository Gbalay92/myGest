from modulos.Utilities.Utilities import crear_objetos_compra, process
if __name__=="__main__":
    #crear_nominas()
    lista=crear_objetos_compra()
    process("compras_procesadas", "fecha", "iva", "total_sin_iva", lista)

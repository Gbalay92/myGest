from modulos.Utilities.Utilities import crear_objetos_compra, process
if __name__=="__main__":
    #leer fichero compras y crear archivo compras procesadas
    lista=crear_objetos_compra()
    process("compras_procesadas", "fecha", "iva", "total_sin_iva", lista)

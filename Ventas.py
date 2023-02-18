from modulos.Utilities.Utilities import process,crear_objetos_venta, write_gerencia

if __name__ == '__main__':
    #leer ficheros de ventas y crear fichero ventas procesadas
    lista=crear_objetos_venta()
    #process("ventas_procesadas", "fecha", "iva", "total_sin_iva", lista)

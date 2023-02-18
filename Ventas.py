from modulos.Utilities.Utilities import process_transactions,crear_objetos_venta

if __name__ == '__main__':
    #leer ficheros de ventas y crear fichero ventas procesadas
    try:
        lista=crear_objetos_venta()
        process_transactions("ventas_procesadas", "fecha", "iva", "total_sin_iva", lista)
    except FileNotFoundError:
        exit()

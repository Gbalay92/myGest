from modulos.Utilities.Utilities import process_report, dict_cell_iva

if __name__ == '__main__':
    try:
        process_report("Documentos/facturas/compras_procesadas.xlsx", 3, 1, "Documentos/facturas/declaracion-ive.xlsx", dict_cell_iva)
        process_report("Documentos/facturas/ventas_procesadas.xlsx", 2, 1,"Documentos/facturas/declaracion-ive.xlsx", dict_cell_iva)
    except FileNotFoundError:
        exit()
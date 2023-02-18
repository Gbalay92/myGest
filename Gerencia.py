from modulos.Utilities.Utilities import process_gasto_nomina,process_report, dict_cell_gerencia


if __name__=="__main__":
    try:
        process_gasto_nomina(dict_cell_gerencia)
        process_report("Documentos/facturas/compras_procesadas.xlsx", 4, 2, "Documentos/gerencia/informe-xerencia.xlsx",dict_cell_gerencia)
        process_report("Documentos/facturas/ventas_procesadas.xlsx", 10, 2, "Documentos/gerencia/informe-xerencia.xlsx", dict_cell_gerencia)
    except FileNotFoundError:
        exit()

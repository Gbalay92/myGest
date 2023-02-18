from modulos.Utilities.Utilities import process_gasto_nomina,process_report
                
if __name__=="__main__":
    process_gasto_nomina()
    process_report("Documentos/facturas/compras_procesadas.xlsx", 4)
    process_report("Documentos/facturas/ventas_procesadas.xlsx", 10)

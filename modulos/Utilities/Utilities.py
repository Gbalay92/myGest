from modulos.models.Transaccion import Compra, Venta
import openpyxl as op
import os
import formulas
from datetime import datetime, timedelta


def process(nombre_fichero,header1,header2,header3,lista_a_procesar):
    filepath = "Documentos/facturas/"+nombre_fichero+".xlsx"
    wb = op.Workbook()
    ws=wb.active
    ws['A1']=header1
    ws['B1']=header2
    ws['C1']=header3
    for element in lista_a_procesar:
        ws.append([element.fecha,element.iva,element.total_sin_iva])
    wb.save(filepath)
    
def crear_objetos_compra():
    lista_compras = []
    path="Documentos/facturas/compras"
    filename="compras.xlsx"
    xl_model=formulas.ExcelModel().loads(os.path.join(path,filename)).finish()
    solution=xl_model.calculate()
    row=3
    for i in solution:
        cell_ref_fecha=f"'[{filename}]T3-2022'!A{row}"
        cell_ref_total=f"'[{filename}]T3-2022'!E{row}"
        cell_ref_iva=f"'[{filename}]T3-2022'!F{row}"
        try:
            fecha=solution.get(cell_ref_fecha).values[cell_ref_fecha]
            total=solution.get(cell_ref_total).values[cell_ref_total]
            iva=solution.get(cell_ref_iva).values[cell_ref_iva]
            for f in fecha:
                if str(type(f))=="<class 'numpy.ndarray'>":
                    lista_compras.append(Compra(xldate_to_datetime(f[0][0]).strftime("%d/%m/%Y"), iva[-1][0][0], total[-1][0][0]))
            row+=1
        except AttributeError:
            break
    return lista_compras


        
def crear_objetos_venta():
    lista_ventas = []
    dir_path="Documentos/facturas/ventas"
    for file in os.listdir(dir_path): 
        cell_ref_total=f"'[{file}]FACTURA'!F47"
        cell_ref_fecha=f"'[{file}]FACTURA'!H3"
        cell_ref_iva=f"'[{file}]FACTURA'!F48"
        xl_model=formulas.ExcelModel().loads(os.path.join(dir_path,file)).finish()
        solution=xl_model.calculate()
        total=solution.get(cell_ref_total).values[cell_ref_total]
        fecha=solution.get(cell_ref_fecha).values[cell_ref_fecha]
        iva=solution.get(cell_ref_iva).values[cell_ref_iva]
        gasto_mes=total[-1][0][0]
        f=fecha[-1][0][0]
        i=iva[-1][0][0]
        lista_ventas.append(Venta(xldate_to_datetime(f).strftime("%d/%m/%Y") , i, gasto_mes))
        
        #lista_ventas.append(Venta(fecha, iva, total))
    return lista_ventas

def xldate_to_datetime(xldate):
	temp = datetime(1899, 12, 30)
	delta = timedelta(days=xldate)
	return temp+delta

def write_gerencia(cantidad, celda):
    file="Documentos/gerencia/informe-xerencia.xlsx"
    wb = op.load_workbook(file)
    ws=wb.active
    ws[f'{celda}']=cantidad
    wb.save(file)
from modulos.models.Transaccion import Compra, Venta
import openpyxl as op
import xlwings as xw
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
    lista_compra = []
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
                    lista_compra.append(Compra(xldate_to_datetime(f[0][0]).strftime("%d/%m/%Y"), iva[-1][0][0], total[-1][0][0]))
            row+=1
        except AttributeError:
            break
    return lista_compra


        
def crear_objetos_venta():
    xw.App(visible=False)
    lista_ventas = []
    dir_path="Documentos/facturas/ventas"
    for path in os.listdir(dir_path): 
        book=xw.Book(os.path.join(dir_path,path))
        sheet=xw.sheets['factura']
        fecha=sheet['H3'].value.strftime("%d/%m/%Y")
        iva=sheet['F48'].value
        total=sheet['F47'].value
        venta=Venta(fecha, iva, total)
        lista_ventas.append(venta)
        #print(fecha, iva, total)
        xw.App().quit()
    return lista_ventas

def xldate_to_datetime(xldate):
	temp = datetime(1899, 12, 30)
	delta = timedelta(days=xldate)
	return temp+delta
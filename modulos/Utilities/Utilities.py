from modulos.models.Transaccion import Compra, Venta
import openpyxl as op
import xlwings as xw
import os


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
    path="Documentos/facturas/compras/compras.xlsx"
    book=xw.Book(path)
    sheet=xw.sheets['T3-2022']
    datos = sheet["A3"].expand().value
    # print(len(datos))
    for i in range(0,len(datos)):
        #print(datos[i][0].strftime("%m/%d/%Y"), datos[i][4], datos[i][5] )
        compra=Compra(datos[i][0].strftime("%m/%d/%Y"), datos[i][4], datos[i][5])
        lista_compra.append(compra)
    return lista_compra
        
def crear_objetos_venta():
    lista_ventas = []
    dir_path="Documentos/facturas/ventas"
    for path in os.listdir(dir_path): 
        book=xw.Book(os.path.join(dir_path,path))
        sheet=xw.sheets['factura']
        fecha=sheet['H3']
        iva=sheet['F48']
        total=sheet['F47']
        venta=Venta(fecha, iva, total)
        lista_ventas.append(venta)
    return lista_ventas
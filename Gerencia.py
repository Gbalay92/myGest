import os
import openpyxl as op
import formulas
import datetime


#def calcular_gasto_nomina():
dir="Documentos/nominas"
for folder in os.listdir(dir):
    dir_path = os.path.join(dir,folder)
    gasto_mes=0
    for path in os.listdir(dir_path): 
        cellRef=f"'[{path}]NOMINA2'!F54"
        xl_model=formulas.ExcelModel().loads(os.path.join(dir_path,path)).finish()
        solution=xl_model.calculate()
        values=solution.get(cellRef).values[cellRef]
        for v in values:
            if str(type(v))=="<class 'numpy.ndarray'>":
                gasto_mes+=v[0][0]
                print(gasto_mes)

        

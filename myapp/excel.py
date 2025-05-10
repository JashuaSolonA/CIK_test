# CODIGO PARA LEER EXCEL COMO FUNCIÓN

import openpyxl
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
import json
import os
import time


def leer_excel_periodico(json_path='data_excel.json', intervalo=0.5, loop=True):
    """
    Lee datos periódicamente desde un archivo Excel definido en un JSON.
    Devuelve un diccionario como:
    {
        "name_1": "data_1",
        "name_2": "data_2",
        ...
    }
    """
    base_path = os.path.dirname(__file__)
    full_json_path = os.path.join(base_path, json_path)

    try:
        with open(full_json_path) as f:
            data_excel = json.load(f)
    except Exception as e:
        print(f"[ERROR] Al cargar archivo JSON: {e}")
        return {}

    path = data_excel.get('path')
    data = data_excel.get('data', {})

    if not os.path.exists(path):
        print(f"[ERROR] El archivo Excel '{path}' no existe.")
        return {}

    while True:
        resultados = {}

        try:
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)

            for nombre_variable, info in data.items():
                try:
                    sheet_index = int(info['sheet'])
                    address = info['address']

                    hoja = wb.worksheets[sheet_index]

                    col_letter, row = coordinate_from_string(address)
                    col = column_index_from_string(col_letter)

                    valor = hoja.cell(row=row, column=col).value
                    resultados[nombre_variable] = valor

                except Exception as e:
                    print(f"[ERROR] leyendo '{nombre_variable}': {e}")
                    resultados[nombre_variable] = None

            wb.close()

            # Retornar resultados si no es en loop
            if not loop:
                return resultados

            print(resultados)  # Solo para debug
            time.sleep(intervalo)

        except Exception as e:
            print(f"[ERROR] General: {e}")
            time.sleep(intervalo)


# EJEMPLO DE USO UNA SOLA VEZ:
# datos = leer_excel_periodico(loop=False)
# print(datos)

import pandas as pd
import os

def main():
    df = leer_archivos()
    df = agregar_filtros(df)

    visualizar_datos(df)
    exportar_datos(df)

def leer_archivos():
    print("Leyendo archivo")

    input_cols = []

    path = "..\Input"
    filename = input("Ingresar el nombre del archivo: ") + "xlsx"
    fullpath = os.path.join(path, filename)

    df = pd.read_excel("*.xlsx",
    sheet_name)

def angle_filtros():
    return
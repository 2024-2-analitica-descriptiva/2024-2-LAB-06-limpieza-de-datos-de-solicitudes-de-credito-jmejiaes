"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    data = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col=0)
    data.dropna(inplace=True)

    data['sexo'] = data['sexo'].str.lower()

    data['tipo_de_emprendimiento'] = data['tipo_de_emprendimiento'].str.lower()
    data['tipo_de_emprendimiento'] = data['tipo_de_emprendimiento'].str.strip()

    data['barrio'] = data['barrio'].str.lower()
    data['barrio'] = data['barrio'].str.replace("_", " ").str.replace("-", " ")

    data['idea_negocio'] = data['idea_negocio'].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()

    data['monto_del_credito'] = data['monto_del_credito'].str.strip().str.replace("$","").str.replace(",","").str.replace(".00","").astype(int)

    data['línea_credito'] = data['línea_credito'].str.replace("_", " ").str.replace("-", " ").str.lower().str.strip()

    data['fecha_homologada'] = pd.to_datetime(data['fecha_de_beneficio'], dayfirst=True, errors='coerce')

    data['fecha_homologada'] = data['fecha_homologada'].fillna(
        pd.to_datetime(data['fecha_de_beneficio'], format="%Y/%m/%d", errors='coerce')
    )
    
    data.drop(columns='fecha_de_beneficio', inplace=True)
    data.rename(columns={'fecha_homologada':'fecha_de_beneficio'}, inplace=True)

    data.drop_duplicates(inplace=True)

    output_directory = os.path.join('files', 'output')
    output_file = os.path.join(output_directory, 'solicitudes_de_credito.csv')
    os.makedirs(output_directory, exist_ok=True)
    data.to_csv(output_file, sep=';')

    return
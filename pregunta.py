"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.dropna(inplace=True)
    df = df.apply(lambda x: x.astype(str))
    df = df.apply(lambda x: x.str.replace("$", ""))
    df = df.apply(lambda x: x.str.replace(",", ""))
    df = df.apply(lambda x: x.str.replace("_", "-"))
    df = df.apply(lambda x: x.str.replace("-", " "))
    df = df.apply(lambda x: x.str.lower())
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format='mixed')
    df.drop_duplicates(inplace=True)
    df = df.copy()
    df = df.drop_duplicates(subset=df.columns[1:], keep="first")
    return df

df = clean_data()
print(df.tipo_de_emprendimiento.value_counts().to_list())
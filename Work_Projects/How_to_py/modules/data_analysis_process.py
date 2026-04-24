1#Extract 
from pyspark.sql import SparkSession

def extract(file_path):
    # Iniciar la sesión de Spark
    spark = SparkSession.builder \
        .appName("Load CSV") \
        .getOrCreate()

    # Leer el archivo CSV con PySpark
    df_spark = spark.read.csv(file_path, header=True, inferSchema=True)

    # Mostrar el DataFrame de PySpark
    df_spark.show()
    return df_spark

2#Transform
def transform(ruta_archivo):
    # Iniciar una sesión de Spark
    spark = SparkSession.builder \
        .appName("Cargar CSV y mostrar info") \
        .getOrCreate()

    # Leer el archivo CSV con PySpark
    df_spark = spark.read.csv(ruta_archivo, header=True, inferSchema=True)

    # Mostrar la información del DataFrame 
    df_spark.printSchema()  # Muestra el esquema de las columnas (tipos de datos y nombres)

    # Mostrar el conteo de filas y columnas
    print(f"Cantidad de filas: {df_spark.count()}")
    print(f"Cantidad de columnas: {len(df_spark.columns)}")

    return df_spark

# 3#Load
from pyspark.sql.functions import avg
import matplotlib.pyplot as plt

def procesar_datos_y_graficar(file_path, column_name, column_value):
    # Iniciar la sesión de Spark
    spark = SparkSession.builder.appName("Load CSV").getOrCreate()
    
    # Leer el archivo CSV con PySpark y filtrar el DataFrame
    df_spark = spark.read.csv(file_path, header=True, inferSchema=True).filter(f"{column_name} == '{column_value}'")
    
    # Calcular la media de las columnas numéricas
    df_medias = df_spark.select([avg(col).alias(col + "_media") for col, dtype in df_spark.dtypes if dtype in ('int', 'double', 'float')]).collect()
    
    # Extraer los nombres de las columnas y los valores de las medias
    columnas = df_medias[0].asDict().keys()
    valores_media = [row[col] for col in columnas for row in df_medias]
    
    # Crear un gráfico de barras horizontales con matplotlib
    plt.figure(figsize=(10, 6))
    plt.barh(list(columnas), valores_media, color='skyblue')
    
    # Añadir etiquetas y título al gráfico
    plt.title(f"Media de las columnas numéricas de '{column_value}'", fontsize=16)
    plt.xlabel("Media", fontsize=14)
    plt.ylabel("Columnas", fontsize=14)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
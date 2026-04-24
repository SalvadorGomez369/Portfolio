from data_analysis_process import extract
from data_analysis_process import transform
from data_analysis_process import procesar_datos_y_graficar as load

data = "C:/Users/nya/Documents/PythonP/Portfolio-main/Work_Projects/Data_analysis_projects/arbnb/Resources/Aemf1.csv"

#extract(data)
#transform(data)
load(data, "City", "Paris")
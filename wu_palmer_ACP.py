# Code written by Amanda Chirino-Perez; modified by Shruthi Sukumar 

import pandas as pd
import numpy as np
from nltk.corpus import wordnet as wn
import sys

# Función para calcular la similitud de Wu-Palmer entre dos palabras
def wu_palmer_similarity(word1, word2):
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)

    if not synsets1 or not synsets2:
        return None

    max_similarity = 0.0

    # Itera sobre los synsets de ambas palabras y calcula la similitud
    for synset1 in synsets1:
        for synset2 in synsets2:
            similarity = synset1.wup_similarity(synset2)
            if similarity is not None and similarity > max_similarity:
                max_similarity = similarity

    return max_similarity

# Verifica que se proporcionen las rutas de entrada y salida desde la línea de comandos
if len(sys.argv) != 3:
    print("Uso: python wp_PALABRAS_EXCEL_ruta_terminal.py ruta_entrada_excel ruta_salida_excel")
    sys.exit(1)

# Obtener rutas desde la línea de comandos
ruta_entrada = sys.argv[1]
ruta_salida = sys.argv[2]

# Leer el archivo Excel de entrada
df = pd.read_csv(ruta_entrada, header = 0)


# Inicializar la lista de resultados
resultados = []
similarity_matrix = np.zeros((len(df.index), len(df.index)))
# Iterar sobre las filas del DataFrame y calcular la similitud para cada par de palabras
for index, row in df.iterrows():
    
    for j_index, j_row in df.iterrows():
        word1, word2 = row['vocab'], j_row['vocab']
        similarity = wu_palmer_similarity(word1, word2)

        if similarity is not None:
            print(f"Similitud entre '{word1}' y '{word2}': {similarity}")

            # Agrega el resultado a la lista de resultados
            resultados.append({'Word1': word1, 'Word2': word2, 'Wu_Palmer_similarity': similarity})
            similarity_matrix[index, j_index] = similarity
        else:
            print(f"No se pudo calcular la similitud para '{word1}' y '{word2}'.")

# Después del bucle for, crea un DataFrame con los resultados
resultados_df = pd.DataFrame(resultados)

# Guarda el DataFrame en un archivo Excel en la ubicación especificada
resultados_df.to_csv(ruta_salida, index=False)
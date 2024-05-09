import tensorflow as tf
import pandas as pd

# Definindo os vetores
vetor1 = tf.constant([1, 2, 3], dtype=tf.float32)
vetor2 = tf.constant([2, 4, 6], dtype=tf.float32)

# Calculando a similaridade entre os vetores
produto_escalar = tf.reduce_sum(tf.multiply(vetor1, vetor2))
magnitude_vetor1 = tf.sqrt(tf.reduce_sum(tf.square(vetor1)))
magnitude_vetor2 = tf.sqrt(tf.reduce_sum(tf.square(vetor2)))
similaridade = produto_escalar / (magnitude_vetor1 * magnitude_vetor2)


print(similaridade, "resultado")

## Read CSV

data = pd.read_csv("testFile.csv", index_col="id", header=0)

print(data)

from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
import numpy as np 

def text_to_vector(text):
    tokens = word_tokenize(text)

    model = Word2Vec([tokens], window=5, min_count=1)
    # Convertir les mots de la chaîne de caractères en vecteurs
    vectors = [model.wv[word] for word in tokens]

    # Calculer la moyenne des vecteurs pour obtenir le vecteur de la chaîne de caractères
    vector = np.mean(vectors, axis=0)
    pod = np.mean(vector, axis=0)
    return pod



def fill_data(valeurs_entree, synopsis, titre, data):
    for valeur_entree in valeurs_entree:
        for i in data.columns:
            parts = i.rsplit('_', 1)
            if len(parts) == 2 and valeur_entree == parts[1]:
                row_index = 0  # assume there is only one row in the DataFrame
                column_name = i
                data.at[row_index, column_name] = 1

    data['Synopsis'] = synopsis
    data['Title'] = titre

    return data
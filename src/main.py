import db_connection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

conn = db_connection.connect()
cur = conn.cursor()

cur.execute('SELECT * FROM Movies')
movies = cur.fetchall()
movies_list = []
for movie in movies:
    # TODO: use id instead of title to be efficient in query
    title = movie[1]
    description = movie[2]
    genre = movie[3]
    movies_list.append([title, description + genre])

movies_list = np.array(movies_list)
count = CountVectorizer()
# create bag of words
bag_of_words = count.fit_transform(movies_list[:,1])
similarity_matrix = cosine_similarity(bag_of_words, bag_of_words)

def recommend_movie(title: str, movies_list: np.ndarray, similarity_matrix: np.ndarray) -> np.ndarray:
    '''Given a title, recommend movies
    :param title (str)
    :param movies_list (numpy.ndarray): list of movies' titles
    :param similarity_matrix (numpy.ndarray): cosine similarity of movies description
    '''
    # get index of movie
    for i, movie in enumerate(movies_list):
        if movie == title:
            break
    movies_vector = similarity_matrix[i]
    similarity = np.column_stack((movies_list[:,0], movies_vector))
    # get top 5 movies
    similarity = similarity[similarity[:,1].argsort()]
    return similarity[:,0][-6:-1]

if __name__ == "__main__":
    movies = recommend_movie('No Time to Die', movies_list, similarity_matrix)
    print(movies)

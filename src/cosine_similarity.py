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
    # currently using id
    title = movie[0]
    description = movie[2]
    genre = movie[3]
    main_genre = genre.split(',')[0]
    # TODO: put more weight on genre
    movies_list.append([title, description + genre + genre + main_genre])

movies_list = np.array(movies_list)
count = CountVectorizer()
# create bag of words for the descriptions
bag_of_words = count.fit_transform(movies_list[:,1])
similarity_matrix = cosine_similarity(bag_of_words, bag_of_words)
print(similarity_matrix)

def recommend_movie(title: str, movies_list: np.ndarray, similarity_matrix: np.ndarray) -> np.ndarray:
    '''Given a title, recommend movies
    :param title (str)
    :param movies_list (numpy.ndarray): list of movies' titles
    :param similarity_matrix (numpy.ndarray): cosine similarity of movies description
    '''
    cur.execute(f"SELECT id FROM Movies where title='{title}'")
    movie_id = cur.fetchone()
    # get index of movie
    for i, movie in enumerate(movies_list):
        if movie == movie_id:
            break
    movies_vector = similarity_matrix[i]
    similarity = np.column_stack((movies_list, movies_vector))
    # get top 5 movies
    similarity = similarity[similarity[:,1].argsort()]
    return similarity[:,0][-6:-1]

def clear_table():
    cur.execute('TRUNCATE RecommendedMovies')
    conn.commit()

def persist(movies_list: np.ndarray, similarity_matrix: np.ndarray):
    clear_table()
    query = 'INSERT INTO RecommendedMovies (movie_id, recommended_movie_id) VALUES \n'
    for i, movie in enumerate(movies_list):
        movie_vector = similarity_matrix[i]
        similarity = np.column_stack((movies_list, movie_vector))
        # get top 5 movies (see argsort, or https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column)
        similarity = similarity[similarity[:,1].argsort()]
        recommended_movies = similarity[:,0][-6:-1]
        for rm in recommended_movies:
            query += f'({movie}, {rm}),\n'
    # remove newline and comma at the end
    query = query[:-2]
    print(query)
    cur.execute(query)
    conn.commit()

if __name__ == "__main__":
    #movies = recommend_movie('Spider-Man: Far from Home', movies_list[:,0], similarity_matrix)
    #print(movies)
    persist(movies_list[:,0], similarity_matrix)

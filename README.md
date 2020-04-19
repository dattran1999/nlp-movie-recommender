# nlp-movie-recommender
Recommend movies based on the similarity in the descriptions. Descriptions are processed by transforming into bag of words. Then we use cosine similarity to calculate the how close are the descriptions. 

## Requirements
```
pip3 install -r requirements.txt
```

## Running the model
The current version only support reading the database from this [app](http://moviesengine.herokuapp.com/). <br />
Alternatively, you can create a database with the schema provided in the src folder, and populate it with some movie data (e.g. data from [IMDb](https://www.imdb.com/interfaces/)). Then navigate to src/db_connection.py to change the database connection.<br /> 
To run the code, 
```
python3 src/main.py
```

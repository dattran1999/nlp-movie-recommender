# nlp-movie-recommender
Recommend movies based on the similarity in description

## Requirements
```
pip3 install -r requirements.txt
```

## Running the model
The current version only support reading the database from this [app](http://moviesengine.herokuapp.com/). <br />
Alternatively, you can create a database with the schema provided in the src folder, and populate it with some movie data (e.g. data from [IMDb](https://www.imdb.com/interfaces/)).<br /> 
To run the code, 
```
python3 src/main.py
```
create table Movies (
    id integer generated always as identity,
    title text,
    summary text,
    genre text, -- a seperate table is better but...
    poster_url text,
    backdrop_url text,
    popularity float,
    rating float,
    isShowing boolean,
    primary key (id),
    unique (title, summary)
);

create table RecommendedMovies (
    movie_id integer,
    recommended_movie_id integer,
    foreign key (movie_id) references Movies(id),
    foreign key (recommended_movie_id) references Movies(id)
); 

create table Cinemas (
    id integer generated always as identity,
    name text,
    lat float,
    lng float,
    url text,
    long_name text,
    primary key (id)
);

create table Sessions (
    id integer generated always as identity,
    movie_id integer,
    cinema_id integer,
    ticket_url text,
    start_time timestamp,
    primary key (id),
    foreign key (movie_id) references Movies(id),
    foreign key (cinema_id) references Cinemas(id)
);

create table Users (
    id integer generated always as identity,
    email text,
    password text,
    primary key (id)
);

create table ShowingIn (
    id integer generated always as identity,
    movie_id integer,
    cinema_id integer,
    primary key (id),
    foreign key (movie_id) references Movies(id),
    foreign key (cinema_id) references Cinemas(id)
);

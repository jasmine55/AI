#coding:utf-8
import media
import koudaidy
import fresh_tomatoes

def get_movies():
    # get movie data list from http://www.kuyiyuan.cn
    movies_data = koudaidy.get_data()
    movies = []

    for movie_data in movies_data:
        if movie_data is not None:
            #config movie model with movie data
            movie = media.Movie(movie_data[1], movie_data[2], movie_data[0])
            movies.append(movie)
    return movies

def show_movies_page():
    movies = get_movies()
    fresh_tomatoes.open_movies_page(movies)

show_movies_page()

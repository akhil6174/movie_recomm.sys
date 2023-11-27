import streamlit as st
import requests
import pandas as pd
import pickle

def fetch_poster(id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=63b74d41047d033299c2b85d5223dfd2&language=en-US".format(id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    rec_movie=[]
    rec_id=[]
    movies=pickle.load(open('movies.pkl','rb'))
    movie_index=movies[movies['title']==movie].index[0]
    distances=pickle.load(open('similarity.pkl','rb'))[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]
    for i in movie_list:
        rec_movie.append(movies.iloc[i[0]].title)
        rec_id.append(movies.iloc[i[0]].id)
    return rec_movie,rec_id

movie_list=pickle.load(open('movies.pkl','rb'))['title'].values
st.title("Movie Recommendation System")
selected_movie_name = st.selectbox(
    'Which type movie would you like?',
movie_list)

if st.button("Recommend"):
    rec_movie,rec_id=recommend(selected_movie_name)
    col1, col2, col3,col4= st.columns(4)
    with col1:
        st.text(rec_movie[0])
        st.image(fetch_poster(rec_id[0]))
    with col2:
        st.text(rec_movie[1])
        st.image(fetch_poster(rec_id[1]))
    with col3:
        st.text(rec_movie[2])
        st.image(fetch_poster(rec_id[2]))
    with col4:
        st.text(rec_movie[3])
        st.image(fetch_poster(rec_id[3]))
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        st.text(rec_movie[5])
        st.image(fetch_poster(rec_id[5]))
    with col2:
        st.text(rec_movie[6])
        st.image(fetch_poster(rec_id[6]))
    with col3:
        st.text(rec_movie[7])
        st.image(fetch_poster(rec_id[7]))
    with col4:
        st.text(rec_movie[8])
        st.image(fetch_poster(rec_id[8]))

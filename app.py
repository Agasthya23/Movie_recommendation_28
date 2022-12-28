import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=55837420c664ac695063a44342aa40b1&language=en-US'.format(movie_id))
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original/"+poster_path
    return full_path
    


def get_recommendations(movie):
    #get the index of the movie
    movie_index=movie_data[movie_data['movie_name'] ==movie].index[0]
    distance=similarity[movie_index]
    #sort the list of movies based on the top 10 similarity scores keeping the index value intact using enumerate
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movie_poster=[]
    for i in movies_list:
        movie_id=movie_data.iloc[i[0]].movie_id
        recommended_movies.append(movie_data.iloc[i[0]].movie_name)
        #fetch poster from API
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_poster
    
st.set_page_config(layout="wide")

movies_dict=pickle.load(open("movies1.pkl","rb"))
movie_data=pd.DataFrame(movies_dict)
st.title('Movie Recommender system')

similarity=pickle.load(open("similarity1.pkl","rb"))

selected_movie = st.selectbox(
'Favorite 21st Century Hollywood Movie?',
movie_data['movie_name'].values)

if st.button('Recommend movies'):
    names,posters=get_recommendations(selected_movie)
    col1, col2, col3,col4,col5= st.columns(5)
    with col1:
        st.subheader(names[0])
        st.image(posters[0],width=None)
    with col2:
        st.subheader(names[1])
        st.image(posters[1],width=None)
    with col3:
        st.subheader(names[2])
        st.image(posters[2],width=None)
    with col4:
        st.subheader(names[3])
        st.image(posters[3],width=None)
    with col5:
        st.subheader(names[4])
        st.image(posters[4],width=None)
   
   


   
import pandas as pd
import requests
import streamlit as st
import pickle
import requests
from PIL import Image
from streamlit.components.v1 import html
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
import numpy as np


logo= Image.open('video-player.png')
st.set_page_config(page_title='The Movie Box', page_icon=logo)



def about():
    st.sidebar.markdown('---')
    st.sidebar.info('''
    ## The Movie Box
    ##### This content-based movie recommendation system uses cosine similarity to find the most similar movies from a given dataset for a chosen movie. It uses TMDB and IMDB APIs for implementing various functionalities.

    #Updated: 8 July, 2022''')

if __name__ == '__main__':
    st.sidebar.image('video-player.png', output_format='png')
    about()



#api_key=8cd35ad65338650a0fcfc899bc031f75
def fetch_poster(movie_id):
     response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8cd35ad65338650a0fcfc899bc031f75'.format(movie_id))
     data= response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def imdb_fetch(movie_id):
     response = requests.get(
          'https://api.themoviedb.org/3/movie/{}?api_key=8cd35ad65338650a0fcfc899bc031f75'.format(movie_id))
     data = response.json()
     imdbid = data['imdb_id']
     return imdbid


def recomment(movie):
     movie_index= movies[movies['title']== movie].index[0]
     distances= similarity[movie_index]
     movie_lisst= sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:11]
     #imdb= 'https://www.imdb.com/title/{}/'.format(imdb_fetch(movie_id))
     recom_imdb = []
     recommended_movies = []
     recommendedposters = []
     for i in movie_lisst:
          movie_id= movies.iloc[i[0]].id
          recommended_movies.append(movies.iloc[i[0]].title)
          recommendedposters.append(fetch_poster(movie_id))
          recom_imdb.append('https://www.imdb.com/title/{}/'.format(imdb_fetch(movie_id)))
     return recommended_movies, recommendedposters, recom_imdb


colT1,colT2,colT3,colT4 = st.columns([6,2,6,8])
with colT2:
     st.subheader('')

     st.image('video-player.png', output_format='png', width=70)
with colT3:
     st.header('The Movie Box')

colT1, colT2, colT3 = st.columns([3, 12, 3])
with colT2:
     st.subheader('A Movie Recommender System')

movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity= pickle.load(open('simalarity.pkl','rb'))
selectedname = st.selectbox(
     'Start typing your movie',
     (movies['title'].values))

if st.button('Recommend'):
          st.subheader('')
          recommended_movies1, recommendedposters1, link= recomment(selectedname)
          col1, col2, col3, col4, col5 = st.columns(5)
          with col1:
               st.write("[IMDB Page](%s)" % link[0])
               st.image(recommendedposters1[0])
               st.caption(recommended_movies1[0])
          with col2:
               st.write("[IMDB Page](%s)" % link[1])
               st.image(recommendedposters1[1])
               st.caption(recommended_movies1[1])
          with col3:
               st.write("[IMDB Page](%s)" % link[2])
               st.image(recommendedposters1[2])
               st.caption(recommended_movies1[2])
          with col4:
               st.write("[IMDB Page](%s)" % link[3])
               st.image(recommendedposters1[3])
               st.caption(recommended_movies1[3])
          with col5:
               st.write("[IMDB Page](%s)" % link[4])
               st.image(recommendedposters1[4])
               st.caption(recommended_movies1[4])

          st.markdown("""<hr style="height:5px;border:none;color:#c3073f;background-color:#c3073f;" /> """,
                      unsafe_allow_html=True)

          col1, col2, col3, col4, col5 = st.columns(5)
          with col1:
               st.write("[IMDB Page](%s)" % link[5])
               st.image(recommendedposters1[5])
               st.caption(recommended_movies1[5])
          with col2:
               st.write("[IMDB Page](%s)" % link[6])
               st.image(recommendedposters1[6])
               st.caption(recommended_movies1[6])
          with col3:
               st.write("[IMDB Page](%s)" % link[7])
               st.image(recommendedposters1[7])
               st.caption(recommended_movies1[7])
          with col4:
               st.write("[IMDB Page](%s)" % link[8])
               st.image(recommendedposters1[8])
               st.caption(recommended_movies1[8])
          with col5:
               st.write("[IMDB Page](%s)" % link[9])
               st.image(recommendedposters1[9])
               st.caption(recommended_movies1[9])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



def image(src_as_string, **style):
     return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
     return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):
     style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 80px; }
    </style>
    """

     style_div = styles(
          position="fixed",
          left=0,
          bottom=0,
          margin=px(0, 0, 0, 0),
          width=percent(100),
          color="black",
          text_align="center",
          height="auto",
          opacity=1
     )

     style_hr = styles(
          display="block",
          margin=px(0, 0, 0, 0),
          border_style="inset",
          border_width=px(2)
     )

     body = p(
          id='myFooter',
          style=styles(
               margin=px(0, 0, 0, 0),

               padding=px(5),
               font_size="0.8rem",
               color="rgb(51,51,51)"
          )
     )
     foot = div(
          style=style_div
     )(
          hr(
               style=style_hr
          ),
          body
     )

     st.markdown(style, unsafe_allow_html=True)

     for arg in args:
          if isinstance(arg, str):
               body(arg)

          elif isinstance(arg, HtmlElement):
               body(arg)

     st.markdown(str(foot), unsafe_allow_html=True)


     js_code = '''
    <script>
    function rgbReverse(rgb){
        var r = rgb[0]*0.299;
        var g = rgb[1]*0.587;
        var b = rgb[2]*0.114;

        if ((r + g + b)/255 > 0.5){
            return "rgb(49, 51, 63)"
        }else{
            return "rgb(250, 250, 250)"
        }

    };
    var stApp_css = window.parent.document.querySelector("#root > div:nth-child(1) > div > div > div");
    window.onload = function () {
        var mutationObserver = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    /************************当DOM元素发送改变时执行的函数体***********************/
                    var bgColor = window.getComputedStyle(stApp_css).backgroundColor.replace("rgb(", "").replace(")", "").split(", ");
                    var fontColor = rgbReverse(bgColor);
                    var pTag = window.parent.document.getElementById("myFooter");
                    pTag.style.color = fontColor;
                    /**************************************************/
                });
            });

            /**Element**/
            mutationObserver.observe(stApp_css, {
                attributes: true,
                characterData: true,
                childList: true,
                subtree: true,
                attributeOldValue: true,
                characterDataOldValue: true
            });
    }


    </script>
    '''
     html(js_code)


def footer():

     with open('video-player.png', 'rb') as f:
          img_logo = f.read()
     logo_cache = st.image(img_logo)
     logo_cache.empty()
     ######
     myargs = [
          "<> ",
          "with   ❤️   by ",
          link("http://www.linkedin.com/in/jasmeet-singh-sethi-67a01b17b", "@Jasmeet"),
     ]
     layout(*myargs)


if __name__ == "__main__":
     footer()

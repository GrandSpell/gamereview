from set_stream3 import setstream3
import streamlit as st
from gameids import get_gameid
titledix,titles=get_gameid()
import streamlit as st
st.set_page_config(
    page_title="reviews",
    layout="wide",
    initial_sidebar_state="expanded",
)

option1 = st.sidebar.selectbox(
    'ゲーム1を選択:',
    titles
)

option2 = st.sidebar.selectbox(
    'ゲーム2を選択:',
    titles
)

title1=option1
gameid1=titledix[title1]

title2=option2
gameid2=titledix[title2]


setstream3(gameid1,gameid2,title1,title2)



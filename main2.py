from set_stream3 import setstream3
import streamlit as st
from gameids import get_gameid
def main2():
    import streamlit as st

    titledix,titles=get_gameid()


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



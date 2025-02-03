from set_stream import setstream
from set_stream2 import setstream2
from gameids import get_gameid
titledix,titles=get_gameid()
import streamlit as st
st.set_page_config(
    page_title="reviews",
    layout="wide",
    initial_sidebar_state="expanded",
)
nowoption=titles[0]
option = st.sidebar.selectbox(
    'ゲームを選択:',
    titles
)
title=option
gameid=titledix[title]


section = st.sidebar.radio(
    "セクションを選択:",
    ("概要", "詳細表示")
)
# セクションに応じたコンテンツを表示
if section == "概要":
    setstream(gameid,title)
elif section == "詳細表示":
    setstream2(gameid,title)






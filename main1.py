from set_stream import setstream
from set_stream2 import setstream2
from gameids import get_gameid
def main1():
    import streamlit as st
    titledix,titles=get_gameid()

    option = st.sidebar.selectbox(
        "ゲームを選択:",
        titles
    )
    title=option
    gameid=titledix[title]


    section = st.sidebar.radio(
        "表示形式を選択",
        ("概要", "詳細表示")
    )
    # セクションに応じたコンテンツを表示
    if section == "概要":
        setstream(gameid,title)
    elif section == "詳細表示":
        setstream2(gameid,title)






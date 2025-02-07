from main1 import main1
from main2 import main2
import streamlit as st
st.set_page_config(
    page_title="ゲームレビュー情報可視化システム",
    layout="wide",
    initial_sidebar_state="expanded",
)

HIDE_ST_STYLE = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
"""

st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)

section = st.sidebar.radio(
    "モードを選択:",
    ("基本モード", "比較分析モード")
)
# セクションに応じたコンテンツを表示
if section == "基本モード":
    main1()
elif section == "比較分析モード":
    main2()





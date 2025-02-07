from main1 import main1
from main2 import main2
import streamlit as st
st.set_page_config(
    page_title="ゲームレビュー情報可視化システム",
    layout="wide",
    initial_sidebar_state="expanded",
)

section = st.sidebar.radio(
    "モードを選択:",
    ("基本モード", "比較分析モード")
)
# セクションに応じたコンテンツを表示
if section == "基本モード":
    main1()
elif section == "比較分析モード":
    main2()





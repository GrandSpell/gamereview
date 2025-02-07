def setstream(gameid, gamename):
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    import streamlit as st
    from PIL import Image
    gameid = str(gameid)
    headerfile = f"data/{gameid}/{gameid}_header.jpg"
    figfile1 = f"data/{gameid}/{gameid}_0_0.jpg"
    figfile2 = f"data/{gameid}/{gameid}_0_1.jpg"
    figfile3 = f"data/{gameid}/{gameid}_1_0.jpg"
    figfile4 = f"data/{gameid}/{gameid}_1_1.jpg"
    import pandas as pd
    df = pd.read_csv(f"data/{gameid}/{gameid}_result.csv")
    lix = []
    for j in range(len(df)):
        li1 = []
        for i in df.loc[j]:
            li1.append(i)
        lix.append(li1)
    reviews = []
    for i in range(len(lix)):
        review = str(lix[i][1])
        if review == "nan":
            review = ""
        reviews.append(review)

    title, img = st.columns([2, 1])
    title.title(gamename)
    image = Image.open(headerfile)
    img.image(image)

    def setsec(st, asptitle, aspects, figfile1, figfile2, reviews):
        # st.header(asptitle,divider=True)
        col1, col2 = st.columns([4, 5])
        # data = np.random.randn(6, 1)

        fig1 = Image.open(figfile1)
        col1.write("<center><strong>観点スコアレーダーチャート</strong></center>", unsafe_allow_html=True)
        col1.image(fig1)
        fig2 = Image.open(figfile2)
        col2.write("<center><strong>言及レビュー数</strong></center>", unsafe_allow_html=True)
        col2.image(fig2)

        def showtable(aspects, reviews):
            import pandas as pd
            pd.set_option('display.max_columns', None)  # 列の数に制限を設けない
            pd.set_option('display.expand_frame_repr', False)  # DataFrameを水平方向に折り返さない
            df = pd.DataFrame({'観点': aspects,
                               '要約': reviews})
            st.write("<strong>レビュー要約</strong>", unsafe_allow_html=True)
            st.table(df)

        showtable(aspects, reviews)

        # aspects2=["遊ぶ意義","没入感","成長感","好奇心","自由度"]
        # st.subheader("機能的観点")
        # showtable(aspects1,reviews1)
        # st.subheader("心理的観点")
        # showtable(aspects2,reviews2)

    asptitle1 = "機能的観点"
    aspects1 = ["操作のしやすさ", "難易度の適切さ", "進捗の明確さ", "目的の明確さ", "視聴覚の魅力"]
    asptitle2 = "心理的観点"
    aspects2 = ["遊ぶ意義", "没入感", "成長感の得やすさ", "好奇心への刺激", "自由度"]

    tabs = st.tabs(["機能的観点", "心理的観点"])
    with tabs[0]:
        setsec(st, asptitle1, aspects1, figfile1, figfile2, reviews[:5])

    with tabs[1]:
        setsec(st, asptitle2, aspects2, figfile3, figfile4, reviews[5:])

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:2rem;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)


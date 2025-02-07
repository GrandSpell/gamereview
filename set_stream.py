def setstream(gameid,gamename):
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib_fontja
    import streamlit as st
    from io import BytesIO
    from PIL import Image
    gameid=str(gameid)
    headerfile=f"data/{gameid}/{gameid}_header.jpg"
    figfile1=f"data/{gameid}/{gameid}_0_0.jpg"
    figfile2=f"data/{gameid}/{gameid}_0_1.jpg"
    figfile3=f"data/{gameid}/{gameid}_1_0.jpg"
    figfile4=f"data/{gameid}/{gameid}_1_1.jpg"
    import pandas as pd 
    df=pd.read_csv(f"data/{gameid}/{gameid}_result.csv")
    lix=[]
    for j in range(len(df)):
        li1=[]
        for i in df.loc[j]:
            li1.append(i)
        lix.append(li1)
    reviews=[]
    for i in range(len(lix)):
        review=str(lix[i][1])
        if review=="nan":
            review=""
        reviews.append(review)

        
    title, img= st.columns([3,1])
    title.title(gamename)
    image = Image.open(headerfile)
    img.image(image)
    
    def setsec(st,asptitle,aspects,figfile1,figfile2,reviews):
        #st.header(asptitle,divider=True)
        col1, col2 = st.columns([2,5])
        #data = np.random.randn(6, 1)

        # 値取得
        def setvalues(gameid, aspects):
            values = []
            df = pd.read_csv(f"data/{gameid}/{gameid}_negpos.csv")
            lix = {}
            getnum = 500
            for j in range(len(df)):
                li1 = []
                for i in df.loc[j]:
                    li1.append(i)
                lix[li1[0]] = [li1[1], li1[2], li1[3]]
            for aspect in aspects:
                values.append(
                    3 * (lix[aspect][0] - lix[aspect][1]) / (lix[aspect][0] + lix[aspect][1] + lix[aspect][2]))
            return values, lix

        # レーダーチャート作成
        def setchart(values,aspects):
            angles = np.linspace(0, 2 * np.pi, len(values) + 1)
            labels = aspects
            values.append(values[0])
            #fig = plt.figure(figsize=(6,4))
            fig = plt.figure()
            ax = fig.add_subplot(111, polar=True)
            ax.set_ylim([-3, 3])
            ax.plot(angles, values)
            ax.fill(angles, values, alpha=0.2)
            ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=16)
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            #ax.legend(bbox_to_anchor=(1.23, 1.1), loc='upper right', borderaxespad=0, fontsize=15)
            buf = BytesIO()
            #fig.savefig(buf, bbox_inches='tight', format="jpg")
            fig.savefig(buf, format="jpg")
            return buf

        # 棒グラフ作成
        def setbar(lix1, aspects):
            def setxposnegneu(lix, aspects):
                xpos, xneg, xneu, xposneg, xposnegneu = [], [], [], [], []
                for asp in aspects:
                    xpos.append(lix[asp][0])
                    xneg.append(lix[asp][1])
                    xneu.append(lix[asp][2])
                    xposneg.append((lix[asp][0] + lix[asp][1]))
                    n = str((lix[asp][0] + lix[asp][1] + lix[asp][2]))
                    xposnegneu.append(n)
                return xpos, xneg, xneu, xposneg, xposnegneu

            xpos1, xneg1, xneu1, xposneg1, xposnegneu1 = setxposnegneu(lix1, aspects)

            left = np.arange(len(aspects))  # numpyで横軸を設定
            labels = aspects

            width = 0.3
            #fig, ax = plt.subplots()
            fig = plt.figure()
            ax = fig.add_subplot()
            ax.set_xlim([0, 500])
            # ゲーム1
            ax.barh(labels, xpos1,  label="positive", align='center', color="blue")
            ax.barh(labels,xneg1,  left=xpos1, label="negative", align='center', color="red")
            aa = ax.barh(labels, xneu1,  left=xposneg1, label="neutral", align='center', color="gray")
            ax.bar_label(aa, labels=xposnegneu1, padding=5, fontsize=16)
            """
            ax.barh(left+width, xpos1, height=width, align='center',color="blue")
            ax.barh(left+width, xneg1, height=width, left=xpos1, align='center',color="red")
            aa=ax.barh(left+width, xneu1, height=width, left=xposneg1, align='center', color="gray")
            """

            #plt.yticks(left + width / 2, labels, fontsize=12)
            plt.yticks(labels, fontsize=16)
            ax.invert_yaxis()
            ax.legend()
            # plt.show()
            buf = BytesIO()
            fig.savefig(buf, bbox_inches='tight', format="jpg")
            #fig.savefig(buf, format="jpg")
            return buf

        values,lix=setvalues(gameid,aspects)

        

        col1.write("<center><strong>観点スコアレーダーチャート</strong></center>", unsafe_allow_html=True)
        col1.image(setchart(values,aspects))
        #fig1= Image.open(figfile1)
        #col1.image(fig1)
        #fig2= Image.open(figfile2)
        col1.write("<center><strong>観点レビュー数</strong></center>", unsafe_allow_html=True)
        col1.image(setbar(lix, aspects))
        #col1.image(fig2)
        
    
        def showtable(aspects,reviews):
            
            import pandas as pd
            pd.set_option('display.max_columns', None)  # 列の数に制限を設けない
            pd.set_option('display.expand_frame_repr', False)  # DataFrameを水平方向に折り返さない
            df = pd.DataFrame({'観点': aspects,
                               '要約': reviews})
            col2.write("<strong>レビュー要約</strong>", unsafe_allow_html=True)
            col2.table(df)

        showtable(aspects,reviews)
        
        #aspects2=["遊ぶ意義","没入感","成長感","好奇心","自由度"]
        #st.subheader("機能的観点")
        #showtable(aspects1,reviews1)
        #st.subheader("心理的観点")
        #showtable(aspects2,reviews2)
    asptitle1="機能的観点"
    aspects1=["操作のしやすさ","難易度の適切さ","進捗の明確さ","目的の明確さ","視聴覚の魅力"]
    asptitle2="心理的観点"
    aspects2=["遊ぶ意義","没入感","成長感の得やすさ","好奇心への刺激","自由度"]

    tabs = st.tabs(["機能的観点", "心理的観点"])
    with tabs[0]:
        setsec(st, asptitle1, aspects1, figfile1, figfile2, reviews[:5])

    with tabs[1]:
        setsec(st, asptitle2, aspects2, figfile3, figfile4, reviews[5:])

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:24px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)



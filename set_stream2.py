def setstream2(gameid,gamename):
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    import streamlit as st
    from PIL import Image
    from io import BytesIO
    gameid=str(gameid)
    headerfile=f"data/{gameid}/{gameid}_header.jpg"
    figfile1=f"data/{gameid}/{gameid}_0_0.jpg"
    figfile2=f"data/{gameid}/{gameid}_0_1.jpg"
    figfile3=f"data/{gameid}/{gameid}_1_0.jpg"
    figfile4=f"data/{gameid}/{gameid}_1_1.jpg"
    import pandas as pd 
    df=pd.read_csv(f"data/{gameid}/{gameid}_result2.csv")
    lix=[]
    for j in range(len(df)):
        li1=[]
        for i in df.loc[j]:
            li1.append(i)
        lix.append(li1)
        

    
    title, img = st.columns([3, 1])
    title.title(gamename)
    image = Image.open(headerfile)
    img.image(image)
    
    def setsec(st, aspect, lix):
        #st.header(asptitle,divider=True)
        #col1, col2 = st.columns([1, 1])
        #data = np.random.randn(6, 1)
        
        #fig1= Image.open(figfile1)
        #col1.image(fig1)
        #fig2= Image.open(figfile2)
        #col2.image(fig2)
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
            fig = plt.figure(figsize=(20, 1))
            ax = fig.add_subplot()
            ax.set_xlim([0, int(xposnegneu1[0])])
            # ゲーム1
            ax.barh(labels, xpos1, label="positive", align='center', color="blue")
            ax.barh(labels,xneg1, left=xpos1, label="negative", align='center', color="red")
            aa = ax.barh(labels, xneu1, left=xposneg1, label="neutral", align='center', color="gray")
            ax.bar_label(aa, labels=xposnegneu1, padding=5, fontsize=18)
            """
            ax.barh(left+width, xpos1, height=width, align='center',color="blue")
            ax.barh(left+width, xneg1, height=width, left=xpos1, align='center',color="red")
            aa=ax.barh(left+width, xneu1, height=width, left=xposneg1, align='center', color="gray")
            """

            #plt.yticks(left + width / 2, labels, fontsize=12)
            plt.yticks(labels, fontsize=18)
            ax.invert_yaxis()
            #ax.legend()
            # plt.show()
            buf = BytesIO()
            fig.savefig(buf, format="jpg")
            #fig.savefig(buf, format="jpg")
            return buf

        st.write("<center><strong>観点レビュー割合</strong></center>", unsafe_allow_html=True)
        aspects=[aspect]
        values, lix1=setvalues(gameid, aspects)
        st.image(setbar(lix1, aspects))
    
        def showtable(reviews):
            import pandas as pd
            #st.subheader(reviews[0],divider=True)
            pd.set_option('display.max_columns', None)  # 列の数に制限を設けない
            pd.set_option('display.expand_frame_repr', False)  # DataFrameを水平方向に折り返さない
            poss=['肯定意見','否定意見','中立意見']
            for i in range(3):
                pos=poss[i]
                if str(reviews[i+1])!="nan":
                    review=reviews[i+1].split("- ")
                    review=review[1:]
                else:
                    review=[]
                df = pd.DataFrame({pos: review})
                st.table(df)
        showtable(lix)
        
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

    css = '''
    <style>
        .stTabs[0] [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:24px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

    with tabs[0]:
        tabs2 = st.tabs(aspects1)
        with tabs2[0]:
            setsec(st, aspects1[0], lix[0])
        with tabs2[1]:
            setsec(st, aspects1[1], lix[1])
        with tabs2[2]:
            setsec(st, aspects1[2], lix[2])
        with tabs2[3]:
            setsec(st, aspects1[3], lix[3])
        with tabs2[4]:
            setsec(st, aspects1[4], lix[4])

    with tabs[1]:
        tabs2 = st.tabs(aspects2)
        with tabs2[0]:
            setsec(st, aspects2[0], lix[5])
        with tabs2[1]:
            setsec(st, aspects2[1], lix[6])
        with tabs2[2]:
            setsec(st, aspects2[2], lix[7])
        with tabs2[3]:
            setsec(st, aspects2[3], lix[8])
        with tabs2[4]:
            setsec(st, aspects2[4], lix[9])

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:24px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)



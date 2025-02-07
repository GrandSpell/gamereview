def setstream3(gameid1,gameid2,gamename1,gamename2):
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    from japanize-matplotlib import japanize_matplotlib
    import streamlit as st
    from PIL import Image
    import pandas as pd
    from io import BytesIO
    
    def setgame(num,gamename,headerfile):
        col,title,img=st.columns([1, 6, 2])
        col.title(f"{num}:")
        title.title(gamename)
        image = Image.open(headerfile)
        img.image(image)

    def getchart(gameid1,gameid2,aspects):
        #値取得
        def setvalues(gameid,aspects):
            values = []
            df=pd.read_csv(f"data/{gameid}/{gameid}_negpos.csv")
            lix={}
            getnum=500
            for j in range(len(df)):
                li1=[]
                for i in df.loc[j]:
                    li1.append(i)
                lix[li1[0]]=[li1[1],li1[2],li1[3]]
            for aspect in aspects:
                values.append(3*(lix[aspect][0]-lix[aspect][1])/(lix[aspect][0]+lix[aspect][1]+lix[aspect][2]))
            return values,lix
    
        #レーダーチャート作成
        def setchart(values1,values2,aspects):
            angles = np.linspace(0, 2 * np.pi, len(values1) + 1)
            labels = aspects
            values1.append(values1[0])
            values2.append(values2[0])
            fig = plt.figure()
            ax = fig.add_subplot(111, polar = True)
            ax.set_ylim([-3, 3])
            ax.plot(angles, values1,label="ゲーム1")
            ax.plot(angles, values2,label="ゲーム2")
            ax.fill(angles, values1, alpha=0.2)
            ax.fill(angles, values2, alpha=0.2)
            ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=15)
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            ax.legend(bbox_to_anchor=(1.23, 1.1), loc='upper right', borderaxespad=0, fontsize=15)
            buf = BytesIO()
            fig.savefig(buf, bbox_inches='tight', format="jpg")
            return buf
    
        #棒グラフ作成
        def setbar(lix1,lix2,aspects):
            def setxposnegneu(lix,aspects):
                xpos,xneg,xneu,xposneg,xposnegneu=[],[],[],[],[]
                for asp in aspects:
                    xpos.append(lix[asp][0]/5)
                    xneg.append(lix[asp][1]/5)
                    xneu.append(lix[asp][2]/5)
                    xposneg.append((lix[asp][0]+lix[asp][1])/5)
                    n=str((lix[asp][0]+lix[asp][1]+lix[asp][2])/5).split(".")
                    if n[1]=="0":
                        n=n[0]
                    else:
                        n=n[0]+"."+n[1]
                    xposnegneu.append(n)
                return xpos,xneg,xneu,xposneg,xposnegneu
            xpos1,xneg1,xneu1,xposneg1,xposnegneu1=setxposnegneu(lix1,aspects)
            xpos2,xneg2,xneu2,xposneg2,xposnegneu2=setxposnegneu(lix2,aspects)
        
            left = np.arange(len(aspects))  # numpyで横軸を設定
            labels = aspects
            
            width = 0.3
            
            fig, ax = plt.subplots()
            ax.set_xlim([0,100])
            #ゲーム1
            ax.barh(left, xpos1, height=width, label="positive", align='center',color="blue")
            ax.barh(left, xneg1, height=width, left=xpos1, label="negative", align='center',color="red")
            aa=ax.barh(left, xneu1, height=width, left=xposneg1, label="neutral", align='center', color="gray")
            ax.bar_label(aa, labels=xposnegneu1,padding=5,fontsize=10)
            #ゲーム2
            ax.barh(left+width, xpos2, height=width, align='center',color="blue")
            ax.barh(left+width, xneg2, height=width, left=xpos2, align='center',color="red")
            aa=ax.barh(left+width, xneu2, height=width, left=xposneg2, align='center', color="gray")
            ax.bar_label(aa, labels=xposnegneu2,padding=5,fontsize=10)
            plt.yticks(left + width/2, labels, fontsize=12)
            ax.invert_yaxis()
            ax.legend()
            #plt.show()
            buf = BytesIO()
            fig.savefig(buf, bbox_inches='tight', format="jpg")
            return buf
            
        values1,lix1=setvalues(gameid1,aspects)
        values2,lix2=setvalues(gameid2,aspects)
        col1,col2=st.columns([2,3])
        #col1.write("##### 観点スコアレーダーチャート")
        col1.write("<center><strong>観点スコアレーダーチャート</strong></center>", unsafe_allow_html=True)
        col2.write("<center><strong>言及レビュー数(ゲーム1:上、ゲーム2:下)</strong></center>", unsafe_allow_html=True)
        col1.image(setchart(values1,values2,aspects))
        col2.image(setbar(lix1,lix2,aspects)) 

    headerfile1=f"data/{gameid1}/{gameid1}_header.jpg"
    headerfile2=f"data/{gameid2}/{gameid2}_header.jpg"
    setgame(1,gamename1,headerfile1)
    setgame(2,gamename2,headerfile2)
    tabs = st.tabs(["機能的観点", "心理的観点"])
    with tabs[0]:
        aspects = ["操作のしやすさ", "難易度の適切さ", "進捗の明確さ", "目的の明確さ", "視聴覚の魅力"]
        getchart(gameid1, gameid2, aspects)

    with tabs[1]:
        aspects = ["遊ぶ意義", "没入感", "成長感の得やすさ", "好奇心への刺激", "自由度"]
        getchart(gameid1, gameid2, aspects)
    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:24px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)



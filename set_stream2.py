def setstream2(gameid,gamename):
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    import streamlit as st
    from PIL import Image
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
        

    
    title, img = st.columns([1, 1])
    title.title(gamename)
    image = Image.open(headerfile)
    img.image(image)
    
    def setsec(st,asptitle,aspects,figfile1,figfile2,lix):
        st.header(asptitle,divider=True)
        col1, col2 = st.columns([1, 1])
        #data = np.random.randn(6, 1)
        
        fig1= Image.open(figfile1)
        col1.image(fig1)
        fig2= Image.open(figfile2)
        col2.image(fig2)
        
    
        def showtable(reviews):
            import pandas as pd
            st.subheader(reviews[0],divider=True)
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
        for i in range(5):
            reviews=lix[i]
            showtable(reviews)
        
        #aspects2=["遊ぶ意義","没入感","成長感","好奇心","自由度"]
        #st.subheader("機能的観点")
        #showtable(aspects1,reviews1)
        #st.subheader("心理的観点")
        #showtable(aspects2,reviews2)
    asptitle1="機能的観点"
    aspects1=["操作のしやすさ","難易度の適切さ","進捗の明確さ","目的の明確さ","視聴覚の魅力"]
    asptitle2="心理的観点"
    aspects2=["遊ぶ意義","没入感","成長感の得やすさ","好奇心への刺激","自由度"]
    setsec(st,asptitle1,aspects1,figfile1,figfile2,lix[:5])
    setsec(st,asptitle2,aspects2,figfile3,figfile4,lix[5:])

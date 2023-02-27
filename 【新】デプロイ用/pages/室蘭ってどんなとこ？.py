import streamlit as st
import numpy as np
import pandas as pd

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">室蘭の名前の由来</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:black; font-size: 20px;">「室蘭」の語源は、アイヌ語の「モ・ルエラニ」という言葉がもとになっており、“小さな・下り路”という意味です。室蘭港を中心にすり鉢状の地形をしており、名前の表すとおり、とても坂道の多いまちです。</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">有名スポット</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:black; font-size: 20px;">室蘭は北海道有数の工業都市であり、自然も豊かで、ここでしか見られない「工場夜景」を楽しむ事が出来ます。</p>',
            unsafe_allow_html=True)

# 「工場夜景」の画像を複数表示
num = 2
lcol = []
col = st.columns(num)

for i in list(range(0, num, 1)):
    with col[i]:
        st.header("")
        st.image(str(i+1)+".png", use_column_width=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">食べ物</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:black; font-size: 20px;">室蘭のご当地グルメといえば「室蘭やきとり」や「室蘭カレーラーメン」。室蘭やきとりは鶏肉ではなく豚肉を使用するのが定番で、豚肉と玉ねぎの串焼きをタレで洋ガラシにつけて食べるのが室蘭流。</p>',
            unsafe_allow_html=True)

# 「食べ物」の画像を複数表示
num = 2
lcol = []
col = st.columns(num)

for i in list(range(0, num, 1)):
    with col[i]:
        st.header("")
        st.image(str(i+1)+".jpg", use_column_width=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">子育て支援</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:black; font-size: 20px;">室蘭市では、子育て支援も充実しており、子育て世代が安心して働く事が出来るよう学童保育の価格もとても良心的なものとなっています。（月額：600円程）また、「室蘭市生涯学習センターきらん」などの複合公共施設もあり、季節や天候に関係なく小さな子供も遊ばせる事が出来ます。</p>',
            unsafe_allow_html=True)

# 「きらん」の画像を複数表示
col1, col2 = st.columns(2)

with col1:
    st.header("")
    st.image("kirangaikan.jpg", use_column_width=True)

with col2:
    st.header("")
    st.image("kiran.jpg", use_column_width=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">室蘭の口コミ</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:black; font-size: 20px;">室蘭市の口コミは以下のリンクからご覧になれます。</p>',
            unsafe_allow_html=True)

# 「室蘭の口コミ」リンク
st.write('ここをクリック ⇒　', 'https://sumaity.com/town/hokkaido/muroran/review/', '')
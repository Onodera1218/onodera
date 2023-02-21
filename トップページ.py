#!/usr/bin/env python
# coding: utf-8

# In[30]:
import streamlit as st
import numpy as np
import pandas as pd

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:RoyalBlue; font-size: 40px;">室蘭市に住みたいあなたへ</p>', unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Black; font-size: 20px;">← 気になる方は 【物件検索】 へ</p>', unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Black; font-size: 20px;">←  室蘭について知りたい方は【室蘭ってどんなとこ？】 へ</p>', unsafe_allow_html=True)


def main():
    # 東京のランダムな経度・緯度を生成する
    data = {
        'lat': np.random.randn(1) / 10000 + 42.32,
        'lon': np.random.randn(1) / 10000 + 140.97,
    }
    map_data = pd.DataFrame(data)
    # 地図に散布図を描く
    st.map(map_data)
if __name__ == '__main__':
    main()

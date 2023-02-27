#!/usr/bin/env python
# coding: utf-8

# In[30]:
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Salmon; font-size: 40px;">室蘭市に住みたいあなたへ</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Black; font-size: 20px;">← 気になる方は 【物件検索】 へ</p>',
            unsafe_allow_html=True)

st.markdown('<p style="font-family:HGP創英角ﾎﾟｯﾌﾟ体; color:Black; font-size: 20px;">←  室蘭について知りたい方は【室蘭ってどんなとこ？】 へ</p>', unsafe_allow_html=True)

# 北海道の画像を表示
img = Image.open('map-hokkaido.png')
st.image(img, caption='', width=600)

# %%
#

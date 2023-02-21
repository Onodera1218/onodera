import streamlit as st
import numpy as np
import pandas as pd

import gspread
from google.oauth2.service_account import Credentials

st.info('条件で絞り込む')
st.text_input('入居可能時期')
st.selectbox('借家', ('普通', '定期'))
st.selectbox('部屋の広さ', ('下限なし', '10畳'))
st.text_input('職場の住所（近いところを探す）')
st.selectbox('空きのある保育所（10km圏内）', ('希望', '不要'))


cost = st.slider('家賃（万/月）?', 0, 30, 5)

direction = st.radio(
    "方位",
    ('南', '北', '東','西'))

options = st.multiselect(
    '建物設備',
    ['駐車場', 'バルコニー', 'エレベーター', 'オール電化','公園1km以内', 'スーパー1km以内'])


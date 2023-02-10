#!/usr/bin/env python
# coding: utf-8

# In[30]:



import streamlit as st

# In[31]:

# %%
st.success('条件で絞り込む')
# %%
st.text_input('入居可能時期')
st.selectbox('借家', ('普通', '定期'))
st.selectbox('部屋の広さ', ('下限なし', '10畳'))
st.text_input('職場の住所（近いところを探す）')
st.selectbox('空きのある保育所（10km圏内）', ('希望', '不要'))

# %%
st.success('12件　見つかりました。')
# %%
st.button('× キャンセル')
st.button('🔍 この条件でさがす')
# %%

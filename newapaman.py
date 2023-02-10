#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd  # pandasを使えるようにする
import numpy as np
import streamlit as st
import subprocess
import pandas as pd
from gspread_dataframe import set_with_dataframe
import json
from google.oauth2.service_account import Credentials
import gspread
import requests
from bs4 import BeautifulSoup


# In[31]:


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
header = {'User-Agent': user_agent}

url = 'https://www.chintaistyle.jp/pref/01/area_12293_list.html?page=0&disp=10&item=aprm&ar=asc'
res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, "html.parser")


# In[32]:


for page in range(1, 5):
    url = 'https://www.chintaistyle.jp/pref/01/area_12293_list.html?page={}'.format(
        page)
    target_url = url.format(page)
    print(target_url)


# In[33]:


soup.find_all('li')


# In[34]:


data = soup.find_all('li', {'class': 'estate-parent-rightBottomUL1_LI1'})


# In[35]:


for li_tag in soup.find_all('li', {'class': 'estate-parent-rightBottomUL1_LI1'}):
    print(li_tag.text)


# In[36]:


#get_ipython().system(' pip install gspread')


# In[37]:


#get_ipython().system(' pip install oauth2client')


# In[38]:


# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file(
    "quantum-tracker-374208-b7f3ed2fadb7.json", scopes=scope)
# OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)
# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = '16a7uIbpFfWT0mluRNR17jdHStS-KH6riqufvZAufJSo'
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)


# In[39]:


# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)
# シートの一覧を取得する。（リスト形式）
worksheets = workbook.worksheets()
print(worksheets)
# シートを開く
worksheet = workbook.worksheet('12/7-13_スクレイピング')
# セルA1に”test value”という文字列を代入する。
worksheet.update_cell(2, 6, 'test')


# In[40]:


# In[41]:


url = 'https://www.chintaistyle.jp/pref/01/area_12293_list.html'  # サイトのURLを取得
# ユーザーエージェントを設定
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
header = {"User-Agent": user_agent}

res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')  # BeautifulSoupでresの中身を整える


# In[42]:


address_list = []
for li_tag in soup.find_all('li', {'class': 'estate-parent-rightBottomUL1_LI1'}):
    print(li_tag.text)
    address_list.append(li_tag.text)


# In[43]:


# データフレームに変換
name_df = pd.DataFrame({'住所': address_list})
print(name_df)


# In[44]:


# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file(
    "quantum-tracker-374208-b7f3ed2fadb7.json", scopes=scope)
# OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)
# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = '16a7uIbpFfWT0mluRNR17jdHStS-KH6riqufvZAufJSo'
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)


# In[45]:


#get_ipython().system(' pip install gspread-dataframe')


# In[46]:


set_with_dataframe(workbook.worksheet('12/7-13_スクレイピング'),
                   name_df, row=1, col=6, include_index=True)


# In[47]:


#get_ipython().system(' pip install beautifulsoup4 lxml html5lib')


# In[48]:


# In[49]:


url = 'https://www.city.muroran.lg.jp/main/org4510/akijyoukyou.html'
# 読み込むサイトのURLを格納
data = pd.read_html(url, header=0)
data[0].head()


# In[50]:


data[0].tail()


# In[51]:


set_with_dataframe(workbook.worksheet('12/7-13_スクレイピング'),
                   data[0], row=23, col=1, include_index=True)


# In[ ]:

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

import streamlit as st

st.title('💰 我的零用錢記帳本')

records = []   # 用一個 list 來存所有記錄

date = st.date_input('日期')
kind = st.radio('收入還是支出？', ['支出', '收入'], horizontal=True)
category = st.selectbox('類別', ['飲食', '交通', '娛樂', '文具', '零用錢', '其他'])
item = st.text_input('項目', placeholder='例如：珍奶')
amount = st.number_input('金額', min_value=0, step=10)

if st.button('記下來'):
    records.append({'日期': str(date), '收支': kind, '類別': category,
                    '項目': item, '金額': amount})
    st.success('記好了！')

st.write('目前共有', len(records), '筆記錄')
st.write(records)

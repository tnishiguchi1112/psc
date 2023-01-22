import streamlit as st
import datetime

st.title('週報作成')

d_start = st.date_input(
    "週報期間（始まりを選択）",
    datetime.date.today())

st.write('始まり:', d_start)

dt = datetime.timedelta(days=7)

d_end = d_start + dt

st.write('終わり:', d_end)

st.write('件名：西日本BPO1課_西口崇登_PJ週報_', d_end)

st.write('本文:')
st.write('各位')
st.write('')
st.write('おつかれさまです。西日本BPO1課の西口です。')
st.write('今週の週報を送らせて頂きます。')
st.write('')
st.write('＜週報期間＞')
st.write(d_start, '～', d_end)
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')






import streamlit as st
import datetime

st.title('週報作成')

d_start = st.sidebar.date_input(
    "週報期間（始まりを選択）",
    datetime.date.today())
d_start_str = str(d_start)
d_start_str_slash = d_start_str.replace('-', '/') 

d_end = d_start + datetime.timedelta(days=7)
d_end_str = str(d_end)
d_end_str_slash = d_end_str.replace('-', '/') 
st.write('')

st.write('件名：西日本BPO1課_西口崇登_PJ週報_', d_end_str_slash)
st.write('')

st.write('本文:（バラメータ入力後、下記をコピーしてください）')
st.write('各位')
st.write('')

st.write('おつかれさまです。西日本BPO1課の西口です。')
st.write('今週の週報を送らせて頂きます。')
st.write('')

st.write('＜週報期間＞')
st.write(d_start_str_slash, '～', d_end_str_slash)
st.write('')

st.write('＜PJ名＞')
st.write('オプテージ様向けクラウド・ホスティングサービスに関する運用委託')
st.write('')

st.write('＜今週の主な業務内容＞')
st.write('1.各種資料作成')
st.write('　・各種機器設定変更手順書')

st.write('2.設定変更作業')

device = st.sidebar.selectbox( #multiselect[]
    '設定変更機器を選択',
    ('FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'レガシー'))
st.write('・', device)

st.write('3.その他')

other = st.sidebar.selectbox( #multiselect[]
    'その他業務を選択',
    ('チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
st.write('・', other)
st.write('')

workday = st.sidebar.slider('稼働日数', 0, 31, 20)
workday_str = str(workday)
holiday = st.sidebar.slider('休暇取得日数', 0, 31, 0)
holiday_str = str(holiday)
worktime = workday * 8
worktime_str = str(worktime)
overtime = st.sidebar.time_input('平日深夜時間', datetime.time(0, 00))
overtime_str = str(overtime)
st.write('＜', d_end_str_slash[5:7], '月稼働実績＞')
st.write('■稼働日：', workday_str, '日', '休暇取得：', holiday_str, '日', '当月想定稼働時間：', worktime_str, '時間(内平日深夜', overtime_str[0:5], '時間)')
st.write('')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
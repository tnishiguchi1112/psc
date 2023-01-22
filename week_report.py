import streamlit as st
import datetime

# git init
# git remoto add origin https://github.com/tnishiguchi1112/psc.git
# git add .
# git commit -m '1st commit'
# git push origin main

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

st.write('本文:（左のスライダーを展開し、パラメータ入力後、下記をコピーしてください）')
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
overnighttime = st.sidebar.time_input('平日深夜時間', datetime.time(0, 00))
overnighttime_str = str(overnighttime)
st.write('＜', d_end_str_slash[5:7], '月稼働実績＞')
st.write('■稼働日：', workday_str, '日', '休暇取得：', holiday_str, '日', '当月想定稼働時間：', worktime_str, '時間(内平日深夜', overnighttime_str[0:5], '時間)')
st.write('')

st.write('＜', d_end_str_slash[5:7], '月超過報告＞')
overtime = st.sidebar.time_input('常駐先残業時間', datetime.time(0, 00))
overtime_str = str(overtime)
st.write('■', overtime_str[0:5], '/常駐先業務のため')
overtime_mtg = st.sidebar.time_input('BPO事業部MTGによる残業時間', datetime.time(0, 00))
overtime_mtg_str = str(overtime_mtg)
st.write('■', overtime_mtg_str[0:5], '/BPO事業部ミーティングのため')
st.write('')

st.write('＜休暇取得実績＞')
premiumday = st.sidebar.checkbox('プレミアムデー取得済み')
holiday_take = st.sidebar.checkbox('有給休暇済み')

if premiumday:
    premiumday_take = st.sidebar.date_input(
    "プレミアムデー取得日を選択",
    datetime.date.today())
    premiumday_take_str = str(premiumday_take)
    premiumday_take_str_slash =premiumday_take_str.replace('-', '/') 
    st.write('■', premiumday_take_str_slash[5:10], 'プレミアムデー')
else:
    st.write('■なし')

if holiday_take:
    holiday_take_take = st.sidebar.date_input(
    "有給休暇取得日を選択",
    datetime.date.today())
    holiday_take_take_str = str(holiday_take_take)
    holiday_take_take_str_slash =holiday_take_take_str.replace('-', '/') 
    st.write('■', holiday_take_take_str_slash[5:10], '有給休暇')
else:
    st.write('■なし')
st.write('')




st.write('＜休暇取得予定＞')
premiumday_schedule = st.sidebar.checkbox('プレミアムデー取得予定')
holiday_schedule = st.sidebar.checkbox('有給休暇予定')

if premiumday_schedule:
    premiumday_schedule_take = st.sidebar.date_input(
    "プレミアムデー取得予定日を選択",
    datetime.date.today())
    premiumday_schedule_take_str = str(premiumday_schedule_take)
    premiumday_schedule_take_str_slash =premiumday_schedule_take_str.replace('-', '/') 
    st.write('■', premiumday_schedule_take_str_slash[5:10], 'プレミアムデー')
else:
    st.write('■なし')

if holiday_schedule:
    holiday_schedule = st.sidebar.date_input(
    "有給休暇取得日を選択",
    datetime.date.today())
    holiday_schedule_str = str(holiday_schedule)
    holiday_schedule_str_slash =holiday_schedule_str.replace('-', '/') 
    st.write('■', holiday_schedule_str_slash[5:10], '有給休暇')
else:
    st.write('■なし')


st.write('')





#■1月18日プレミアムデー





st.write('＜休日出勤実績＞')
st.write('')
st.write('＜休日出勤予定＞')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('＜有給休暇取得状況＞')
st.write('')

st.write('＜資格取得報告＞')
st.write('■5日中4日取得済（残6日）')
st.write('')

st.write('＜トピックス、連絡事項、その他＞')
st.write('■Python 3 エンジニア認定基礎試験/2月予定/50%')
st.write('基本情報技術者試験/4月予定/20%')

st.write('以上、よろしくお願いいたします。')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.write('改善点：業務内容を複数選択できるようにする、稼働日数を平日から計算するようにする、前回入力値を維持するにわ？、先頭に空白をいれる、超過報告を追加できるようにする（その他の項目についても例外を入力できるようにする）、休暇取得や休日出勤を複数選択でき、1つも存在しないときは「■なし」の出力を1つにする')
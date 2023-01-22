import streamlit as st
import datetime

# git init
# git remoto add origin https://github.com/tnishiguchi1112/psc.git
# git add .
# git commit -m '1st commit'
# git push origin main

st.title('週報作成')


#週報期間（開始）
d_start = st.sidebar.date_input(
    "週報期間（始まりを選択）",
    datetime.date.today())
d_start_str = str(d_start)
d_start_str_slash = d_start_str.replace('-', '/') 
st.sidebar.write('')


#週報期間（終了）
d_end = d_start + datetime.timedelta(days=7)
d_end_str = str(d_end)
d_end_str_slash = d_end_str.replace('-', '/') 
st.write('')


#件名
st.write('件名：西日本BPO1課_西口崇登_PJ週報_', d_end_str_slash)
st.write('')


#本文
st.write('本文:（左のスライダーを展開し、パラメータ入力後、下記をコピーしてください）')
st.write('')


#挨拶文
st.write('各位')
st.write('')
st.write('おつかれさまです。西日本BPO1課の西口です。')
st.write('今週の週報を送らせて頂きます。')
st.write('')


#週報期間
st.write('＜週報期間＞')
st.write(d_start_str_slash, '～', d_end_str_slash)
st.write('')


#プロジェクト名
st.write('＜PJ名＞')
st.write('オプテージ様向けクラウド・ホスティングサービスに関する運用委託')
st.write('')


#業務内容
st.write('＜今週の主な業務内容＞')

#1
st.write('1.各種資料作成')
st.write('　・各種機器設定変更手順書')

#2
st.write('2.設定変更作業')
device = st.sidebar.selectbox( #multiselect[]
    '設定変更機器を選択',
    ('なし', 'FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'レガシー'))
st.write('・', device)

device2 = st.sidebar.checkbox('設定変更機器を追加')
if device2:
    device2 = st.sidebar.selectbox( #multiselect[]
    '設定変更機器2を選択',
    ('FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'レガシー'))
    st.write('・', device2)
else:
    pass
st.sidebar.write('')

#3
st.write('3.その他')
other = st.sidebar.selectbox( #multiselect[]
    'その他業務を選択',
    ('なし', 'チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
st.write('・', other)
other2 = st.sidebar.checkbox('その他業務を追加')
if other2:
    other2 = st.sidebar.selectbox( #multiselect[]
    'その他業務2を選択',
    ('チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
    st.write('・', other2)
else:
    pass
st.write('')
st.sidebar.write('')


#稼働実績
workday = st.sidebar.slider('稼働日数', 0, 31, 20)
workday_str = str(workday)
st.sidebar.write('')
holiday = st.sidebar.slider('休暇取得日数', 0, 31, 0)
holiday_str = str(holiday)
st.sidebar.write('')
worktime = workday * 8
worktime_str = str(worktime)
overnighttime = st.sidebar.time_input('平日深夜時間', datetime.time(0, 00))
overnighttime_str = str(overnighttime)
st.sidebar.write('')
st.write('＜', d_end_str_slash[5:7], '月稼働実績＞')
st.write('■稼働日：', workday_str, '日', '休暇取得：', holiday_str, '日', '当月想定稼働時間：', worktime_str, '時間(内平日深夜', overnighttime_str[0:5], '時間)')
st.write('')

st.write('＜', d_end_str_slash[5:7], '月超過報告＞')
overtime = st.sidebar.time_input('常駐先残業時間', datetime.time(0, 00))
overtime_str = str(overtime)
st.sidebar.write('')
st.write('■', overtime_str[0:5], '/常駐先業務のため')
overtime_mtg = st.sidebar.time_input('BPO事業部MTGによる残業時間', datetime.time(0, 00))
overtime_mtg_str = str(overtime_mtg)
st.write('■', overtime_mtg_str[0:5], '/BPO事業部ミーティングのため')
st.write('')
st.sidebar.write('')


#休暇取得実績
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


#休暇取得予定
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
    holiday_schedule_take = st.sidebar.date_input(
    "有給休暇取得予定日を選択",
    datetime.date.today())
    holiday_schedule_take_str = str(holiday_schedule_take)
    holiday_schedule_take_str_slash =holiday_schedule_take_str.replace('-', '/') 
    st.write('■', holiday_schedule_take_str_slash[5:10], '有給休暇')
else:
    st.write('■なし')
st.write('')
st.sidebar.write('')


#休日出社実績
st.write('＜休日出勤実績＞')

holiday_work = st.sidebar.checkbox('休日出社実績（全体研修のみ）')
if holiday_work:
    holiday_work_take = st.sidebar.date_input(
    "休日出社日程",
    datetime.date.today())
    holiday_work_take_str = str(holiday_work_take)
    holiday_work_take_str_slash =holiday_work_take_str.replace('-', '/') 
    st.write('■', holiday_work_take_str_slash[5:10], '全体研修のため')
else:
    st.write('■なし')
st.write('')


#休日出勤予定
st.write('＜休日出勤予定＞')
holiday_work_schedule = st.sidebar.checkbox('休日出社予定（全体研修のみ）')
if holiday_work_schedule:
    holiday_work_schedule = st.sidebar.date_input(
    "休日出社予定日程",
    datetime.date.today())
    holiday_work_schedule_str = str(holiday_work_schedule)
    holiday_work_schedule_str_slash =holiday_work_schedule_str.replace('-', '/') 
    st.write('■', holiday_work_schedule_str_slash[5:10], '全体研修のため')
else:
    st.write('■なし')
st.write('')
st.sidebar.write('')


#有給休暇取得状況
st.write('＜有給休暇取得状況＞')
all_paid = st.sidebar.slider('総有給数', 0, 40, 10)
all_paid_str = str(all_paid)
st.sidebar.write('')
paid = st.sidebar.slider('有給取得数', 0, 40, 0)
paid_str = str(paid)
st.sidebar.write('')
st.write('■5日中', paid_str, '日取得済（残', all_paid_str, '日）')
st.write('')


st.write('＜資格取得報告＞')
python3 = st.sidebar.slider('Python 3 エンジニア認定基礎試験進捗', 0, 100, 50)
python3_str = str(python3)
st.sidebar.write('')
st.write('■Python 3 エンジニア認定基礎試験/2月予定/', python3_str, '%')
basic_enginer = st.sidebar.slider('基本情報技術者試験進捗', 0, 100, 20)
basic_enginer_str = str(basic_enginer)
st.sidebar.write('')
st.write('■基本情報技術者試験/4月予定/', basic_enginer_str, '%')
st.write('')

st.write('＜トピックス、連絡事項、その他＞')
contact = st.sidebar.checkbox('トピックス、連絡事項、その他記入')
if contact:
    message = st.sidebar.text_input('内容記入')
    st.write(message)
else:
    st.write('なし')


st.write('')

st.write('以上、よろしくお願いいたします。')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')


#改善点
st.write('改善点1：稼働日数を自動で出力できるようにする')
st.write('改善点2：前回値を初期値にできないか？')
st.write('改善点3：超過報告を追加できるようにする（その他の項目についても例外を入力できるようにする）')
st.write('改善点4：休暇取得や休日出勤を複数選択でき、1つも存在しないときは「■なし」の出力を1つにする')
st.write('改善点5：月をまたいだ時に二つ出力できるようにする')
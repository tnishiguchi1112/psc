import streamlit as st
import datetime
import time

# git init
# git remoto add origin https://github.com/tnishiguchi1112/psc.git
# git add .
# git commit -m '1st commit'
# git push origin main


st.title('週報作成ツール')
st.write('左上部の「>」ボタンをクリックしスライダーを展開できます。')
st.write('パラメータ入力後、下記をコピーボタンをしてください。')


#作成者選択
human_text = st.sidebar.checkbox('←「対象者を選択」になければ選択')
if human_text:
    human_text_message = st.sidebar.text_input('対象者を記入（苗字が2文字の方のみ対応）')
    #空白で分割して記述すれば、苗字と名前を分けられるかも
    human_text_message_str = str(human_text_message)
else:
    human = st.sidebar.selectbox(
    '対象者を選択',
    ('西口崇登', '井東直人', '白川真衣'))
    human_str = str(human)

    
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')

#週報期間（開始）
d_start = st.sidebar.date_input(
    "＜週報期間＞（開始日を選択）",
    datetime.date.today())
d_start_str = str(d_start)
d_start_str_slash = d_start_str.replace('-', '/') 


st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#週報期間（終了）
d_end = d_start + datetime.timedelta(days=7)
d_end_str = str(d_end)
d_end_str_slash = d_end_str.replace('-', '/') 
st.write('')


st.write('-----------------------------------------')
st.write('')


#件名
mail = ('件名：')
mail_title = ('西日本BPO1課_')
pj = ('_PJ週報_')
if human_text:
    mail_title_sun_text = mail + mail_title + human_text_message_str + pj + d_end_str_slash
    st.write(mail_title_sun_text)
else:
    mail_title_sun = mail + mail_title + human_str + pj + d_end_str_slash
    st.write(mail_title_sun)
import pyperclip
if human_text:
    if st.button('件名コピー'):
        mail_title_sun_text2 = mail_title + human_text_message_str + pj + d_end_str_slash
        pyperclip.copy(mail_title_sun_text2) # クリップボードに文字列を格納
    else:
        pass
else:
    if st.button('件名コピー'):
        mail_title_sun2 = mail_title + human_str + pj + d_end_str_slash
        pyperclip.copy(mail_title_sun2) # クリップボードに文字列を格納
    else:
        pass


st.write('')
st.write('-----------------------------------------')
st.write('')


#本文
st.write('本文:')
st.write('')


#挨拶文
otukare = ('おつかれさまです。西日本BPO1課の')
desu = ('です。')
st.write('各位')
st.write('')
if human_text:
    mail_start_text = otukare + human_text_message[0:2] + desu
    st.write(mail_start_text)
else:
    mail_start = otukare + human[0:2] + desu
    st.write(mail_start)
st.write('')
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
st.sidebar.subheader('＜今週の主な業務内容＞')


#各種資料作成
document = st.sidebar.checkbox('各種資料作成')
if document:
    st.write('■各種資料作成')
    document1 = st.sidebar.checkbox('各種機器設定変更手順書を選択')
    if document1:
        st.write('・各種機器設定変更手順書')
    else:
        pass
    document_text = st.sidebar.checkbox('その他を記入')
    if document_text:
        document_text1 = st.sidebar.text_input('その他')
        st.write('・', document_text1)
        document_text2 = st.sidebar.checkbox('2つ目のその他を記入')
        if document_text2:
            document_text2 = st.sidebar.text_input('2つ目のその他')
            st.write('・', document_text2)
            document_text3 = st.sidebar.checkbox('3つ目のその他を記入')
            if document_text3:
                document_text3 = st.sidebar.text_input('3つ目のその他')
                st.write('・', document_text3)
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass


#設定変更作業
st.sidebar.write('')
device = st.sidebar.checkbox('設定変更作業')
if device:
    st.write('■設定変更作業')
    device1 = st.sidebar.checkbox('設定変更機器を選択')
    if device1:
        device1 = st.sidebar.selectbox(
        '機器を選択',
        ('FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'BIG-IP', 'レガシー'))
        st.write('・', device1)
        device2 = st.sidebar.checkbox('2つ目の設定変更機器を追加')
        if device2:
            device2 = st.sidebar.selectbox(
            '2つ目の機器を選択',
            ('FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'BIG-IP', 'レガシー'))
            st.write('・', device2)
            device3 = st.sidebar.checkbox('3つ目の設定変更機器を追加')
            if device3:
                device3 = st.sidebar.selectbox(
                '3つ目の機器を選択',
                ('FortiGate', 'PaloAlto', 'i-Filter', 'DNS', 'vShieldEdge', 'BIG-IP', 'レガシー'))
                st.write('・', device3)
            else:
                pass
        else:
            pass
    device_text = st.sidebar.checkbox('設定変更機器を記入')
    if device_text:
        message = st.sidebar.text_input('設定変更機器')
        st.write('・', message)
        device_text2 = st.sidebar.checkbox('2つ目の設定変更機器を記入')
        if device_text2:
            message2 = st.sidebar.text_input('2つ目の設定変更機器')
            st.write('・', message2)
            device_text3 = st.sidebar.checkbox('3つ目の設定変更機器を記入3')
            if device_text3:
                message3 = st.sidebar.text_input('3つ目の設定変更機器')
                st.write('・', message3)
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass


#その他
st.sidebar.write('')
other = st.sidebar.checkbox('その他')
if other:
    st.write('■その他')
    other1 = st.sidebar.checkbox('その他業務を選択')
    if other1:
        other2 = st.sidebar.selectbox(
        '業務を選択',
        ('チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
        st.write('・', other2)
        other3 = st.sidebar.checkbox('2つ目のその他業務を追加')
        if other3:
            other4 = st.sidebar.selectbox(
            '2つ目の業務を選択',
            ('チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
            st.write('・', other4)
            other5 = st.sidebar.checkbox('3つ目のその他業務を追加')
            if other5:
                other6 = st.sidebar.selectbox(
                '3つ目の業務を選択',
                ('チケット当番', 'エビデンス当番', '当番業務', 'MTG'))
                st.write('・', other6)
        else:
            pass
    else:
        pass
    other_text = st.sidebar.checkbox('その他業務を記入')
    if other_text:
        other_text1 = st.sidebar.text_input('業務を記入')
        st.write('・', other_text1)
        other_text2 = st.sidebar.checkbox('2つ目のその他業務を記入')
        if other_text2:
            other_text3 = st.sidebar.text_input('2つ目の業務を記入')
            st.write('・', other_text3)
            other_text4 = st.sidebar.checkbox('3つ目のその他業務を記入')
            if other_text4:
                other_text5 = st.sidebar.text_input('3つ目の業務を記入')
                st.write('・', other_text5)
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass


st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


syonari = '＜'
month = d_start_str_slash[5:7]


#稼働実績(後で修正)
kadou = ('月稼働実績＞')
kadou_str = syonari + month + kadou
st.sidebar.subheader(kadou_str)
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
st.write('＜', d_start_str_slash[5:7], '月稼働実績＞')
st.write('■稼働日：', workday_str, '日', '休暇取得：', holiday_str, '日', '当月想定稼働時間：', worktime_str, '時間(内平日深夜', overnighttime_str[0:5], '時間)')
st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#超過報告
st.write('＜', d_start_str_slash[5:7], '月超過報告＞')
overworkreport = ('月超過報告＞')
overworkreport_str = syonari + month + overworkreport
st.sidebar.subheader(overworkreport_str)
overtime = st.sidebar.time_input('常駐先残業時間', datetime.time(0, 00))
overtime_str = str(overtime)
st.sidebar.write('')
st.write('■', overtime_str[0:5], '/ 常駐先業務のため')
overtime_mtg = st.sidebar.time_input('BPO事業部MTGによる残業時間', datetime.time(0, 00))
overtime_mtg_str = str(overtime_mtg)
st.write('■', overtime_mtg_str[0:5], '/ BPO事業部ミーティングのため')

overtime_text = st.sidebar.checkbox('その他残業項目記入')
if overtime_text:
    overtime_text1 = st.sidebar.text_input('項目記入')
    overtime_text1_time = st.sidebar.time_input('残業時間', datetime.time(0, 00))
    overtime_text1_time_str = str(overtime_text1_time)
    st.write('■', overtime_text1_time_str[0:5], '/', overtime_text1)
    overtime_text2 = st.sidebar.checkbox('2つ目の残業項目記入')
    if overtime_text2:
        overtime_text3 = st.sidebar.text_input('2つ目の残業項目')
        overtime_text3_time = st.sidebar.time_input('2つ目の残業時間', datetime.time(0, 00))
        overtime_text3_time_str = str(overtime_text3_time)
        st.write('■', overtime_text3_time_str[0:5], '/', overtime_text3)
        overtime_text4 = st.sidebar.checkbox('3つ目の残業項目記入')
        if overtime_text4:
            overtime_text5 = st.sidebar.text_input('3つ目の残業項目')
            overtime_text5_time = st.sidebar.time_input('3つ目の残業時間', datetime.time(0, 00))
            overtime_text5_time_str = str(overtime_text5_time)
            st.write('■', overtime_text5_time_str[0:5], '/', overtime_text5)
        else:
            pass
    else:
        pass
else:
    pass

st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#休暇取得実績
st.write('＜休暇取得実績＞')
st.sidebar.subheader('＜休暇取得実績＞')
holiday_takeing = st.sidebar.checkbox('休暇取得の選択')
if holiday_takeing:
    premiumday = st.sidebar.checkbox('プレミアムデー取得')
    if premiumday:
        premiumday_take = st.sidebar.date_input(
        "プレミアムデー取得日を選択",
        datetime.date.today())
        premiumday_take_str = str(premiumday_take)
        premiumday_take_str_slash =premiumday_take_str.replace('-', '/') 
        st.write('■', premiumday_take_str_slash[5:10], 'プレミアムデー')
    else:
        pass
    holiday_take = st.sidebar.checkbox('有給休暇取得')
    if holiday_take:
        holiday_take_take = st.sidebar.date_input(
        "有給休暇取得日を選択",
        datetime.date.today())
        holiday_take_take_str = str(holiday_take_take)
        holiday_take_take_str_slash =holiday_take_take_str.replace('-', '/') 
        st.write('■', holiday_take_take_str_slash[5:10], '有給休暇')
    else:
        pass
else:
    st.write('■なし')


st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#休暇取得予定
st.write('＜休暇取得予定＞')
st.sidebar.subheader('＜休暇取得予定＞')
holiday_takeing_schedule = st.sidebar.checkbox('休暇取得予定の選択')
if holiday_takeing_schedule:
    premiumday_schedule = st.sidebar.checkbox('プレミアムデー取得予定')
    if premiumday_schedule:
        premiumday_schedule_take = st.sidebar.date_input(
        "プレミアムデー取得予定日を選択",
        datetime.date.today())
        premiumday_schedule_take_str = str(premiumday_schedule_take)
        premiumday_schedule_take_str_slash =premiumday_schedule_take_str.replace('-', '/') 
        st.write('■', premiumday_schedule_take_str_slash[5:10], 'プレミアムデー')
    else:
        pass
    holiday_schedule = st.sidebar.checkbox('有給休暇予定')
    if holiday_schedule:
        holiday_schedule_take = st.sidebar.date_input(
        "有給休暇取得予定日を選択",
        datetime.date.today())
        holiday_schedule_take_str = str(holiday_schedule_take)
        holiday_schedule_take_str_slash =holiday_schedule_take_str.replace('-', '/') 
        st.write('■', holiday_schedule_take_str_slash[5:10], '有給休暇')
    else:
        pass
else:
    st.write('■なし')


st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#休日出社実績
st.write('＜休日出勤実績＞')
st.sidebar.subheader('＜休日出勤実績＞')
holiday_work = st.sidebar.checkbox('休日出社実績（全体研修のみ）')
if holiday_work:
    holiday_work_take = st.sidebar.date_input(
    "休日出社日",
    datetime.date.today())
    holiday_work_take_str = str(holiday_work_take)
    holiday_work_take_str_slash =holiday_work_take_str.replace('-', '/') 
    st.write('■', holiday_work_take_str_slash[5:10], '全体研修のため')
else:
    st.write('■なし')
st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#休日出勤予定
st.write('＜休日出勤予定＞')
st.sidebar.subheader('＜休日出勤予定＞')
holiday_work_schedule = st.sidebar.checkbox('休日出社予定（全体研修のみ）')
if holiday_work_schedule:
    holiday_work_schedule = st.sidebar.date_input(
    "休日出社予定日",
    datetime.date.today())
    holiday_work_schedule_str = str(holiday_work_schedule)
    holiday_work_schedule_str_slash =holiday_work_schedule_str.replace('-', '/') 
    st.write('■', holiday_work_schedule_str_slash[5:10], '全体研修のため')
else:
    st.write('■なし')
st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#有給休暇取得状況
st.write('＜有給休暇取得状況＞')
st.sidebar.subheader('＜有給休暇取得状況＞')
all_paid = st.sidebar.slider('総有給数', 0, 40, 10)
all_paid_str = str(all_paid)
st.sidebar.write('')
paid = st.sidebar.slider('有給取得数', 0, 40, 0)
paid_str = str(paid)
all_paid_nokori = all_paid - paid
all_paid_nokori_str = str(all_paid_nokori)
st.write('■5日中', paid_str, '日取得済（残', all_paid_nokori_str, '日）')
st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#資格取得報告
st.write('＜資格取得報告＞')
st.sidebar.subheader('＜資格取得報告＞')
syape = ('/')
pasent = ('%')
shikaku = st.sidebar.checkbox('その他の資格項目を記入')
if shikaku:
    shikaku_text = st.sidebar.text_input('資格項目記入')
    shikaku_text_goal = st.sidebar.selectbox(
            '取得予定月を選択',
            ('1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月' '11月', '12月'))
    shikaku_slider = st.sidebar.slider(shikaku_text, 0, 100, 50)
    shikaku_slider_str = str(shikaku_slider)
    st.write(shikaku_text + syape + shikaku_text_goal + syape + shikaku_slider_str + pasent)
else:
    python3 = st.sidebar.slider('Python 3 エンジニア認定基礎試験進捗', 0, 100, 50)
    python3_str = str(python3)
    st.sidebar.write('')
    st.write('■Python 3 エンジニア認定基礎試験/2月予定/', python3_str, '%')

    basic_enginer = st.sidebar.slider('基本情報技術者試験進捗', 0, 100, 20)
    basic_enginer_str = str(basic_enginer)
    st.sidebar.write('')
    st.write('■基本情報技術者試験/4月予定/', basic_enginer_str, '%')





st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


#連絡事項
st.write('＜トピックス、連絡事項、その他＞')
contact = st.sidebar.checkbox('＜トピックス、連絡事項、その他＞')
if contact:
    message = st.sidebar.text_input('内容記入')
    st.write(message)
else:
    st.write('なし')
st.write('')
st.sidebar.write('')
st.sidebar.write('-----------------------------------------')
st.sidebar.write('')


st.write('以上、よろしくお願いいたします。')
st.write('')
st.write('-----------------------------------------')
st.write('')
st.write('ver1.2')
st.write('')
st.subheader('改善点')
st.write('対象者以外も選べるように記述欄を挿入')
st.write('選択を3つ、記述も3つまで選べるように改善')
st.write('休暇や休日出勤が1つもない場合「■なし」を1つだけ出力するように改善')
st.write('作成した文をコピーできるコピーボタンを挿入')
st.write('')
st.subheader('要改善点')
st.write('平日から休暇取得日数を引いて自動で稼働日数を算出')
st.write('スマホで使用する場合、サイドバーのカレンダー使用時、毎回閉じてしまう')
st.write('本文のコピーは分岐や量が多すぎて、今の技術力では困難')

# if human_text:
#     human_text_message_str = str(human_text_message)
# else:
#     human_str = str(human)

# fasdf = human_text_message_str

# if st.button('本文コピー'):
#     pyperclip.copy(fasdf)
# else:
#     pass
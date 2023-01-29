# print('グー=1, チョキ=2, パー=3, OK=4')

# t = input('太郎: ')
# h = input('花子: ')

# t = int(t)
# h = int(h)

# # syohai = (t - h + 3) % 3

# if t == h:
#     print('あいこ')
# else:
#     t = t + 1
#     if t > 3:
#         t = 1
#         if t == h or t == 4:
#             print('太郎の勝ち')
#         else:
#             print('花子の勝ち')



# t = ('太郎の勝ち')
# h = ('花子の勝ち')
# a = ('あいこ')

# two_dimensional_list_janken = [
#     [a,t,h,h],
#     [h,a,t,h],
#     [t,h,a,h],
#     [t,t,t,a]
# ]

# print('グー=1, チョキ=2, パー=3, OK=4')

# t_int = input('太郎: ')
# h_int = input('花子: ')

# t_int = int(t_int)
# h_int = int(h_int)

# t_int = int(t_int - 1)
# h_int = int(h_int - 1)

# print(two_dimensional_list_janken[t_int][h_int])



# import random

# for i in range(10):
#     t = random.randint(0,3)

# for i in range(10):
#     h = random.randint(0,3)



#日数計算
# two_dimensional_list_day = [
#     [1,2,3,4,5,6,7,8,9,10,11,12],
#     [31,59,90,120,151,181,212,243,273,304,334,365]
# ]

# m = input('月を入力：')
# d = input('日を入力：')

# m = int(m)
# m = m - 2
# d = int(d)

# total_day = d

# if m < 0:
#     pass
# else:
#     tmp_day = (two_dimensional_list_day[1][m])
#     tmp_day = int(tmp_day)
#     total_day = total_day + tmp_day

# print(total_day)



# two_dimensional_list_day = [
#     [1,2,3,4,5,6,7,8,9,10,11,12],
#     [31,28,31,30,31,30,31,31,30,31,30,31]
# ]
# day_of_week = ('日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日')





# try:
#     y = int(input('年を入力：'))
#     m = int(input('月を入力：'))
#     d = int(input('日を入力：'))
# except ValueError:
#     print('数字以外が入力されました。数字のみを入力してください')

# try:
#     m < 1 or 12 < m
# except:
#     print('生年月日の月の値が間違っています')

# if y / 4 == 0 and not(y / 100 == 0) or y / 400 == 0:
    

# week = input('曜日：')
# week = int(week)
# week = week - 1

# if week < 0 or 6 < week:
#     pass
# else:
#     print(day_of_week[week])



#p125割引率---------------------------------------------
# money_table = (0, 1000, 5000, 10000, 30000, 50000)
# tax = (1, 0.9, 0.85, 0.8, 0.75, 0.7)

# try:
#     total_money = int(input('合計金額を記入を入力：'))
# except ValueError:
#     print('数字以外が入力されました。数字のみを入力してください')

# kazu = 5

# while total_money < money_table[kazu]:
#     kazu = kazu - 1

# pay_money = int(total_money * tax[kazu])

# print(pay_money)



#p126賞与の金種計算
TBL = [10000, 5000, 1000, 500, 100, 50, 10 , 5 , 1] #金種表
MNY = [0, 0, 0, 0, 0, 0, 0, 0, 0] #枚数表

try:
    GNK = int(input('賞与支給額を入力：'))
except ValueError:
    print('数字以外が入力されました。数字のみを入力してください')

number = 0

while GNK > 0:
    sheet = int(GNK / TBL[number])
    MNY[number] = MNY[number] + sheet
    GNK = GNK - sheet * TBL[number]
    number += 1

for (x, y) in zip(TBL, MNY):
    print(x, y)


import pandas as pd

df = pd.DataFrame({'金種':TBL, '枚数':MNY})

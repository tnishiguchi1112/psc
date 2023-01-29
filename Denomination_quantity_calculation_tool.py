import streamlit as st
import pandas as pd

# git init
# git remoto add origin https://github.com/tnishiguchi1112/psc.git
# git add .
# git commit -m '1st commit'
# git push origin main

st.title('金種枚数計算ツール')

TBL = [10000, 5000, 1000, 500, 100, 50, 10 , 5 , 1] #金種表
MNY = [0, 0, 0, 0, 0, 0, 0, 0, 0] #枚数表

GNK = st.number_input('金額を入力：',0,1000000,356789)

number = 0

GNK = int(GNK)

while GNK > 0:
    sheet = int(GNK / TBL[number])
    MNY[number] = MNY[number] + sheet
    GNK = GNK - sheet * TBL[number]
    number += 1

for (x, y) in zip(TBL, MNY):
    print(x, y)

df = pd.DataFrame({'金種':TBL, '枚数':MNY})
st.write(df)
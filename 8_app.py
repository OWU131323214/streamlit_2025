import streamlit as st  # streamlit run 8_app.py
import pandas as pd
import plotly.express as px
import os

# EXCEL_PATH = "eitango.xlsx"
# SHEET_NAME = "Sheet2"


# # エクセル
# @st.cache_data
# def load_data():
#     if os.path.exists(EXCEL_PATH):
#         return pd.read_excel(EXCEL_PATH, sheet_name=None) # sheet_name=None → 全シート読み込む
#     else:
#         return pd.DataFrame(columns=["回答数", "合計数"])

# # 保存
# def save_excel(df):
#     # pd.ExcelWriter() Pandasの関数で、Excelファイルに書き込むための「書き込み用オブジェクト」 を作成
#     with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='w') as writer:
#         if "data1" in st.session_state:
#             df1 = pd.DataFrame(st.session_state["ans"])
#             df1.to_excel(writer, sheet_name="Sheet2", index=False)

#     if "data2" in st.session_state:
#             df2 = pd.DataFrame(st.session_state["total_ans"])
#             df2.to_excel(writer, sheet_name="Sheet3", index=False)

# # 3. session_state に保存用リストがなければ作る
# if "data" not in st.session_state:
#     st.session_state["data"] = load_data()


options = ["","リンゴ", "ナス", "ブドウ", "イチゴ", "モモ", "カキ(果物)", "スイカ", "カブ"]
anser = {"リンゴ":"apple", "ナス":"eggplant", "ブドウ":"grapes", "イチゴ":"strawberry", "モモ":"peach", "カキ(果物)":"persimmon", "スイカ":"watermelon", "カブ":"turnip"}

# ------問１-----
faculty0_Q = "apple"
faculty0 = st.selectbox(  #None # 仮の値
    # label="1.apple",
    faculty0_Q,
    options,
)

# 選択値の表示
if st.button("問1答え"):
    st.session_state.total_ans += 1
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty0_Q == anser.get(faculty0):
        st.write(faculty0_Q , ":", faculty0)
        st.balloons() # 風船を出す
        st.write("正解！")
        st.session_state.ans += 1
    else:
        st.write(faculty0_Q , ":？")
        st.write("不正解")
        st.session_state.ans -= 1

#-----問２-----
faculty1_Q = "eggplant"
faculty1 = st.selectbox(  #None # 仮の値
    # label="2.eggplant",
    faculty1_Q,
    options,
)

# 選択値の表示
if st.button("問2答え"):
    st.session_state.total_ans += 1
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty1_Q == anser.get(faculty1):
        st.write(faculty1_Q , ":", faculty1)
        st.balloons() # 風船を出す
        st.write("正解！")
        st.session_state.ans += 1
    else:
        st.write(faculty1_Q , ":？")
        st.write("不正解")
        st.session_state.ans -= 1

#------問３-----
faculty2_Q = "persimmon"
faculty2 = st.selectbox(  #None # 仮の値
    # label="1.apple",
    faculty2_Q,
    options,
)

# 選択値の表示
if st.button("問3答え"):
    st.session_state.total_ans += 1
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty2_Q == anser.get(faculty2):
        st.write(faculty2_Q , ":", faculty2)
        st.balloons() # 風船を出す
        st.write("正解！")
        st.session_state.ans += 1
    else:
        st.write(faculty2_Q , ":？")
        st.write("不正解")
        st.session_state.ans -= 1

#-----問４-----
faculty3_Q = "turnip"
faculty3 = st.selectbox(  #None # 仮の値
    # label="1.apple",
    faculty3_Q,
    options,
)

# 選択値の表示
if st.button("問4答え"):
    st.session_state.total_ans += 1
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty3_Q == anser.get(faculty3):
        st.write(faculty3_Q , ":", faculty3)
        st.balloons() # 風船を出す
        st.write("正解！")
        st.session_state.ans += 1
    else:
        st.write(faculty3_Q , ":？")
        st.write("不正解")
        st.session_state.ans -= 1

# その他
st.write("自由")
with st.expander("自由"):
    mondai = st.text_input("問題を入力")
    kotae = st.text_input("答えを入力")

# with st.expander("一覧"):
    df = pd.read_excel("eitango1.xlsx")
    country_names = df["日本語"].unique()
    selected_country = st.selectbox("問題一覧", country_names)
    df_selected = df[df["日本語"] == selected_country]
    st.dataframe(df_selected)

options.append(kotae)
anser[kotae] = mondai
faculty_Q = mondai
faculty = st.selectbox(  #None # 仮の値
    # label="2.eggplant",
    faculty_Q,
    options,
)

# 選択値の表示
if st.button("その他答え"):
    # st.session_state.total_ans += 1
    # st.write(f"単語の訳:{faculty}は、{anser.get(faculty)}")
    if faculty_Q == anser.get(faculty):
        st.write(faculty_Q , ":", faculty)
        st.balloons() # 風船を出す
        st.write("正解！")
        # st.session_state.ans += 1
    else:
        st.write(faculty_Q , ":？")
        st.write("不正解")
        st.session_state.ans -= 1

if "ans" and "total_ans" not in st.session_state:
    st.session_state["ans"] = 0
    st.session_state["total_ans"] = 0

st.write(f"正解数：{st.session_state.ans}/{st.session_state.total_ans} 正解 +1、不正解 -1")

# if st.button("保存"):
#     save_excel(df)
#     st.session_state["data"].append({"名前": name, "年齢": age})
#     st.success("セッションに追加しました")

if st.button("リセット"):
    st.session_state.ans = 0


# if st.button("診断する"):
#     st.header("診断結果")

#     # 選択値の表示
#     st.write(f"あなたが選んだ果物:{faculty}")
    
#     # if faculty: # 簡単な入力チェック
#     feedback = []

#     if "文学部" in faculty:
#         feedback.append("自由時間ががたくさんできますね")
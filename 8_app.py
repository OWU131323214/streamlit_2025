import streamlit as st  # streamlit run 8_app.py

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
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty0_Q == anser.get(faculty0):
        st.write(faculty0_Q , ":", faculty0)
        st.balloons() # 風船を出す
        st.write("正解！")
    else:
        st.write(faculty0_Q , ":？")
        st.write("不正解")

#-----問２-----
faculty1_Q = "eggplant"
faculty1 = st.selectbox(  #None # 仮の値
    # label="2.eggplant",
    faculty1_Q,
    options,
)

# 選択値の表示
if st.button("問2答え"):
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty1_Q == anser.get(faculty1):
        st.write(faculty1_Q , ":", faculty1)
        st.balloons() # 風船を出す
        st.write("正解！")
    else:
        st.write(faculty1_Q , ":？")
        st.write("不正解")

#------問３-----
faculty2_Q = "persimmon"
faculty2 = st.selectbox(  #None # 仮の値
    # label="1.apple",
    faculty2_Q,
    options,
)

# 選択値の表示
if st.button("問3答え"):
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty2_Q == anser.get(faculty2):
        st.write(faculty2_Q , ":", faculty2)
        st.balloons() # 風船を出す
        st.write("正解！")
    else:
        st.write(faculty2_Q , ":？")
        st.write("不正解")

#-----問４-----
faculty3_Q = "turnip"
faculty3 = st.selectbox(  #None # 仮の値
    # label="1.apple",
    faculty3_Q,
    options,
)

# 選択値の表示
if st.button("問4答え"):
    # st.write(f"単語の訳:{faculty0}は、{anser.get(faculty0)}")
    if faculty3_Q == anser.get(faculty3):
        st.write(faculty3_Q , ":", faculty3)
        st.balloons() # 風船を出す
        st.write("正解！")
    else:
        st.write(faculty3_Q , ":？")
        st.write("不正解")

# その他
st.write("自由")
with st.expander("自由"):
    mondai = st.text_input("問題を入力")
    kotae = st.text_input("答えを入力")
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
    # st.write(f"単語の訳:{faculty}は、{anser.get(faculty)}")
    if faculty_Q == anser.get(faculty):
        st.write(faculty_Q , ":", faculty)
        st.balloons() # 風船を出す
        st.write("正解！")
    else:
        st.write(faculty_Q , ":？")
        st.write("不正解")


# if st.button("診断する"):
#     st.header("診断結果")

#     # 選択値の表示
#     st.write(f"あなたが選んだ果物:{faculty}")
    
#     # if faculty: # 簡単な入力チェック
#     feedback = []

#     if "文学部" in faculty:
#         feedback.append("自由時間ががたくさんできますね")
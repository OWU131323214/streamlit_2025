import streamlit as st

# st.sidebar 例
st.markdown("**st.sidebar 例:**")
add_selectbox = st.sidebar.selectbox(
    "連絡方法を選択してください",
    ("メール", "携帯電話", "LINE")
)
st.sidebar.write(f"選択された連絡方法: {add_selectbox}")

st.markdown("---")

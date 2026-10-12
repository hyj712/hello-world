# -*- coding: utf-8 -*-
# lab1_探针.py —— 实验室 1：整页重跑实验
import streamlit as st
from datetime import datetime

# ========== 探针 1：脚本真的每次都被重新执行吗？ ==========
print("🎬 脚本从头执行了一次！当前时刻：", datetime.now().strftime("%H:%M:%S"))

# ========== 探针 2：普通变量 ==========
ordinary = datetime.now().strftime("%H:%M:%S")
print("   普通变量 ordinary 本轮的值 =", ordinary)

st.title("实验室 1：什么能记住，什么记不住？")

st.write("📦 普通变量 ordinary 的值：", ordinary)
st.write("（提示：点几下按钮、在输入框里打字，再看它变不变）")

# ========== 储物柜 st.session_state ==========
if "counter" not in st.session_state:
    st.session_state.counter = 0
    print("   （首次运行）counter 被初始化成 0")

if st.button("点我：储物柜 counter + 1"):
    st.session_state.counter += 1
    print("   按钮被点击！counter =", st.session_state.counter)

st.write("🔒 st.session_state 里 counter 的值：", st.session_state.counter)

# ========== 输入框 ==========
name = st.text_input("随便输入点东西：")
print("   输入框本轮返回的值 name =", repr(name))
st.write("输入框本轮返回的值：", name)
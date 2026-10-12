# -*- coding: utf-8 -*-
# lab3_清空方案.py —— 实验室 3：验证你的清空方案
import streamlit as st

st.title("实验室 3：验证你的清空方案")

st.markdown("""
你的方案：**删掉格子 + st.rerun()**。
这一课我们实测它，再做一组对照实验，看看 rerun 到底在做什么。
""")

print("▶ 本轮开始时，格子 w_name =", repr(st.session_state.get("w_name")))

name = st.text_input("伴侣名字（key='w_name'）", key="w_name", value="")
print("   输入框渲染后：格子 w_name =", repr(st.session_state.get("w_name")), "| 变量 name =", repr(name))

st.write("🔍 储物柜：", dict(st.session_state))

col1, col2 = st.columns(2)
with col1:
    if st.button("对照实验：只删格子，不 rerun"):
        st.session_state.pop("w_name", None)
        print("   🔧 对照实验：格子已删，但没有 rerun——页面会立刻变吗？")
with col2:
    if st.button("你的方案：删格子 + rerun"):
        st.session_state.pop("w_name", None)
        print("   🔧 你的方案：格子已删，马上 rerun 重画页面")
        st.rerun()

st.write("本轮变量 name 的值 =", repr(name))
# -*- coding: utf-8 -*-
# lab4_出生证明.py —— 实验室 4：value 是干什么的？
import streamlit as st

st.title("实验室 4：value 是干什么的？")

st.session_state.truth = "真昼"   # 柜子里的"真相"（模拟项目里的 st.session_state.partner_name）

# 输入框 A：有 key，没有 value —— 出生时用 Streamlit 默认值（空字符串）
a = st.text_input("输入框 A（有 key，没有 value）", key="w_a")

# 输入框 B：有 key，有 value —— 出生时把柜子里的真相拿来当初始值
b = st.text_input("输入框 B（有 key，value=柜子里的真相）", key="w_b", value=st.session_state.truth)

st.write("🔍 储物柜：", dict(st.session_state))

if st.button("删掉两个输入框的格子，让它们重生"):
    st.session_state.pop("w_a", None)
    st.session_state.pop("w_b", None)
    st.rerun()
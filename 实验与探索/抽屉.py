# -*- coding: utf-8 -*-
# 抽屉.py —— 实验室 5 修复版：动态 key（换身份证）方案
import streamlit as st

print("🎬 脚本重跑！真相 =", repr(st.session_state.get("partner_name")),
      "| 当前输入框格子 =", repr(st.session_state.get(f"w_partner_name_{st.session_state.get('widget_version', 0)}")))

st.title("实验室 5：两个抽屉的分工（修复版）")

if "partner_name" not in st.session_state:
    st.session_state.partner_name = ""
if "widget_version" not in st.session_state:
    st.session_state.widget_version = 0   # 输入框的"身份证版本号"

st.session_state.partner_name = st.text_input(
    "伴侣名字",
    key=f"w_partner_name_{st.session_state.widget_version}",  # 换版本 = 换一个全新输入框
    value=st.session_state.partner_name,                      # 出生时从真相抽屉抄初始值
)

st.write("🟦 真相抽屉 partner_name =", repr(st.session_state.partner_name))
st.write("🟨 输入框抽屉（当前版本）=", repr(st.session_state.get(f"w_partner_name_{st.session_state.widget_version}")))

if st.button("加载历史：真相填入'真昼'"):
    st.session_state.partner_name = "真昼"
    st.session_state.pop(f"w_partner_name_{st.session_state.widget_version}", None)  # 清理旧格子
    st.session_state.widget_version += 1   # 版本号 +1：下一轮输入框以新身份、新值出生
    print("   [按钮被点击] 真相已改，版本号 +1，马上 rerun")
    st.rerun()

if st.button("新建会话：清空真相"):
    st.session_state.partner_name = ""
    st.session_state.pop(f"w_partner_name_{st.session_state.widget_version}", None)
    st.session_state.widget_version += 1
    print("   [按钮被点击] 真相已清空，版本号 +1，马上 rerun")
    st.rerun()
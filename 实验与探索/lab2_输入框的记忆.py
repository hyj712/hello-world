# # -*- coding: utf-8 -*-
# # lab2_输入框的记忆.py —— 实验室 2：输入框的字藏在储物柜的哪个格子？
# import streamlit as st
#
# st.title("实验室 2：输入框的记忆住在哪里")
#
# st.markdown("""
# 你已经猜到：输入框里的字，存在 `st.session_state` 里。
# 这一课我们**亲手抓住它**，并复刻你项目里的那个 bug。
# """)
#
# # ========== 实验 A：没起名字的输入框，把字藏进了哪个格子？ ==========
# st.markdown("### 实验 A：没起名字的输入框，把字藏进了哪个格子？")
#
# st.write("🔍 打字之前，储物柜里的全部内容：")
# st.write(dict(st.session_state))
#
# a = st.text_input("在下面输入框里打几个字（这个输入框没起 key）：")
#
# st.write("📝 打完字后，回头看上面那个储物柜——有没有多出一个名字很乱的格子？")
# st.write("本轮变量 a 的值 =", repr(a))
# print("实验A：本轮 a =", repr(a))
#
# st.divider()
#
# # ========== 实验 B：给输入框起名字 key，复刻你项目里的 bug ==========
# st.markdown("### 实验 B：给输入框起名字，然后复刻你项目里的 bug")
#
# st.write("🔍 当前储物柜：")
# st.write(dict(st.session_state))
#
# name = st.text_input(
#     "伴侣名字（key='w_name'）",
#     key="w_name",
#     value="",   # 注意：value 只在输入框"第一次出生"时生效一次
# )
#
# if st.button("复刻 bug：把变量 name 清空"):
#     name = ""   # 你以为这样能清空输入框……
#     st.rerun()
#
# st.write("本轮变量 name 的值 =", repr(name))
# print("实验B：本轮 name =", repr(name))
# st.write("⚠️ 先在输入框里打字，再点按钮——框里的字消失了吗？")
import streamlit as st



if st.button("正确做法：清空输入框"):
    # ① 对储物柜里的格子 w_name 做什么操作？
    st.session_state.w_name = ""
    # ② 变量 name 还需要特意清空吗？为什么？

    # ③ 为什么最后还要 st.rerun()？

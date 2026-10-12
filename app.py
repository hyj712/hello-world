# -*- coding: utf-8 -*-
"""
启动器（只有 3 行，不是你的业务代码）

作用：Streamlit Cloud 那边的"Main file path"已经设成了 app.py，
      所以这里放一个启动器去运行你自己写的 AI-partner_1.py。
      这样你在 PyCharm 里改 AI-partner_1.py 就行，
      Streamlit 的设置一个字都不用动。

如果你更想把入口文件直接改成 AI-partner_1.py：
  在 Streamlit Cloud → 你的 App → Settings 里改不了入口文件，
  只能删掉这个 App 重新建一个，Main file path 填 AI-partner_1.py。
  两种做法效果一样，用启动器更省事。
"""

import runpy

# 运行你自己写的那份代码
runpy.run_path("AI-partner_1.py")

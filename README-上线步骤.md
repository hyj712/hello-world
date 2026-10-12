# 让"你自己的代码"上线：只需要三步

这个文件夹里的东西，是**部署必需的辅助文件**（不是你的业务代码）：

| 文件 | 作用 |
|---|---|
| `app.py` | 启动器，3 行，负责运行你的 `AI-partner_1.py`（这样 Streamlit 那边的入口不用改） |
| `requirements.txt` | 告诉 Streamlit Cloud 装 `streamlit` 和 `openai` |
| `.gitignore` | 防止把聊天记录、`.DS_Store` 传上 GitHub |
| `.streamlit/config.toml` | 深色主题（可选，删掉也能跑） |
| `assets/avatar_user.png`、`assets/avatar_ai.png` | 两张头像图片（要用自定义头像才需要） |

## 第 1 步：把这些文件复制进你的 PyCharm 项目

在 PyCharm 底部的 **Terminal** 标签里执行：

```bash
cp -R /Users/hyj/Documents/deepseek-harness/default-workspace/pycharm-deploy/. ~/PycharmProjects/AI应用/
```

## 第 2 步：给你自己的 `AI-partner_1.py` 打补丁

见聊天窗口里给的两段代码（一处必须改：key 的读法；一处可选：自定义头像）。

## 第 3 步：推送（还是在 PyCharm 的 Terminal 里）

```bash
cd ~/PycharmProjects/AI应用
git init -b main
git add .
git status
git commit -m "用我自己的代码上线"
git remote add origin https://github.com/hyj712/hello-world.git
git push -f origin main
```

推完 Streamlit Cloud 会自动重新部署（1 分钟左右）。

## 怎么确认线上跑的是你的代码

看网页左侧边栏第一块：
- 显示 "🔑 服务状态" → 还是我之前那份；
- 直接显示 "关于伴侣" → 已经是你的代码了 ✅

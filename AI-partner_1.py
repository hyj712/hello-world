                                          #The environment construction part


# to import the required modules
import streamlit as st
import os
from openai import OpenAI
import json
from datetime import datetime


# page configuration
st.set_page_config(
    page_title="Your personal AI partner",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
# ---- 访问口令（可选，但建议：防止陌生人用你的额度）----
try:
    _password = st.secrets["app_password"]
except Exception:
    _password = ""
if _password and not st.session_state.get("gate_passed"):
    if st.text_input("请输入访问口令", type="password", key="gate_input") == _password:
        st.session_state.gate_passed = True
        st.rerun()
    st.stop()

# page title
st.title("AI智能伴侣")
st.subheader("made by hyj712 from github")
st.logo("img.png")


# environment configuration
# environment configuration
key = os.getenv("DEEPSEEK_API_KEY")        # 本机：读环境变量
if not key:                                # 线上：读 Streamlit 的 Secrets
    try:
        key = st.secrets["DEEPSEEK_API_KEY"]
    except Exception:
        key = ""
if not key:
    st.error("没有找到 API Key：本机请先设置环境变量 DEEPSEEK_API_KEY；"
             "线上请在 Streamlit Cloud 的 Settings → Secrets 里配置。")
    st.stop()
client = OpenAI(api_key=key,base_url="https://api.deepseek.com")
# conversation stream generator
def stream():
    for i in res.choices[0].message.content :
        yield i
        time.sleep(0.04)

def reset_partner_inputs():

    st.session_state.pop(f"w_name_{st.session_state.widget_version}", None)
    st.session_state.pop(f"w_character_{st.session_state.widget_version}", None)
    st.session_state.widget_version += 1

#define some functions
def create_conversation_file():
# to create the name of the conversation file and collect the conversation data
    if check_avoid_file_repetition() == False:
        st.warning("")
    else:
        conversation_time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
        st.session_state.conversation_conversation_data = {"name": conversation_time,
                                                       "system_prompt": [st.session_state.partner_name,st.session_state.partner_character],
                                                       "messages": st.session_state.messages
                                                       }
        st.session_state.messages = []
        st.session_state.partner_character = ""
        st.session_state.partner_name = ""
        st.session_state.current_time = ""
        reset_partner_inputs()

# to create a json file to store the conversation data
    with open(f"./conversation_record/{conversation_time}.json", "w") as f:
        json.dump(st.session_state.conversation_conversation_data, f, ensure_ascii=False, indent=2)
    st.rerun()

def list_conversation_history():
    st.text("历史会话")
    if os.path.exists("conversation_record"):
        for i in os.listdir("conversation_record"):
            col1,col2 = st.columns([3,1])
            with col1:

                if st.button(i[:-5],width = "stretch"):
                    display_conversation_history(i[:-5])
            with col2:
                if st.button("",width = "stretch",key = i[:-5],icon = ":material/delete:"):
                    delete_conversation(i[:-5])

def display_conversation_history(conversation_time):
    st.session_state.messages = json.load(open(f"./conversation_record/{conversation_time}.json", "r"))["messages"]
    st.session_state.partner_name = json.load(open(f"./conversation_record/{conversation_time}.json", "r"))["system_prompt"][0]
    st.session_state.partner_character = json.load(open(f"./conversation_record/{conversation_time}.json", "r"))["system_prompt"][1]
    st.session_state.current_time = conversation_time
    reset_partner_inputs()
    st.rerun()


    st.rerun()
def delete_conversation(conversation_time):
    os.remove(f"./conversation_record/{conversation_time}.json")
    st.rerun()

    if conversation_time == st.session_state.current_time:
        st.session_state.current_time = ""
        st.session_state.partner_name = ""
        st.session_state.partner_character = ""
        st.session_state.messages = []
        reset_partner_inputs()
    st.rerun()

    # for file in os.listdir("./conversation_record"):
    #     with open(f"./conversation_record/{conversation_time}/{file}", "r") as f:
    #         data = json.load(f)
    #         if data["system_prompt"][0] == st.session_state.partner_name and data["system_prompt"][1] == st.session_state.partner_character and data["messages"] == st.session_state.messages:
    #             st.rerun()
    #
    #         else :
    #             st.session_state.messages = []
    #             st.session_state.partner_character = ""
    #             st.session_state.partner_name = ""
    #             reset_partner_inputs()
    #             st.rerun()







def stream_response():
    """逐 token 流式输出（真流式：边生成边显示）"""
    try:
        stream = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=api_messages,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                reply_parts.append(delta)
                yield delta
    except Exception as e:
        yield f"\n\n[出错了：{e}]"

def check_avoid_file_repetition():
    for file in os.listdir("conversation_record"):
        with open(f"./conversation_record/{file}", "r") as f:
            data = json.load(f)
            if data["system_prompt"][0] == st.session_state.partner_name and data["system_prompt"][1] == st.session_state.partner_character and data["messages"] == st.session_state.messages:
                st.session_state.partner_name = ""
                st.session_state.partner_character = ""
                st.session_state.messages = []
                reset_partner_inputs()
                st.rerun()
                return False












                                             # The Operation Part




if "messages" not in st.session_state:
    st.session_state.messages = []          #to store the conversation history
#if "system prompt" not in st.session_state:
   # st.session_state.system_prompt = []     # to store the system prompt
if not os.path.exists("conversation_record"):
    os.makedirs("conversation_record")
if "partner_name" not in st.session_state:
    st.session_state.partner_name = ""
if "partner_character" not in st.session_state:
    st.session_state.partner_character = ""
if "widget_version" not in st.session_state:
    st.session_state.widget_version = 0   # 输入框的"身份证版本号"
if "current_time" not in st.session_state:
    st.session_state.current_time = ""


# conversation history display
for m in st.session_state.messages:
    if m["role"] == "user" or m["role"] == "assistant":
        st.chat_message(m["role"]).write(m["content"])

# sidebar
with st.sidebar:
    st.subheader("关于伴侣")

    # system prompt input
    st.session_state.partner_name = st.text_input("为你的伴侣起个名字吧～", placeholder="例如：真昼……", key=f"w_name_{st.session_state.widget_version}", value=st.session_state.partner_name)
    st.session_state.partner_character = st.text_area("为你的伴侣添加一些介绍吧～", placeholder="例如：你是一个温柔可爱细致体贴的女孩……", key=f"w_character_{st.session_state.widget_version}", value=st.session_state.partner_character)

 #conversation management

    if st.button("新建会话",width = "stretch",icon = ":material/add_circle:") and st.session_state.messages != []:
        create_conversation_file()

 # present conversation history
    list_conversation_history()



# conversation input
prompt = st.chat_input("和你的伴侣说点什么吧～")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 正确的消息顺序：system + 历史消息（含刚发的这条），按时间线排列
    api_messages = [{"role": "system", "content": f"你的名字是{st.session_state.partner_name}，{st.session_state.partner_character}，你是一个智能伴侣，你需要像伴侣一样和用户进行对话，话不冗长，但要富含情感，同时可以适当使用表情"}]
    api_messages += [{"role": m["role"], "content": m["content"]}
                     for m in st.session_state.messages
                     if m.get("role") in ("user", "assistant")]

    reply_parts = []   # 收集流式输出的每一小段

    with st.chat_message("assistant"):
        st.write_stream(stream_response())

    full_reply = "".join(reply_parts)
    if full_reply:
        st.session_state.messages.append({"role": "assistant", "content": full_reply})






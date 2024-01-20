# -*- coding: utf-8 -*-
"""
 @Author: zengp
 @Data: 2024-01-20 09:21
 @Email: zengp@kth.se
"""

import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from prompts import system_prompts
load_dotenv()
client = OpenAI()

# with st.sidebar:
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("👨‍🚀 TwinVista")
st.caption("🏤 TwinVista is a future BuildingOS")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_prompts},
                                    {"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
    else:
        st.chat_message("user").write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
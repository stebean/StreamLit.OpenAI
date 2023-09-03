import streamlit as st
from streamlit_option_menu import option_menu
import chatbot
import location


select = option_menu(
    menu_title=None,
    options=["chat", "location"],
    icons= ["chat", "geo"],
    orientation="horizontal",
)

if select == "chat":
    chatbot.chatbot()
if select == "location":
    location.location()
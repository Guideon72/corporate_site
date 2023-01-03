import streamlit as st
import pandas as pd
import mail_client as mc


st.set_page_config(page_title="Contact Us", layout="wide")


def send_mail():
    contact_user = st.session_state["address"]
    topic = st.session_state["topic"]
    body = st.session_state["content"]
    # If you fix the indentation here, the email will print everything in the subject line
    message = f"""\
Subject: New proposal inquiry

From: {contact_user}
Topic: {topic}
{body}
    """
    mc.esend(message)
    st.info("Your email was sent")


def topic_list():
    topics_df = pd.read_csv("data/topics.csv")
    topic_list = topics_df["topic"].tolist()
    # topic_list.sort()
    return topic_list


st.header("Proposals and Inquiries")

with st.form(key="email_form", clear_on_submit=True):
    st.text_input(
        label="Where can we reach you?",
        max_chars=32,
        key="address",
    )

    st.selectbox(
        "What would you like to discuss?",
        options=topic_list(),
        key="topic",
    )

    st.text_area("What is your question or proposal?", max_chars=500, key="content")

    st.form_submit_button("Send Email", on_click=send_mail)

import streamlit as st
from send_emails import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your e-mail address")
    raw_message = st.text_area("Your message")
    message = f"""Subject: New email from {user_email} \n
    From {user_email}
    {raw_message}"""
    button = st.form_submit_button("Submit")
    if button:
       send_email(message)
       st.info("You email was send sent sucessfully!")
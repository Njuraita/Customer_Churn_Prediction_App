import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load the configuration file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Instantiate the authenticator
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
    preauthorized=config['pre-authorized']
)

# Login page 
name, authentication_status, username = authenticator.login('main')

# Handle login statuses
if authentication_status:
    st.success(f"Welcome, {name}!")
elif authentication_status == False:
    st.error("Username or password is incorrect.")
elif authentication_status == None:
    st.warning("Please enter your username and password.")

import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd
from styles import Styles
from users import Users
from logs import Logs
import datetime as dt
import pytz
from connector import Database

class Layer():
    def __init__(self) -> None:
    
        self.df = pd.DataFrame(
            [
                {"command": "st.selectbox", "rating": 4, "is_widget": True},
                {"command": "st.balloons", "rating": 5, "is_widget": False},
                {"command": "st.time_input", "rating": 3, "is_widget": True},
            ]
        )
        self.edited_df = st.data_editor(self.df, num_rows="dynamic")

if __name__ == '__main__':
    layer = Layer()
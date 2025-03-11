import os
from streamlit_motor import Motor

os.environ["STREAMLIT_CONFIG_FILE"] = "./.streamlit/config.toml"

motor = Motor()

motor.welcome()
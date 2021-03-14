import streamlit as st
import pandas as pd

st.title("Valorant EDA")

df = pd.read_csv("data.csv")


option = st.sidebar.selectbox(
     "What would you like to view the graph of?",
     ['First Kills', 'First Kills by Agent'])
if option == "First Kills":
	num = st.sidebar.slider(min_value=50, max_value=112, value=50, label="Minimum number of First Kills")
	st.header("First Kills in VCT.")
	st.text("")
	st.table(df[df.Kills > num])
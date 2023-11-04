import streamlit as st
from PIL import Image
import pandas

st.set_page_config(layout="wide")
st.title("Home")
ab1,ab2 = st.columns(2)
about_me="""
Hey! Im a 15 year old kid with a passion for photography and I wanted to share some of my work 
Enjoy!
"""

with ab1:
    st.image("me.jpeg")

with ab2:
    st.title("Sohan Katragadda")
    st.write(about_me)

st.text("Below are my photographs!")

col1,empty_col, col2 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("stuff.csv", sep=";")

print(df)

with col1:
    for index, row in df[:9:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        i = row["image"]
        st.image(f"images\{i}")

with col2:
    for index, row in df[1:9:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        i = row["image"]
        st.image(f"images/{i}")
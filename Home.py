import streamlit as st
from PIL import Image
import pandas

st.set_page_config(layout="wide")
st.title("Home")
ab1,ab2 = st.columns(2)
about_me="""
My name is Sohan, I'm 15 years old and I recently picked up analogue photography.
I never really considered myself to be the artistic kind as a kid.
Clumsy with pencils and paintbrushes, I stopped exploring after I realised my limits were stuck to poorly made stick figures.
However, during the pandemic, my restlessness led me to find my dad's old camera.

For an entire year, I was deadset on repairing that camera, finding someone who still sells film, someone to develop that film and so on and so forth.
Long story short, I ended up having to buy a new camera because I later found out that whatever issue it had, it was unrepairable.

That brings us to my first roll of film that I shot back in June.
I had never really used a camera of any kind other than the one on my phone and the lack of instant feedback is something which taught me to have foresight and be patient.
I waited a month for the film to get developed and scanned, and I found that the anticipation and need to be precise in what I shoot (as it's not a cheap medium) paid back tenfold when I received my photos. 

I was hooked.

In the 6 months since I started, I have consumed loads and loads of information, from the technical aspects of film to even portraits by Raja Ravi Varma to open my mind on how I look at things.
Even though it's an extremely cliched line, it did open up a whole new world for me- a way to show others what I saw, what I felt.
This is something I definitely want to keep working on and have fun with

New Portfolio:- https://1drv.ms/f/s!Any01Ygv8cwTjimUaNIWyUHhvfMI?e=clDh6D
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
        st.image(f"images/{i}")

with col2:
    for index, row in df[1:9:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        i = row["image"]
        st.image(f"images/{i}")
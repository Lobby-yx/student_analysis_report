import pandas as pd
import streamlit as st

st.title("Student performance Analysis")

df =pd.read_csv("stuydent.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset summary")
st.write(df.describe())

if st.button("show Dataset"):
   st.dataframe(df)

min_score = st.slider("select minimun score", 0, 100, 50)
filtered_df =df["score"] >= min_score
st.dataframe(filtered_df)

uploaded_file = st.file_uploader("upload csv file")

if uploaded_file:
    df = pd.read_csv("uploaded_file")
st.dataframe(df)

st.bar_chart(df["age"].value_counts())
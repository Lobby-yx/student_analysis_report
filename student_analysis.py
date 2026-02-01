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


st.bar_chart(df["gender"].value_counts())

st.line_chart(df["score"])
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["score"])
st.pyplot(fig)
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dataset", "Summary", "Visualizations"]
)
if option == "Dataset":
    st.dataframe(df)

elif option == "Summary":
    st.write(df.describe())

elif option == "Visualizations":
    st.bar_chart(df["gender"].value_counts())

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="EDA", layout="wide")
st.title("# EDA - Exploratory Data Analysis 🔍")

df=pd.read_csv("data/cleaned_survey_data.csv")

st.subheader("Summary of the data is:")
st.write(df.describe())

st.subheader("Shape of Dataset is:")
st.write(df.shape)
st.subheader("Datatypes of features are:")
st.write(df.dtypes)
st.subheader("Missing/Null values:")
st.write(df.isnull().sum())

st.write("First 5 Rows:")
st.dataframe(df.head())

st.subheader("Categorical Feature Distribution")
cat_col=st.selectbox("Select a categorical column:", df.select_dtypes(include=['object']).columns)
fig, ax = plt.subplots()
sns.countplot(data=df, x=cat_col, order=df[cat_col].value_counts().index, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Numeric Feature Distribution")
num_col = st.selectbox("Select a numerical column:", df.select_dtypes(include=['int64','float64']).columns)
fig, ax = plt.subplots()
sns.histplot(df[num_col], kde=True, ax=ax)
st.pyplot(fig)
import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Prediction My Career Project')
st.header('Data Visualization')
mydata = pd.read_csv('career.csv')

st.write(mydata.head())
# Printing the dataset shape
st.subheader('Number of Data Shape')
#target class histogram
st.header('Observation')
fig = px.histogram(mydata['Suggested Job Role'])
st.plotly_chart(fig)
st.markdown('This histogram looks like bell shaped that is a normal distribution')
#category value count
st.subheader('Total values counts of Category Data')
catlist=mydata.select_dtypes(include=['object']).columns.tolist()
categorical_col = mydata[catlist]
for i in categorical_col:
    category_df = mydata[i].value_counts()
    st.dataframe(category_df)
dfchurn=mydata.groupby(['Suggested Job Role'])[['Introvert']].value_counts()

fig = px.histogram(dfchurn)
st.plotly_chart(fig)

import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Data Visualization')

st.write('Prediction My Career project')
mydata = pd.read_csv(r'C:\Users\Dell\Documents\tytsan\batch5\career.csv')

mydata
# Printing the dataset shape
st.subheader('Number of Data Shape')
mydata.shape


st.subheader('Total values counts of Category Data')
catlist=mydata.select_dtypes(include=['object']).columns.tolist()
categorical_col = mydata[catlist]
for i in categorical_col:
    category_df = mydata[i].value_counts()
    st.dataframe(category_df)

#Create a heatmap to visualize correlation
corr_matrix = mydata.apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1)#to convert categorical values in each column of mydata into numerical labels using factorize()
st.write(corr_matrix)


hmap=px.imshow(corr_matrix, text_auto=True)
st.plotly_chart(hmap)
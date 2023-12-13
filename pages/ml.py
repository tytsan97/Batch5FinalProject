import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
rfmodel= st.sidebar.checkbox('Decision Trees')
data = pd.read_csv('career.csv')
st.title('Classify the new career prediction')
st.subheader("Please Choose all features for predicting good result")
logic_rate=st.number_input('Pick a number for Logical Rating',1,9)
hack_rate = st.number_input('Pick a number for hackathons',1,9)
code_rate = st.number_input('Pick a number for coding skills rating',1,9)
speak_rate = st.number_input('Pick a number for public speaking points',1,9)
self_learn = st.radio("Self Learning Capability:", ['yes', 'no'])
extra_course = st.radio("Extra Course:", ['yes', 'no'])
certificate = st.selectbox("Certifications:", ['information security', 'shell programming', 'r programming', 'distro making', 'machine learning', 'full stack', 'hadoop', 'app development', 'python'])
wshop = st.selectbox("Workshop:", ['testing', 'database security', 'game development', 'data science', 'system designing', 'hacking', 'cloud computing', 'web technologies'])
rw_skill = st.selectbox("Read and Write Skill",['poor', 'excellent', 'medium'])
memory_score = st.selectbox("Memory capability score:",['poor', 'excellent', 'medium'])
like_subj = st.selectbox("Interesting Subjects:",data['Interested subjects'].unique())
like_area = st.selectbox("Interesting Career Area:",['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'])
like_com = st.selectbox("Type of company want to settle in:",['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'])
takein_snr = st.radio("Taken inputs from seniors or elders:",['no','yes'])
like_book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())
mana_tech = st.radio("Tech or Manage:",['Management','Technical'])
worker = st.radio("Hard or Smart:",['smart worker', 'hard worker'])
team = st.radio("work in team ever?",['no','yes'])
mbti = st.radio("Are you Inrovert:",['no','yes'])

st.write("You selected:",logic_rate + hack_rate +code_rate +speak_rate +self_learn +extra_course+ certificate+ wshop+ rw_skill+ memory_score +like_subj+like_area+like_com+takein_snr+like_book+mana_tech+worker+team+mbti)
        
       

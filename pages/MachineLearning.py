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
self_learn = st.radio("Self Learning Capability:If yes=1 else 0", [1,0])
extra_course = st.radio("Extra Course:If yes=1 else 0", [1,0]) 
certificate = st.selectbox("Certificate:",[0,1,2,3,4,5,6,7,8])
wshop = st.selectbox("Workshop:", [0,1,2,3,4,5,6,7])
rw_skill = st.radio("Read and Write Skill Excellent=0,Medium=1,Poor=2", [0,1,2])
memory_score = st.radio("Memory capability Excellent=0,Medium=1,Poor=2",[0,1,2])
like_subj = st.number_input("Interesting Subjects:",0,9)
like_area = st.number_input("Interesting Career Area",0,5)
takein_snr = st.radio("Take in input from senior IF yes=1 or 0",[0,1])
like_com = st.number_input("Type of company choice",0,9)
like_book = st.number_input('Pick a number code for interested type of book',0,30)
mana_tech = st.radio("Tech=1 or Manage=0:",[0,1])
worker = st.radio("Hard=1 or Smart=0:",[0,1])
team = st.radio("work in team ever?if yes choice 1",[1,0])
mbti = st.radio("Are you Inrovert:if yes choice 1",[1,0])
st.write("Your Logic, Hackaton, Coding Skill and Public Speaking points:",logic_rate,hack_rate,code_rate,speak_rate)
st.write("Your selected:",self_learn,extra,certificate,workshop,rw_skill,memory_score,like_subj,like_area,like_com,
         takein_snr,like_book,mana_tech,worker,team,mbti)
        
       

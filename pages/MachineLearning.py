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
if self_learn == "yes":
         new_self = 1
else :
         new_self = 0
st.write(new_self)
extra = st.radio("Extra Course:",['yes', 'no'])
if extra == "yes":
         new_extra = 1
else :
         new_extra = 0
st.write(new_extra)
snrinput = st.radio("Take in input from senior",['yes','no'])
if snrinput == "yes":
         new_snrin = 1
else :
         new_snrin = 0
st.write(new_snrin)
team = st.radio("Work team in ever?",['yes','no'])
if team == "yes":
         new_team = 1
else :
         new_team = 0
st.write(new_team)
mbti = st.radio("Are you introverted",['yes','no'])
if mbti == "yes":
         new_mbti = 1
else :
         new_mbti = 0
st.write(new_mbti)
certi = st.selectbox("Certificate",data['certifications'].unique()) 
#new_certi = certi.astype('category').cat.codes
st.write(new_certi)
wshop = st.selectbox("Workshops",data['workshops'].unique())
subj = st.selectbox("Interesting Subjects",data['Interested subjects'].unique())
area = st.selectbox("Interesting Working Area",data['interested career area '].unique())
comp = st.selectbox("What type of company settle in",data['What type of company want to settle in?'].unique())
book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())
#self_learn = st.number_input("Self Learning Capability:If yes=1 else 0", 0,1)
#extra = st.number_input("Extra Course:If yes=1 else 0", 0,1) 
#certificate = st.number_input("Certificate:",0,8)
#wshop = st.number_input("Workshop:", 0,7)
#rw_skill = st.number_input("Read and Write Skill Excellent=0,Medium=1,Poor=2", 0,2)
#memory_score = st.number_input("Memory capability Excellent=0,Medium=1,Poor=2",0,2)
#like_subj = st.number_input("Interesting Subjects:",0,9)
#st.subheader("Interesting Career Area")
#st.markdown("0-Business Process Analyst") 
#st.markdown("1-Cloud Computing")
#st.markdown("2-Developer")
#st.markdown("3-Security")
#st.markdown("4-System Developer")
#st.markdown("5-Testing")
#like_area = st.number_input("Interesting Career Area",0,5)
#takein_snr = st.number_input("Take in input from senior IF yes=1 or 0",0,1)
#like_com = st.number_input("Type of company choice",0,9)
#like_book = st.number_input('Pick a number code for interested type of book',0,30)
#like_book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())
#mana_tech = st.number_input("Tech=1 or Manage=0:",0,1)
#worker = st.number_input("Hard=1 or Smart=0:",0,1)
#team = st.number_input("work in team ever?if yes choice 1",0,1)
#mbti = st.number_input("Are you Inrovert:if yes choice 1",0,1)
st.write("Your Logic, Hackaton, Coding Skill and Public Speaking points:",logic_rate,hack_rate,code_rate,speak_rate)
#st.write(self_learn,extra,certificate,wshop,rw_skill,memory_score,like_subj,like_area,like_com,takein_snr,like_book,mana_tech,worker,team,mbti)
        
       

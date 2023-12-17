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
rdwe = st.selectbox("Reading or Writing Skill",['Excellent','Medium','Poor'])
if rdwe == "Excellent":
         new_rdwe = 0
elif rdwe == "Medium":
         new_rdwe = 1
else:
         new_rdwe = 2
st.write(new_rdwe)
memo = st.selectbox("Memory Capability Skill", ['Excellent','Medium','Poor'])
if memo == "Excellent":
         new_memo = 0
elif memo == "Medium":
         new_memo = 1
else:
         new_memo = 2
st.write(new_memo)
metl = st.radio("Choice Management or Technical",['Management', 'Technical']) 
if metl == 'Management':
         new_metl = 0
else:
         new_metl = 1
st.write(new_metl)
work = st.radio("Choice Smart or Hard",['Smart Worker','Hard Worker'])
if work == 'Smart Worker':
         new_work = 0
else:
         new_work = 1
st.write(new_work)
certi = st.selectbox("Certificate",data['certifications'].unique()) 
data['certifications']=data['certifications'].astype('category')
d=dict(enumerate(data['certifications'].cat.categories))
for key,value in d.items():
    if value == certi:
        new_certi=key
st.write(new_certi)
wshop = st.selectbox("Workshops",data['workshops'].unique())
subj = st.selectbox("Interesting Subjects",data['Interested subjects'].unique())
area = st.selectbox("Interesting Working Area",data['interested career area '].unique())
comp = st.selectbox("What type of company settle in",data['Type of company want to settle in?'].unique())
book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())

inputdata = {'Logical quotient rating': logic_rate,
                        'hackathons': hack_rate,                         
                        'coding skills rating': code_rate,
                        'public speaking points': speak_rate,
                        'self-learning capability?': new_self,
                        'Extra-courses did': new_extra,
                        'certifications_code': new_certi,
                        'workshops_code': wshop,
                        'reading and writing skills': new_rdwe,
                        'memory capability score': new_memo,
                        'Interested subjects_code': subj,
                        'interested career area _code': area,
                        'Type of Companay want to settle in?':comp,
                        'Taken inputs from seniors or elders':new_snrin,
                        'Interested Type of Books_code': book,
                        'Management or Technical': new_metl,
                         'hard/smart worker': new_work,
                          'worked in teams ever?': new_team,
                           'Introvert': new_mbti}

features = pd.DataFrame(inputdata, index=[0])
st.write(features)

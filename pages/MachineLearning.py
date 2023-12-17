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

extra = st.radio("Extra Course:",['yes', 'no'])
if extra == "yes":
         new_extra = 1
else :
         new_extra = 0
#st.write(new_extra)
snrinput = st.radio("Take in input from senior",['yes','no'])
if snrinput == "yes":
         new_snrin = 1
else :
         new_snrin = 0
#st.write(new_snrin)
team = st.radio("Work team in ever?",['yes','no'])
if team == "yes":
         new_team = 1
else :
         new_team = 0
#st.write(new_team)
mbti = st.radio("Are you introverted",['yes','no'])
if mbti == "yes":
         new_mbti = 1
else :
         new_mbti = 0
#st.write(new_mbti)
rdwe = st.selectbox("Reading or Writing Skill",['Excellent','Medium','Poor'])
if rdwe == "Excellent":
         new_rdwe = 0
elif rdwe == "Medium":
         new_rdwe = 1
else:
         new_rdwe = 2
#st.write(new_rdwe)
memo = st.selectbox("Memory Capability Skill", ['Excellent','Medium','Poor'])
if memo == "Excellent":
         new_memo = 0
elif memo == "Medium":
         new_memo = 1
else:
         new_memo = 2
#st.write(new_memo)
metl = st.radio("Choice Management or Technical",['Management', 'Technical']) 
if metl == 'Management':
         new_metl = 0
else:
         new_metl = 1
#st.write(new_metl)
work = st.radio("Choice Smart or Hard",['Smart Worker','Hard Worker'])
if work == 'Smart Worker':
         new_work = 0
else:
         new_work = 1
#st.write(new_work)
certi = st.selectbox("Certificate",data['certifications'].unique()) 
data['certifications']=data['certifications'].astype('category')
d=dict(enumerate(data['certifications'].cat.categories))
for key,value in d.items():
    if value == certi:
        new_certi=key
#st.write(new_certi)
wshop = st.selectbox("Workshops",data['workshops'].unique())
data['workshops']=data['workshops'].astype('category')
w=dict(enumerate(data['workshops'].cat.categories))
for key,value in w.items():
    if value == wshop:
        new_wshop=key
#st.write(new_wshop)
subj = st.selectbox("Interesting Subjects",data['Interested subjects'].unique())
data['Interested subjects']=data['Interested subjects'].astype('category')
s=dict(enumerate(data['Interested subjects'].cat.categories))
for key,value in s.items():
    if value == subj:
        new_subj=key
#st.write(new_subj)
area = st.selectbox("Interesting Working Area",data['interested career area '].unique())
data['interested career area ']=data['interested career area '].astype('category')
a=dict(enumerate(data['interested career area '].cat.categories))
for key,value in a.items():
    if value == area:
        new_area=key
#st.write(new_area)
comp = st.selectbox("What type of company settle in",data['Type of company want to settle in?'].unique())
data['Type of company want to settle in?']=data['Type of company want to settle in?'].astype('category')
c=dict(enumerate(data['Type of company want to settle in?'].cat.categories))
for key,value in c.items():
    if value == comp:
        new_comp=key
#st.write(new_comp)
book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())
data['Interested Type of Books']=data['Interested Type of Books'].astype('category')
b=dict(enumerate(data['Interested Type of Books'].cat.categories))
for key,value in b.items():
    if value == book:
        new_book=key
#st.write(new_book)
inputdata = {'Logical quotient rating': logic_rate,
                        'hackathons': hack_rate,                         
                        'coding skills rating': code_rate,
                        'public speaking points': speak_rate,
                        'self-learning capability?': new_self,
                        'Extra-courses did': new_extra,
                        'certifications_code': new_certi,
                        'workshops_code': new_wshop,
                        'reading and writing skills': new_rdwe,
                        'memory capability score': new_memo,
                        'Interested subjects_code': new_subj,
                        'interested career area _code': new_area,
                        'Type of Companay want to settle in?':new_comp,
                        'Taken inputs from seniors or elders':new_snrin,
                        'Interested Type of Books_code': new_book,
                        'Management or Technical': new_metl,
                         'hard/smart worker': new_work,
                          'worked in teams ever?': new_team,
                           'Introvert': new_mbti}

features = pd.DataFrame(inputdata,index=[0])
st.write(features)
catlist = data.select_dtypes(include=['object']).columns
st.write(catlist)
st.write(data.info())
st.write(data.columns)

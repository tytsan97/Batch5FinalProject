import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
rfmodel= st.sidebar.checkbox('Decision Trees')
data = pd.read_csv('career.csv')
if rfmodel: 
    with st.form("my_form1"):     
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
        snrinput = st.radio("Take in input from senior",['yes','no'])
        if snrinput == "yes":
            new_snrin = 1
        else :
            new_snrin = 0
        team = st.radio("Work team in ever?",['yes','no'])
        if team == "yes":
            new_team = 1
        else :
            new_team = 0
        mbti = st.radio("Are you introverted",['yes','no'])
        if mbti == "yes":
            new_mbti = 1
        else :
            new_mbti = 0
        rdwe = st.selectbox("Reading or Writing Skill",['Excellent','Medium','Poor'])
        if rdwe == "Excellent":
            new_rdwe = 0
        elif rdwe == "Medium":
            new_rdwe = 1
        else:
            new_rdwe = 2
        memo = st.selectbox("Memory Capability Skill", ['Excellent','Medium','Poor'])
        if memo == "Excellent":
            new_memo = 0
        elif memo == "Medium":
            new_memo = 1
        else:
            new_memo = 2
        metl = st.radio("Choice Management or Technical",['Management', 'Technical']) 
        if metl == 'Management':
            new_metl = 0
        else:
            new_metl = 1
        work = st.radio("Choice Smart or Hard",['Smart Worker','Hard Worker'])
        if work == 'Smart Worker':
            new_work = 0
        else:
            new_work = 1
        certi = st.selectbox("Certificate",data['certifications'].unique()) 
        data['certifications']=data['certifications'].astype('category')
        d=dict(enumerate(data['certifications'].cat.categories))
        for key,value in d.items():
            if value == certi:
                new_certi=key
        wshop = st.selectbox("Workshops",data['workshops'].unique())
        data['workshops']=data['workshops'].astype('category')
        w=dict(enumerate(data['workshops'].cat.categories))
        for key,value in w.items():
            if value == wshop:
                new_wshop=key
        subj = st.selectbox("Interesting Subjects",data['Interested subjects'].unique())
        data['Interested subjects']=data['Interested subjects'].astype('category')
        s=dict(enumerate(data['Interested subjects'].cat.categories))
        for key,value in s.items():
            if value == subj:
                new_subj=key
        area = st.selectbox("Interesting Working Area",data['interested career area '].unique())
        data['interested career area ']=data['interested career area '].astype('category')
        a=dict(enumerate(data['interested career area '].cat.categories))
        for key,value in a.items():
            if value == area:
                new_area=key         
        comp = st.selectbox("What type of company settle in",data['Type of company want to settle in?'].unique())
        data['Type of company want to settle in?']=data['Type of company want to settle in?'].astype('category')
        c=dict(enumerate(data['Type of company want to settle in?'].cat.categories))
        for key,value in c.items():
            if value == comp:
                new_comp=key
        book = st.selectbox("Interesting type of book:",data['Interested Type of Books'].unique())
        data['Interested Type of Books']=data['Interested Type of Books'].astype('category')
        b=dict(enumerate(data['Interested Type of Books'].cat.categories))
        for key,value in b.items():
            if value == book:
                new_book=key
        submitted = st.form_submit_button("Submit")
        if submitted:
            inputdata = {'Logical quotient rating': logic_rate,'hackathons': hack_rate,                         
                         'coding skills rating': code_rate,'public speaking points': speak_rate,
                         'self-learning capability?': new_self,'Extra-courses did': new_extra,
                         'certifications_code': new_certi,'workshops_code': new_wshop,
                         'reading and writing skills': new_rdwe,'memory capability score': new_memo,
                         'Interested subjects_code': new_subj,'interested career area _code': new_area,
                         'Type of Companay want to settle in?':new_comp,'Taken inputs from seniors or elders':new_snrin,
                         'Interested Type of Books_code': new_book,'Management or Technical': new_metl,
                        'hard/smart worker': new_work,'worked in teams ever?': new_team,'Introvert': new_mbti}                  
            features = pd.DataFrame(inputdata,index=[0])         
            x=data.drop("Suggested Job Role",axis=1)
            y=data["Suggested Job Role"]
            cols= ['self-learning capability?','Extra-courses did',
                   'certifications','workshops','reading and writing skills',
                   'memory capability score','Interested subjects', 'interested career area ',
                   'Type of company want to settle in?','Taken inputs from seniors or elders',
                   'Interested Type of Books','Management or Technical','hard/smart worker',
                   'worked in teams ever?','Introvert']
            for i in cols:
                x[i]=x[i].astype('category').cat.codes
            x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=25)
            dtmodel = DecisionTreeClassifier(criterion='entropy').fit(x_train,y_train)
            dt_pred = dt_model.predict(features)
            st.write(dt_pred)        
            #clfres = p.predict(features)    
            st.subheader("Your suggested job role is")
            #st.write(x_train)
         

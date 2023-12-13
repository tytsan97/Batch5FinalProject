import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
rfmodel= st.sidebar.checkbox('Decision Trees')
data = pd.read_csv('career.csv')

if rfmodel:
    
    with st.form("my_form1"):
        
        st.title('Classify the new career prediction')
        st.subheader("Please Choose all features for predicting good result")
        logic_rate=st.slide('Pick a number for Logical Rating',1,9)
        hack_rate = st.slide('Pick a number for hackathons',1,9)
        code_rate = st.slide('Pick a number for coding skills rating',1,9)
        speak_rate = st.slide('Pick a number for public speaking points,1,9)
        self_learn = st.radio("Self Learning Capability:", ['yes', 'no'])
        extra_course = st.radio("Extra Course:", ['yes', 'no'])
        #agegp = st.selectbox("What's customer Age:", ['youth', 'middle_aged', 'senior'])
        certificate = st.selectbox("Certifications:", ['information security', 'shell programming', 'r programming', 'distro making', 'machine learning', 'full stack', 'hadoop', 'app development', 'python'])
        wshop = st.selectbox("Workshop:", ['testing', 'database security', 'game development', 'data science', 'system designing', 'hacking', 'cloud computing', 'web technologies'])
        rw_skill = st.selectbox("Read and Write Skill",['poor', 'excellent', 'medium'])
        memory_score = st.selectbox("Memory capability score:",['poor', 'excellent', 'medium'])
        like_subj = st.selctbox("Interesting Subjects:",['programming', 'Management', 'data engineering', 'networks', 'Software Engineering', 'cloud computing', 'parallel computing', 'IOT', 'Computer Architecture', 'hacking'])
        like_area = st.selctbox("Interesting Career Area:",['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'])
        like_com = st.selctbox("Type of company want to settle in:",['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'])
        takein_snr = st.radio("Taken inputs from seniors or elders:",['no','yes'])
        like_book = st.selctbox("Interesting type of book:",data['Interested Type of Books'].unique())
        mana_tech = st.radio("Tech or Manage:",['Management','Technical'])
        worker = st.radio("Hard or Smart:",['smart worker', 'hard worker'])
        team = st.radio("work in team ever?",['no','yes'])
        mbti = st.radio("Are you Inrovert:",['no','yes'])
    
        
        st.write("You selected:", "Age:" + agegp + "Student:" + student)
    
    
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            #st.write("slider", slider_val, "checkbox", checkbox_val)
            inputdata = {'age': agegp,
                        'studen': student, 
                        'income': income,
                        'credit rating': credit_rating}
            features = pd.DataFrame(inputdata, index=[0])
            features_dummy = pd.get_dummies(features)
            #st.write(features)
            #################################################
            
            X = data[['age', 'income', 'studen', 'credit rating']]
            y = data[['class']]
            X_dummies = pd.get_dummies(X)
            X_train, X_test, y_train, y_test = train_test_split(X_dummies,y,test_size=0.25, random_state=25)
            ##################################################
            # load model
            filename = 'C:/Users/Dell/Documents/tytsan/prjsample/test1'
            loaded_model = pickle.load(open(filename, "rb"))
            testsdata1=pd.get_dummies(features_dummy)
            testsdata2 =  testsdata1.reindex(columns =  X_train.columns, fill_value=0)
            clfres = loaded_model.predict(testsdata2)
            if clfres == 'yes':
                st.write('The customer will buy the computer')
            else:
                st.write('The customer will not buy the computer')
            
           
            
          

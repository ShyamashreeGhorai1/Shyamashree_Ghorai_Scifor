#1. What is Streamlit, and how does it differ from other web frameworks?
# Ans.
'''
Streamlit is an open-source framework for building interactive, data-driven applications in Python.
It provides a simple, easy-to-use interface for creating beautiful, interactive web apps with just
a few lines of Python code.
    

Streamlit is designed in such way  that it requires minimal code to create interactive web apps.
This is because it handles automatically the underlying web developement tasks, such as generating
HTML,CSS and JavaScript code.

'''


#2. Explain the basic structure of a Streamlit app.
# Ans.
'''
1. Project planning
2. Install required libraries
3. Data Collection
4. Sketch web app
5. Build main functions and additional features
6. Commit to Github
7. Deploy the app from streamlit.io/cloud
'''


#3. How can you add a title to your Streamlit app?
#Ans.
'''
For add any title to our streamlit app, we can use the following command:
st.title('title name')
For example:
'''
import streamlit as st
st.title('Plotting App')


#4. What is the purpose of the st.write() function in Streamlit?
#Ans.
'''
If we want to print or display anything in our page, then we can use the
st.write() function in streamlit.
'''
st.write("Please, enter your name.")


#5.How do you create interactive widgets in Streamlit? Provide examples.
#Ans
'''
Using widgets, we can create interactivity in streamlit app.
For example
'''
import streamlit as st
st.button("Click")
st.checkbox("Submit")
st.radio('Pick your gender',['Male','Female','Other'])
st.multiselect('Choose the travel spot',['Darjeeling','Sikim','Bhutan'])
st.selectbox('Pick Your course',['Data Science','Cloud Computing','Cyber Security'])
st.text_input('Enter your name')
st.text_area('Describe the reason')

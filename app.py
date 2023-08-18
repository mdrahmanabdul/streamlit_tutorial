import streamlit as st

#side bar
st.sidebar.header("About")
st.sidebar.text("This is my streamlit project")

#algorithms
algorithms = st.sidebar.selectbox("Algorithms",["Linear Regression","Logistic Regression","Decision Tree"])

#title
st.title("Welcome to Streamlit Tutorial")

#header
st.header("One stop destination ")

#sub-header
st.subheader("to learn each and everything about Streamlit")

#text
st.title("What is Streamlit ?")

#markdown
streatlit_def = "Streamlit is an open-source Python library that allows developers to create web applications for data visualization and analysis with minimal effort. It's designed to turn data scripts into shareable web apps with a few lines of Python code. Streamlit is particularly popular among data scientists, engineers, and researchers who want to quickly create interactive and visually appealing dashboards or applications to showcase their data and analyses."
st.markdown(streatlit_def)

#info
st.success("If the task is done")
st.info("Please practice streamlit to become master of it")
st.error("If the task is not done")
st.warning("Warning will be displayed in this colour")
st.exception("NameError('Name is not defined')")

#help
import pandas
#st.help(pandas) #Will print the pandas documentation

st.help(range) #will get help for range function

#write #1
name = "Mohammed Abdul Rahman"
age = 22
st.write("Name : ",name)
st.write("Age : ",age)

#2
fruits = ["Apple",'Cherry',"Bananas","Papaya"]
st.write("List of fruits : ",fruits)

#image
from PIL import Image
img = Image.open("streamlit.png")
st.image(img,caption="This is streamlit logo")


#balloons
#st.balloons()

vid_path = "/Users/rahman/Desktop/Streamlit/sample.mp4"
st.video(vid_path,start_time=1)

video_url = "https://www.youtube.com/watch?v=Bnsbbzkct58"
st.video(video_url)


#audio file
aud_file = open("evare.mp3","rb").read()
st.audio(aud_file)

#checkbox
if st.checkbox("show/hide"):
    st.text("Showing or hiding widget")

option = st.checkbox("Enable Feature")
if option:
    st.write("Feature is enabled")
else:
    st.write("Feature disabled")



#radio buttons
status = st.radio("What is your status",("Active","Inactive"))
if status=="Active":
    st.success("You are active")
else :
    st.error("You are inactive")


#select box
occupation = st.selectbox("Select your occupation",["Programmer","Data scientist","Doctor","Businessman"])
st.write("You selected {} occupation".format(occupation))

#multiselect
location_pref = st.multiselect("Choose your preferences",("Karnataka","Bangalore","Hyderabad","Chennai"))
st.write("You selected",len(location_pref),"locations")

#slider
exp_lev = st.slider("Years of experience you have",1,5)

#simple button
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is cool")

if st.button("Submit"):
    st.success("Successfully Submitted")

#Text input
f_name = st.text_input("Enter your first name","Type here...")
if st.button("Submit",key=1):
    st.success("name submitted")

#text area
message = st.text_area("Enter your message", "Type here..")
if st.button("Submit", key = "2"):
    st.success("Message submitteed")

#date and time
import datetime
today = st.date_input("Today is ",datetime.datetime.now())

time = st.time_input("Select time ",value=None)


#json output
st.text("Display json data")
st.json({
    "Name" : "Rahman",
    "Age" : 23,
    "Gender" : "Male"
});

#display code
st.text("Display raw code");
st.code("import numpy as np")

#Progress bar
import time
my_bar = st.progress(0)
for p in range(101):
    time.sleep(0.1)
    my_bar.progress(p)
    if p==100:
        st.success("Process completed")


#spinner
with st.spinner("Waiting..."):
    time.sleep(5) #->spins for 5 seconds
    st.success("Finished!")


#file uploader
uploaded_file = st.file_uploader("Choose a file",type=["csv","xlsv"])

if uploaded_file is not None:
    st.spinner("uploading...")
    time.sleep(3)
    st.success("File uploaded successfully")
else:
    st.error("File not uploaded")
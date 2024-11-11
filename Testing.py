import streamlit as st
import pandas as pd
import numpy as np
import time



st.title("Pritesh (Title)")
st.header(":green[Dinesh] (Header)")
st.subheader(":blue[hello(Subheader)]")
st.write(":red[Shinde] (Text)")
st.markdown("Karan (markdown)")
st.caption(":orange[Sahil] (caption)")

st.write("#")
st.subheader(":blue[Image (Subheader)]")
st.image("D:/5ME GenAi/Stream/car1.jpg")
st.write("#")
st.subheader(":blue[Audio (Subheader)]")
st.audio("D:/5ME GenAi/Stream/song1.wav", format="audio/wav", loop=False)
st.write("#")
st.subheader(":blue[Video (Subheader)]")
st.video("D:/5ME GenAi/Stream/sample1.mkv")

agree = st.checkbox('I agree to the given conditions. (checkbox)')
#specifying what should be displayed if the check box is selected
if agree:
    st.write('Welcome Buddyyy!!')



if st.button('Wish Good morning (button)'):
     st.write('Good Morning Sir') #displayed when the button is clicked


st.radio("Pick your fav Car: (radio Tag)",['Toyota','Audi','JEEp','BMW','Skoda'])
st.button("Press Ok")


st.selectbox("Pick your Language: (SELECTBOX)",["py","c++","c","JAVA",])
st.button("Press ok")



st.multiselect("Pick Your Fav Food: (MULTISELECT)",["Biryani","Soup","Chinese","ArabianFood"])


st.select_slider(":red[Rate us:] (SELECT_SLIDER)",["Bad","Good","Excellent"])

st.slider("Remark from 0 to 100 (SLIDER)", 0,100)

on = st.toggle("Activate Feature: (toggle)")
if on:
     st.write("Feature is Activated!!!")
else:
     st.write("Feature is Deactivated!!!")


number = st.number_input("Insert valid number: (number_input)")
st.write("Your Current number is ",number)



d= st.date_input("What's ur birthday: (date_input)",value = None)
st.write("Ur Birth Date is ",d)

t = st.time_input("Set Alarm: (time_input)",value = None)
st.write("Alarm Is Set To",t)




st.number_input("Enter marks from 0 to 100:", 0,100)
st.text_input("Enter text: ")
st.time_input("Exam time: ")
st.date_input("Exam date: ")
st.text_area('Description: ')
st.file_uploader("Upload file: ")
st.color_picker("Pick Color: ")





st.success('Succesfull')
st.error('Error')
st.warning('Warning!!!')
st.info('Information')
st.exception(RuntimeError('Runtime Error'))

st.sidebar.title("Welcome Dosto")
st.sidebar.image("D:/5ME GenAi/Stream/car1.jpg")
st.markdown("##")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(1,21)))
st.dataframe(df)


df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "45 °F", "1.4 °F")
col2.metric("Wind", "10 mph", "-5%")
col3.metric("Humidity", "36%", "6%")
col4.metric("Snow","78%","25%")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")




with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")




'''
st.write("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)


st.write("Bar Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)



st.write("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
'''


df = pd.DataFrame(
    np.random.randn(1000, 2) / [70, 60] + [47.76, -100.4],
    columns=['lat', 'lon'])
st.map(df)




'''chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data) '''




with st.chat_message("user"):
    st.write("Hello ji")
import streamlit as st
import mediapipe as mp
import cv2 as cv
import numpy as np
import tempfile
import time
from PIL import Image

st.title("Fit Mate")

add_selectbox = st.sidebar.selectbox(
        "Please do select the options below",
        ("Home Page", "Squats Tracker" , "Knee Exercise Tracker" , "Push Ups Tracker")
    )

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![IOT Project Team]'
                '(https://img.shields.io/badge/Author-IOT%20Team-brightgreen)]'
                '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("J Component Project IOT")

if add_selectbox == "Home Page":
    st.image("homepage.webp")
    st.write('''Despite the many benefits of regular exercise, many people struggle to maintain proper 
    form and technique while working out. This can lead to ineffective workouts, lack of progress, 
    and even injury. To address this problem, we aim to create a web application using streamlit 
    python for exercise tracking, correction, and guidance, using the mediapipe library for real-time 
    movement analysis. Our application will provide users with real-time feedback on their exercise form 
    and technique, detect errors and provide corrective suggestions, and guide users through personalized exercise 
    routines. By using our application, users will be able to achieve more effective and safer workouts, leading to 
    improved fitness and reduced risk of injury.''')

if add_selectbox == 'Squats Tracker':

    st.title('Fitness Trainer: Squats Analysis')


    recorded_file = 'output_sample.mp4'
    sample_vid = st.empty()
    sample_vid.video(recorded_file)

    st.write("""The squat exerciser corrector is a device algorithm to help users maintain proper form while performing squats. It consists of a waist belt with sensors that detect the angle and position of the user's hips, and a companion app that provides real-time feedback on their form. If the user's form is incorrect, the app will alert them with a warning and provide tips on how to adjust their posture. With regular use, the squat exerciser corrector can help users improve their squatting technique and avoid injury.""")

if add_selectbox == "Knee Exercise Tracker":
    st.image("KneeImage.jpeg")

    st.title('Fitness Trainer: Knee Analysis')

    st.write("""The knee exerciser corrector is a device algorithm to help users perform knee exercises with proper form and alignment. It consists of a leg strap with sensors that detect the angle and position of the user's knee, and a companion app that provides real-time feedback on their form. If the user's form is incorrect, the app will alert them with a warning and provide tips on how to adjust their posture. With regular use, the knee exerciser corrector can help users improve their knee exercise technique, avoid injury, and strengthen their knees.""")

if add_selectbox == "Push Ups Tracker":
    st.image("PushUps.webp")
    st.title('Fitness Trainer: Knee Analysis')
    st.write("""The push-up exerciser corrector is a algorithm designed to help users perform push-ups with proper form and alignment. It uses deep learning algorithms to analyze the user's movements and provide real-time feedback on their form. The device consists of a camera that captures the user's push-up movements, and a companion app that uses deep learning models to analyze the video and provide feedback. If the user's form is incorrect, the app will alert them with a warning and provide tips on how to adjust their posture. With regular use, the push-up exerciser corrector can help users improve their push-up technique, avoid injury, and build upper body strength.""")
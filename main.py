import numpy 
import cv2 as cv
import streamlit as st

path = "https://www.youtube.com/watch?v=ESIZ0CRswnE"

f_bytes  = open('sample-10s.mp4', 'rb')
video = f_bytes.read()

st.video(video)

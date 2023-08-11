import streamlit as st
import pandas as pd
import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr

def save_uploadedfile(uploadedfile):
     with open(os.path.join(uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
#     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

def convert_video2audio(video):
	AUDIO_FILE = video.audio
	AUDIO_FILE.write_audiofile('audio.wav')


def transcript_audio():
	audio_file = "audio.wav"	
	r = sr.Recognizer()
	with sr.AudioFile(audio_file) as source:
		audio = r.record(source)  # read the entire audio file

	recognized_text = r.recognize_google(audio)
	return recognized_text

st.title('Convert video to text')
text_frvid = ""
uploaded_file = st.file_uploader("Choose an mp4 file",type = "mp4", accept_multiple_files=False)
if uploaded_file is not None:
	save_uploadedfile(uploaded_file)
if st.button("Convert"):
	VIDEO_FILE = str(uploaded_file.name)
	video = VideoFileClip(VIDEO_FILE)
	convert_video2audio(video)
	text_frvid = transcript_audio()

st.write('Please wait until the button is highlighted')
st.download_button("Download transcript",text_frvid, file_name = "textfile.txt")


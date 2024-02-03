import streamlit as st
import os

from video_info import GetVideo
from model import Model
from prompt import Prompt



#Prompt for video
prompt01 = Prompt.prompt1()




def Homepage():
    st.title("AI Video Summarizer")

    youtube_url = st.text_input("Enter YouTube Video Link")

    if youtube_url:
        video_title = GetVideo.title(youtube_url)
        video_transcript = GetVideo.transcript(youtube_url)
        video_id = GetVideo.Id(youtube_url)
        st.write(video_title)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get summary"):
        #summary = Model.google_gemini(video_transcript,prompt01)
        st.markdown("## Summary :")
        st.write("summary")


Homepage()











#Imports
import streamlit as st
import os

#Local imports
from video_info import GetVideo
from model import Model
from prompt import Prompt


#Prompt for video
prompt01 = Prompt.prompt1()
prompt_time = Prompt.prompt1(ID='0t')

def Homepage():
    st.title("AI Video Summarizer")

    youtube_url = st.text_input("Enter YouTube Video Link")

    if youtube_url:
        video_title = GetVideo.title(youtube_url)
        video_transcript = GetVideo.transcript(youtube_url)
        video_transcript_time = GetVideo.transcript_time(youtube_url)
        video_id = GetVideo.Id(youtube_url)
        st.write(f"**{video_title}**")
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)


    genre = st.radio(
        "What do you want to generate for this video?",
        [":rainbow[**AI summary**]", "**Transcript**", "**Timestamps**"],
        captions = ["AI generated summary of the video", "Transcript/Subtitles of the video", "AI generated timestamps for main topics"])

    if genre == ':rainbow[**AI summary**]':
        if st.button(":rainbow[**Get summary**]"):
            try:
                summary = Model.google_gemini(video_transcript,prompt01)
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Summary :")
            st.write(summary)
    elif genre == '**Transcript**':
        if st.button('**Get Transcript**'):
            try:
                transcript = video_transcript
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Transcript :")
            st.write(transcript)
    else:
        if st.button("**Get Timestamps**"):
            try:
                TimeStamps = Model.google_gemini(video_transcript_time,prompt_time)
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Timestamps :")
            st.write(TimeStamps)


Homepage()











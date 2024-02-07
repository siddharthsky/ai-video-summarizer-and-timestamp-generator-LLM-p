#Imports
import streamlit as st
import os

#Local imports
from video_info import GetVideo
from model import Model
from prompt import Prompt


#Prompt for video
prompt01 = Prompt.prompt1()
prompt_time = Prompt.prompt1(ID='transcript')

def Homepage():
    st.set_page_config( page_title="AI Video Summarizer", 
                        page_icon="chart_with_upwards_trend")
    
    st.title("AI Video Summarizer")

    youtube_url = st.text_input("Enter YouTube Video Link")

    if youtube_url:
        video_id = GetVideo.Id(youtube_url)
        if video_id == None:
            st.write(f"**Error**")
            st.image(r"https://i.imgur.com/KWFtgxB.png", use_column_width=True)
            st.stop()

        video_title = GetVideo.title(youtube_url)
        st.write(f"**{video_title}**")
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)


    genre = st.radio(
        "What do you want to generate for this video?",
        [":rainbow[**AI summary**]", ":rainbow[**AI Timestamps**]", "**Transcript**"],
        captions = ["AI generated summary of the video","AI generated timestamps for main topics" , "Transcript/Subtitles of the video"])

    if genre == ':rainbow[**AI summary**]':
        if st.button(":rainbow[**Get summary**]"):
            try:
                video_transcript = GetVideo.transcript(youtube_url)
                summary = Model.google_gemini(video_transcript,prompt01)
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Summary :")
            st.write(summary)

    elif genre == ':rainbow[**AI Timestamps**]':
        if st.button(':rainbow[**Get Timestamps**]'):
            try:
                video_transcript_time = GetVideo.transcript_time(youtube_url)
                youtube_url_full = f"https://youtube.com/watch?v={video_id}"
                TimeStamps = Model.google_gemini(video_transcript_time,prompt_time,extra=youtube_url_full)
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Timestamps :")
            st.markdown(TimeStamps)

    else :
        if st.button('**Get Transcript**'):
            try:
                transcript = video_transcript
            except UnboundLocalError as err:
                st.write(f"Please enter the :rainbow[**YouTube Video**] link")
                st.stop()
            st.markdown("## Transcript :")
            st.write(transcript)
  
        

Homepage()











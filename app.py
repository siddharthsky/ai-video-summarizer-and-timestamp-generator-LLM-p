import streamlit as st
import pafy as p


class video_info():

    def __init__(self,link):
        video_info.get_title(link)
        video_info.get_transcript(link)

    def get_title(link):
        print(2)
        pass
       

    def get_transcript(link):
        print(3)
        pass



















def Homepage():
    st.title("AI Video Summarizer")

    youtube_url = st.text_input("Enter YouTube Video Link")

    if youtube_url:
        video_id = youtube_url.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get summary"):
        pass


Homepage()
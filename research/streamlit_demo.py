import streamlit as st

st.title("AI Video Summarizer")

youtube_url = st.text_input("Enter YouTube Video Link")

if youtube_url:
    video_id = youtube_url.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get summary"):
    pass
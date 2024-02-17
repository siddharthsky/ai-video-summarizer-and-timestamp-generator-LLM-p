import streamlit as st
from video_info import GetVideo
from model import Model
from prompt import Prompt

class AIVideoSummarizer:
    def __init__(self):
        self.youtube_url = None
        self.video_id = None
        self.video_title = None
        self.video_transcript = None
        self.video_transcript_time = None
        self.summary = None
        self.time_stamps = None
        self.transcript = None

    def get_youtube_info(self):
        self.youtube_url = st.text_input("Enter YouTube Video Link")
        if self.youtube_url:
            self.video_id = GetVideo.Id(self.youtube_url)
            if self.video_id is None:
                st.write("**Error**")
                st.image("https://i.imgur.com/KWFtgxB.png", use_column_width=True)
                st.stop()
            self.video_title = GetVideo.title(self.youtube_url)
            st.write(f"**{self.video_title}**")
            st.image(f"http://img.youtube.com/vi/{self.video_id}/0.jpg", use_column_width=True)

    def generate_summary(self):
        if st.button(":rainbow[**Get Summary**]"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            self.summary = Model.openai_chatgpt(self.video_transcript, Prompt.prompt1())
            st.markdown("## Summary:")
            st.write(self.summary)

    def generate_time_stamps(self):
        if st.button(":rainbow[**Get Timestamps**]"):
            self.video_transcript_time = GetVideo.transcript_time(self.youtube_url)
            youtube_url_full = f"https://youtube.com/watch?v={self.video_id}"
            self.time_stamps = Model.openai_chatgpt(self.video_transcript_time, Prompt.prompt1(ID='transcript'), extra=youtube_url_full)
            st.markdown("## Timestamps:")
            st.markdown(self.time_stamps)

    def generate_transcript(self):
        if st.button("Get Transcript"):
            self.transcript = self.video_transcript
            st.markdown("## Transcript:")
            st.write(self.transcript)

    def run(self):
        st.set_page_config(page_title="AI Video Summarizer", page_icon="chart_with_upwards_trend")
        st.title("AI Video Summarizer")
        self.get_youtube_info()
        genre = st.radio(
            "What do you want to generate for this video?",
            [":rainbow[**AI Summary**]", ":rainbow[**AI Timestamps**]", "**Transcript**"],
            index=0
        )
        if genre == ":rainbow[**AI Summary**]":
            self.generate_summary()
        elif genre == ":rainbow[**AI Timestamps**]":
            self.generate_time_stamps()
        else:
            self.generate_transcript()

if __name__ == "__main__":
    app = AIVideoSummarizer()
    app.run()

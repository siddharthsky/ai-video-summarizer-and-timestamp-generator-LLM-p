from youtube_transcript_api import YouTubeTranscriptApi 
from bs4 import BeautifulSoup
import requests


class GetVideo():
    def __init__(self):
        pass

    def title(link):
        r = requests.get(link) 
        s = BeautifulSoup(r.text, "html.parser") 
        title = s.find("meta", itemprop="name")["content"]
        return title
        
    def transcript(link):
        video_id = link.split("=")[1]
        transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
        final_transcript = ""
        for i in transcript_dict:
            final_transcript += " " + i["text"]
        return final_transcript
    
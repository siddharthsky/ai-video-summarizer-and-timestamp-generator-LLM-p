from youtube_transcript_api import YouTubeTranscriptApi 
from bs4 import BeautifulSoup
import requests


class GetVideo():
    def __init__(self):
        pass

    def Id(link):
        video_id = link.split("=")[1]
        return video_id
        
    def title(link):
        r = requests.get(link) 
        s = BeautifulSoup(r.text, "html.parser") 
        title = s.find("meta", itemprop="name")["content"]
        return title
        
    def transcript(link):
        video_id=GetVideo.Id(link)
        try:
            transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
            final_transcript = ""
            for i in transcript_dict:
                final_transcript += " " + i["text"]
            return final_transcript
        except Exception as e:
            print(e)

    def transcript_time(link):
        video_id=GetVideo.Id(link)
        
        try:
            transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
            transcript_dict = f"{transcript_dict}"
            return transcript_dict
    
        except Exception as e:
            print(e)
   